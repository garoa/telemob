(function() {
  contact = {
    init: function(){
      contact.check_selected();
      $(document).on('change', 'select', function(){
        contact.check_selected();
      });
    },

    check_selected: function(){
      var result = $('#id_result optgroup option').is(':selected'),
          id_contacted = $('#id_contacted_by');

      if ( result && id_contacted.val() ) {
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
