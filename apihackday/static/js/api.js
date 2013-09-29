
$(document).ready(function(e){
    listarBoloes;
});

listarBoloes = function(){
    $.get( "http://localhost:8000/api/v1/bolao/", function( data ) {
        var boloes = $.parseJSON(data.objects);

        var template = _.template($("#listar-template").html());
        $('#listar-render').html(template({'boloes': boloes}));
    });
};

getBolao = function(e){
    $.ajax({
            type: 'GET',
            url: '/api/v1/bolao/1',
            success: function(data){
                console.log(data);
                listarBoloes(data);
                return true;
            }
        });
};


saveBolao = function(e){
    var formData = JSON.stringify({
        'titulo': $("#id_titulo").val(),
        'time_1': $("#id_time1").val(),
        'time_2': $("#id_time2").val()

    });
    console.log(formData);
    $.ajax({
        type: 'POST',
        url: '/api/v1/bolao/',
        contentType: 'application/json  ',
        dataType: 'json',
        data: formData,
        success: function(data){
            console.log('oi');
            return false;
        }
    });
};

$('.js_save_bolao').live('click', function(e){
   saveBolao();
});
