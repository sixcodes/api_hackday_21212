
$(document).ready(function(e){

});

listarBoloes = function(){
    var template = _.template($("#boloes-template").html());
    $('#bolao-render').html(template({'boloes': data}));

};

getBolao = function(e){
    $.ajax({
            type: 'GET',
            url: '/api/v1/bolao/',
            success: function(data){
                console.log(data);
                listarBoloes(data);
                return true;
            }
        });
};