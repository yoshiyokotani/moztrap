var CC = (function (CC, $) {

    'use strict';

    // hide empty run-tests environments form on initial load
    CC.browseridLogin = function () {
        navigator.id.get(function (assertion) {
            if (assertion) {
                // This code will be invoked once the user has successfully
                // selected an email address they control to sign in with.
            } else {
                // something went wrong!  the user isn't logged in.
            }
        });
    };
});


