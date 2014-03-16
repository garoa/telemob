(function() {
  contact = {
    init: function(){
      contact.check_selected();
      $(document).on('change', 'select', function(){
        contact.check_selected();
      });
    },

    check_selected: function(){
      var contacted_by = $('#id_contacted_by option').is(':selected'),
          result = $('#id_result optgroup option').is(':selected'),
          id_contacted = $('#id_contacted_by');

      if ( contacted_by && result && id_contacted.val() ) {
        $('.send-button').removeClass('disabled');
      } else {
        $('.send-button').addClass('disabled');
      }
    },
  };

  $(document).ready(function(){
    contact.init();
  });
})();
