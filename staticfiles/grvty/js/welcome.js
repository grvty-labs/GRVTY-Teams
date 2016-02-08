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
      onNext: function(from, to) {
        if (to.$pane.attr('id') == 'FinishProfile3'){
          $('.sweet-alert .icon.success').addClass('animate');
          $('.sweet-alert .icon.success .line.tip').addClass('animateSuccessTip');
          $('.sweet-alert .icon.success .line.long').addClass('animateSuccessLong');
          finishProfile();
        }
      },
      onBack: function(from, to) {
        $('.sweet-alert .icon.success').removeClass('animate');
        $('.sweet-alert .icon.success .line.tip').removeClass('animateSuccessTip');
        $('.sweet-alert .icon.success .line.long').removeClass('animateSuccessLong');
      },
      buttonsAppendTo: '.panel-body'
    });

    $("#completeProfileWizardFormContainer").wizard(options);
  })();
})(document, window, jQuery);
