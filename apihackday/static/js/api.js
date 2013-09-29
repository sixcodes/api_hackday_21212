
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