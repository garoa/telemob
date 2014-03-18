(function() {
  var politician = {
    init: function() {
      $('.count-contacts').text(politician.getSumContacts());
    },

    getSumContacts: function() {
      var sum = 0;
      $('table').find('.pol-contacts').each(function( index, element ) {
        var aux = $(element).text(),
            count = parseFloat(aux);
        
        sum += count;
      });

      return sum;
    },
  };

  $(document).ready(function(){
    politician.init();
  });

})();
