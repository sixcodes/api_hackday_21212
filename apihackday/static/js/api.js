
$(document).ready(function(e){

});

listarBolao = function(data){
    var template = _.template($("#bolao1-template").html());
    $('#bolao-render').html(template({'bolao': data}));

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
            alert('O bolão foi criado com sucesso. Convide seus amigos.');
            window.location = "/convidar"
            return false;
        }
    });
};

$('.js_save_bolao').live('click', function(e){
   saveBolao();
});