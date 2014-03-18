(function() {
  var politician = {
    init: function() {
      var total = politician.getSumContacts();
      if (total === 1) msg = "1 contato"
      else msg = total + " contatos"
      $('#count-contacts').text("Total: "+msg);
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
