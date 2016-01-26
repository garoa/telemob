(function() {
  var contact = {
    init: function(){
      contact.check_selected();
      $(document).on('change', 'select', function(){
        contact.check_selected();
        contact.change_optgroup();
      });
    },
    create_optgroup: function(group){
      var opt_group = '<option value="" selected="selected">---------</option>',
          opt_groups = {
        'Telefonei': [
          ['10', 'Falei com o(a) Deputado(a) em pessoa.'],
          ['11', 'Falei com outra pessoa.'],
          ['12', 'Deixei recado em uma máquina.'],
          ['13', 'Fone: número ocupado'],
          ['14', 'Fone: ninguém atendeu.'],
          ['15', 'Fone: número inexistente ou outra falha.']
        ],
        'Enviei telegrama': [
          ['20', 'Nada a reportar: correio vai entregar no gabinete!'],
        ],
        'Enviei fax': [
          ['30', 'Fax: transmissão bem sucedida.'],
          ['31', 'Fax: número ocupado.'],
          ['32', 'Fax: não atendeu.'],
          ['33', 'Fax: número inexistente ou outra falha.']
        ],
        'Enviei e-mail': [
          ['40', 'E-mail enviado e não voltou, tomara que leiam.'],
          ['41', 'E-mail voltou com erro.'],
        ]
      };

      if (group === 'all'){
        for (var group in opt_groups){
          opt_group = opt_group + '<optgroup label="'+group+'">';
          var group_list = opt_groups[group];
          for (var i=0,len=group_list.length; i<len; i++){
            opt_group = opt_group + '<option value="'+ group_list[i][0] +'" selected="selected">'+group_list[i][1]+'</option>';
          }
          opt_group = opt_group + '</optgroup>';
        }
      } else {
        var group_list = opt_groups[group];
        for (var i=0,len=group_list.length; i<len; i++){
            opt_group = opt_group + '<option value="'+ group_list[i][0] +'" selected="selected">'+group_list[i][1]+'</option>';
        }
      }
      return $(opt_group);
    },
    change_optgroup: function(){
      var selected = $('#id_contacted_by option:selected').val(),
          groups = {
        tel: 'Telefonei',
        telegram: 'Enviei telegrama',
        fax: 'Enviei fax',
        email: 'Enviei e-mail'
      };

      if (groups.hasOwnProperty(selected)){
        var opt_group = contact.create_optgroup(groups[selected]);
      } else {
        var opt_group = contact.create_optgroup('all');
      }
      $('#id_result').html(opt_group);
    },
    check_selected: function(){
      var result = $('#id_result optgroup option').is(':selected'),
          id_contacted = $('#id_contacted_by');

      if ( result && id_contacted.val() || id_contacted.val() === 'telegram' ) {
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
