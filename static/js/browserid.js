var CC = (function (CC, $) {

    'use strict';


    CC.browseridLogin = function (container) {
        var context = $(container),
            getAssertion = function () {
                navigator.id.get(gotAssertion);
            },
            gotAssertion = function (assertion) {
                if (assertion !== null) {
                    alert("asserted")
                /*    $.ajax({
                               type: 'POST',
                               url: '/login/login',
                               data: { assertion: assertion },
                               success: function(res, status, xhr) {
                                   if (res === null) loggedOut();
                                   else loggedIn(res);
                               },
                               error: function(xhr, status, error) {
                                   alert("login failure " + error);
                               }
                           });
                           */
                }
                else {
                    alert("nope();")
                }
            };
        context.find('.browserid').click(function (e) {
            e.preventDefault();
            getAssertion();
        });
    };


    return CC;

}(CC || {}, jQuery));

