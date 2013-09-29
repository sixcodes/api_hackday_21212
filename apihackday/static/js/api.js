
$(document).ready(function(e){

});

listarBoloes = function(data){
    var template = _.template($("#bolao-template").html());
    $('#bolao-render').html(template({'bolao': data}));

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