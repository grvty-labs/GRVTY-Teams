/*!
 * remark v1.1.2 (http://getbootstrapadmin.com/remark)
 * Copyright 2015 amazingsurge
 * Licensed under the Themeforest Standard Licenses
 */
(function(document, window, $) {
  'use strict';
  (function() {
    var defaults = $.components.getDefaults("wizard");
    var options = $.extend(true, {}, defaults, {
      onInit: function() {
        console.log('ON INIT');
      },
      onFinish: function() {
        console.log('ON FINISH');
      },
      buttonsAppendTo: '.panel-body'
    });

    $("#completeProfileWizardFormContainer").wizard(options);
  })();
})(document, window, jQuery);
