import time
import urllib
from datetime import datetime
from mock import patch

from django.utils import unittest

from tests.case.api import ApiTestCase

import logging
mozlogger = logging.getLogger('moztrap.test')


class ApiCrudCases(ApiTestCase):
    """Re-usable test cases for Create, Read, Update, and Delete.

    Child classes must implement the following abstract methods:
      - factory(self)                           (property)
      - resource_name(self)                     (property)
      - permission(self)                        (property)
      - new_object_data(self)                   (property)
      - backend_object(self, id)                (method)
      - backend_data(self, backend_object)      (method)

    If any of these properties / methods are called on a child class without
    having implemented them, a NotImplementedError will be thrown.

    Child classes are may extend setUp() to provide required fixtures.

    The test methods provided by this class are:
      - test_create()
      - test_create_fails_with_wrong_perms()
      - test_read_list()
      - test_read_detail()
      - test_update_detail()
      - test_update_list_forbidden()
      - test_update_fails_without_creds()
      - test_delete_detail_perminant()
      - test_delete_detail_soft()
      - test_delete_list_forbidden()
      - test_delete_fails_with_wrong_perms()

    Child classes may override these methods if necessary.
    """


    @property
    def factory(self):
        """The factory to use to create fixtures of the object under test.
        Example: self.F.SuiteFactory()
        """
        raise NotImplementedError


    @property
    def is_abstract_class(self):
        """This is used to keep the tests from running them on the abstract
        class.

        It is needed because the django test collector matches path names to
        /test*.py/, which all matches .py files in the tests/ directory.
        The test framework will run the tests for ApiCrudCases, but all of them
        will return without doing anything or asserting on anything.
        """
        if self.__class__.__name__ == "ApiCrudCases":
            return True
        return False


    @property
    def resource_name(self):
        """String defining the resource name.
        Example: "suite"
        """
        raise NotImplementedError


    @property
    def permission(self):
        """String defining the permission required for
        Create, Update, and Delete.
        Example: "library.manage_suites"
        """
        raise NotImplementedError


    @property
    def wrong_permissions(self):
        """String defining permissions that will NOT work for this object.
        This method will only need to be overwritten in ProductResourceTest.
        """
        if self.__class__.__name__ == "ProductResource":
            raise NotImplementedError
        else:
            return "core.manage_products"


    @property
    def new_object_data(self):
        """Generates a dictionary containing the field names and auto-generated
        values needed to create a unique object.

        The output of this method can be sent in the payload parameter of a
        POST message.
        """
        raise NotImplementedError


    def backend_object(self, id):
        """Returns the object from the backend, so you can query it's values in
        the database for validation.
        """
        raise NotImplementedError


    def backend_data(self, backend_object):
        """Query's the database for the object's current values. Output is a
        dictionary that should match the result of getting the object's detail
        via the API, and can be used to verify API output.

        Note: both keys and data should be in unicode
        """
        raise NotImplementedError


    def clean_backend_data(self, backend_obj):
        """Returns backend_data, minus any keys not generated by
        new_object_data.
        Use this for comparing to input fields of a POST or PUT.

        Should be extended for objects that have one-to-many foriegn keys.
        """
        data = self.backend_data(backend_obj)
        data.pop("id")
        data.pop("resource_uri")
        return data


    def backend_meta_data(self, backend_obj):
        """Query's the database for the object's current values for:
          - created_on
          - created_by
          - modified_on
          - modified_by
          - deleted_on
          - deleted_by

        Returns a dictionary of these keys and their values.
        Used to verify that the CRUD methods are updating these
        values.
        """
        actual = {}
        try:
            actual["created_by"] = backend_obj.created_by.username
        except AttributeError:
            actual["created_by"] = None
        try:
            actual["modified_by"] = backend_obj.modified_by.username
        except AttributeError:
            actual["modified_by"] = None
        try:
            actual["deleted_by"] = backend_obj.deleted_by.username
        except AttributeError:
            actual["deleted_by"] = None

        actual["created_on"] = backend_obj.created_on
        actual["modified_on"] = backend_obj.modified_on
        actual["deleted_on"] = backend_obj.deleted_on

        return actual


    def manipulate_edit_data(self, fixture, fields):
        """may be used to replace items in the fields dicts with the values
        from the fixture, so as not to disturb read-only fields."""
        return fields


    @property
    def datetime(self):
        """May be used to provide mostly-unique strings"""
        return datetime.utcnow().isoformat()


    def setUp(self):
        """Set-up for all CRUD test cases.
        Sets the follwing attributes on self:
          - user
          - apikey
          - credentials

        self.credentials can be sent in the params parameter of POST, PUT, and
        DELETE messages, but should not be required for GET messages.

        Also mocks datetime.utcnow() with datetime in self.utcnow.
        """
        if self.is_abstract_class:
            return

        # credentials
        self.user = self.F.UserFactory.create(permissions=[self.permission])
        self.apikey = self.F.ApiKeyFactory.create(owner=self.user)
        self.credentials = {
            "username": self.user.username,
            "api_key": self.apikey.key}

        # mocking
        self.utcnow = datetime(2011, 12, 13, 22, 39)
        patcher = patch("moztrap.model.mtmodel.datetime")
        self.mock_utcnow = patcher.start().datetime.utcnow
        self.mock_utcnow.return_value = self.utcnow
        self.addCleanup(patcher.stop)


    def _id_from_uri(self, uri):
        return uri.split('/')[-2]


    # test cases

    def test_create(self):
        """Creates an object using the API.
        Verifies that the fields sent in the message have been set in
        the database.
        Verifies that the created_on and created_by have been set in
        the database.
        """
        if self.is_abstract_class:
            return
        mozlogger.info('test_create')

        # get data for creation
        fields = self.new_object_data

        # do the create
        res = self.post(
            self.get_list_url(self.resource_name),
            params=self.credentials,
            payload=fields,
            )

        # make sure response included detail uri
        object_id = self._id_from_uri(res.headers["location"])
        self.assertIsNotNone(object_id)

        # get data from backend
        backend_obj = self.backend_object(object_id)
        created_object_data = self.clean_backend_data(backend_obj)

        # compare backend data to desired data
        self.maxDiff = None
        mozlogger.debug("actual: %s", created_object_data)
        mozlogger.debug("expected: %s", fields)
        self.assertEqual(created_object_data, fields)

        # make sure meta data is correct
        created_obj_meta_data = self.backend_meta_data(backend_obj)
        self.assertEqual(
            created_obj_meta_data["created_by"], self.user.username)
        self.assertEqual(created_obj_meta_data["created_on"], self.utcnow)
        self.assertEqual(
            created_obj_meta_data["modified_by"], self.user.username)
        self.assertEqual(created_obj_meta_data["modified_on"], self.utcnow)


    def test_create_fails_with_wrong_perms(self):
        """Attempts to create an object using a user who has the wrong perms.
        Verifies that the POST message gets a 401 response.
        """
        if self.is_abstract_class:
            return
        mozlogger.info('test_create_fails_with_wrong_perms')

        # get data for creation
        fields = self.new_object_data

        # get user with wrong permissions
        user = self.F.UserFactory.create(permissions=[self.wrong_permissions])
        apikey = self.F.ApiKeyFactory.create(owner=self.user)
        credentials = {"username": user.username, "api_key": apikey.key}

        res = self.post(
            self.get_list_url(self.resource_name),
            params=credentials,
            payload=fields,
            status=401,
            )


    def test_read_list(self):
        """Performs a GET on the list without credentials.
        Verifies that the meta data returned by the API is correct.
        Verifies that the objects returned by the API have the correct data.
        """
        if self.is_abstract_class:
            return
        mozlogger.info('test_read_list')

        # create fixture
        fixture1 = self.factory
        fixture2 = self.factory

        # fetch list (ordered so assert won't flake)
        res = self.get_list(params={'order_by': 'id'})  # no creds

        act = res.json

        act_meta = act["meta"]
        exp_meta = {
            u"limit": 20,
            u"next": None,
            u"offset": 0,
            u"previous": None,
            u"total_count": 2,
            }

        self.assertEquals(act_meta, exp_meta)

        act_objects = act["objects"]
        exp_objects = [
            self.backend_data(fixture1),
            self.backend_data(fixture2)
            ]

        self.maxDiff = None
        self.assertEqual(exp_objects, act_objects)


    def _test_filter_list_by(self, key, value, expected_number_of_results):
        """Performs a get on the list with the supplied filter.
        Validates that the results meet the criteria.

        ::example::

        self._test_filter_list_by(u'name', u'foo', 1)
        self._test_filter_list_by(u'product', u'', 3)
        """

        res = self.get_list(params={key: value})
        objects = res.json["objects"]

        # validate
        self.assertEqual(len(objects), expected_number_of_results)
        for obj in objects:
            if value:
                # can't use assertEqual here because for foriegn keys,
                # the filter must be an id
                # but the value in the response is an uri
                self.assertTrue(value in obj[key])
            else:
                # case for value being None
                self.assertEqual(value, obj[key])


    def test_read_detail(self):
        """Performs a GET on the object detail without credentials.
        Verifies that the object returned by the API has the correct data.
        """
        if self.is_abstract_class:
            return
        mozlogger.info('test_read_detail')

        # create fixture
        fixture1 = self.factory

        # fetch detail
        res = self.get_detail(fixture1.id)  # no creds

        actual = res.json

        expected = self.backend_data(fixture1)

        self.maxDiff = None
        self.assertEqual(expected, actual)


    def test_update_detail(self):
        """Performs a PUT on the object detail.
        Verifies that the values in the database entry for the object has
        been updated.
        Verifies that the object's modified_on and modified_by have been
        updated.
        """
        if self.is_abstract_class:
            return
        mozlogger.info('test_update_detail')

        # create fixture
        fixture1 = self.factory
        # change modified on to 2 hours earlier than utcnow
        fixture1.modified_on = datetime(2011, 12, 13, 20, 39)
        meta_before = self.backend_meta_data(fixture1)
        obj_id = str(fixture1.id)
        fields = self.new_object_data

        # make read-only fields unchanging
        fields = self.manipulate_edit_data(fixture1, fields)

        # do put
        res = self.put(
            self.get_detail_url(self.resource_name, obj_id),
            params=self.credentials,
            data=fields
            )

        # make sure object has been updated in the database
        fixture1 = self.refresh(fixture1)
        backend_data = self.clean_backend_data(fixture1)

        self.maxDiff = None
        self.assertEqual(fields, backend_data)

        # make sure 'modified' meta data has been updated
        meta_after = self.backend_meta_data(fixture1)
        self.assertEqual(meta_after["modified_by"], self.user.username)
        self.assertEqual(meta_after["modified_on"], self.utcnow)
        self.assertNotEqual(
            meta_before['modified_on'], meta_after['modified_on'])


    def test_update_list_forbidden(self):
        """Attempts to PUT to the list uri.
        Verifies that the request is rejected with a 405 error.
        """
        if self.is_abstract_class:
            return
        mozlogger.info('test_update_list_forbidden')

        # create fixturs
        fixture1 = self.factory
        fixture2 = self.factory

        backend_obj1 = self.backend_object(fixture1.id)
        backend_obj2 = self.backend_object(fixture2.id)
        fields1 = self.backend_data(backend_obj1)
        fields2 = self.backend_data(backend_obj2)
        fields1.update(self.new_object_data)
        fields2.update(self.new_object_data)
        data = [fields1, fields2]

        # do put
        res = self.put(
            self.get_list_url(self.resource_name),
            params=self.credentials,
            data=data,
            status=405
            )


    def test_update_fails_without_creds(self):
        """Attempts to PUT to the object detail uri without credentials.
        Verifies that the request is denied with a 401 error.
        """
        if self.is_abstract_class:
            return
        mozlogger.info('test_update_fails_without_creds')

        # create fixture
        fixture1 = self.factory
        backend_obj = self.backend_object(fixture1.id)
        obj_id = str(fixture1.id)
        fields = self.backend_data(backend_obj)
        fields.update(self.new_object_data)

        # do put
        res = self.put(
            self.get_detail_url(self.resource_name, obj_id),
            data=fields,
            status=401,
            )


    def test_delete_detail_permanent(self):
        """Tests that an object can be deleted permanently.
        Verifies that the object no longer appears in the database after
        the delete.
        """
        if self.is_abstract_class:
            return
        mozlogger.info('test_delete_detail_permanent')

        # create fixture
        fixture1 = self.factory
        obj_id = str(fixture1.id)

        # check meta data before
        meta_before_delete = self.backend_meta_data(
            self.backend_object(obj_id))
        self.assertIsNone(meta_before_delete["deleted_on"])
        self.assertIsNone(meta_before_delete["deleted_by"])

        # do delete
        params = self.credentials
        params.update({"permanent": True})
        self.delete(self.resource_name, obj_id, params=params, status=204)

        from django.core.exceptions import ObjectDoesNotExist

        with self.assertRaises(ObjectDoesNotExist):
            meta_after_delete = self.backend_meta_data(
                self.backend_object(obj_id))


    def test_delete_detail_soft(self):
        """Tests that an object can be 'soft' deleted.
        Verifies that the object still exists in the database.
        Verifies that the object's deleted_by and deleted_on properties have
        been set.
        """
        if self.is_abstract_class:
            return
        mozlogger.info('test_delete_detail_soft')

        # create fixture
        fixture1 = self.factory
        obj_id = str(fixture1.id)
        backend_obj = self.backend_object(obj_id)
        # set created_on to 2 hours earlier than utcnow
        backend_obj.created_on = datetime(2011, 12, 13, 20, 39)

        # check meta data before
        meta_before_delete = self.backend_meta_data(backend_obj)
        self.assertIsNone(meta_before_delete["deleted_on"])
        self.assertIsNone(meta_before_delete["deleted_by"])

        # do delete
        self.delete(
            self.resource_name,
            obj_id,
            params=self.credentials,
            status=204)

        # check meta data after
        meta_after_delete = self.backend_meta_data(
            self.backend_object(obj_id))
        self.assertEqual(meta_after_delete["deleted_on"], self.utcnow)
        self.assertEqual(meta_after_delete["deleted_by"], self.user.username)
        self.assertNotEqual(
            meta_before_delete["deleted_on"], meta_after_delete["deleted_on"])


    def test_delete_list_forbidden(self):
        """Attempts to send a DELETE message to the list uri.
        Verifies that the message recieves a 405 error.
        """
        if self.is_abstract_class:
            return
        mozlogger.info('test_delete_list_forbidden')

        url = self.get_list_url(self.resource_name)
        url = "{0}?{1}".format(url, urllib.urlencode(self.credentials))
        self.app.delete(url, status=405)


    def test_delete_fails_with_wrong_perms(self):
        """Attempts to send a DELETE message with the wrong credentials.
        Verifies that the message recieves a 401 error.
        Verifies that object still exists.
        Verifies that delete meta data has not been set on object.
        """
        if self.is_abstract_class:
            return
        mozlogger.info('test_delete_fails_with_wrong_perms')

        # create fixture
        fixture1 = self.factory
        obj_id = str(fixture1.id)

        # get user with wrong permissions
        user = self.F.UserFactory.create(permissions=[self.wrong_permissions])
        apikey = self.F.ApiKeyFactory.create(owner=user)
        credentials = {"username": user.username, "api_key": apikey.key}

        # do delete
        self.delete(self.resource_name, obj_id, params=credentials, status=401)

        # make sure object is still found
        backend_obj = self.backend_object(obj_id)

        # and delete meta data has not been set
        meta_after_delete = self.backend_meta_data(backend_obj)
        self.assertIsNone(meta_after_delete["deleted_on"])
        self.assertIsNone(meta_after_delete["deleted_by"])
