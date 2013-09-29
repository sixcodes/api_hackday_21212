
$(document).ready(function(e){
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
            url: '/api/v1/bolao/' + '1',
            success: function(data){
                console.log(data);
                listarBolao(data);
                return true;
            }
        });
};

$('.js_ver_bolao').live('click', function(e){
   getBolao();
});


saveBolao = function(e){
    var formData = JSON.stringify({
        'titulo': $("#id_titulo").val(),
        'time_1': $("#id_time1").val(),
        'time_2': $("#id_time2").val()
    });
    $.ajax({
        type: 'POST',
        url: '/api/v1/bolao/',
        contentType: 'application/json  ',
        dataType: 'json',
        data: formData,
        success: function(data){
            console.log(data);
            alert('O bolão foi criado com sucesso. Convide seus amigos.');
            window.location = "/convidar/" + data['id'];
            return false;
        }
    });
};

$('.js_save_bolao').live('click', function(e){
   saveBolao();
});
