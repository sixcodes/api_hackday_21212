
$(document).ready(function(e){
    function todosBoloes(){
        boloes = {
            "Bolao":
            {
                "titulo": "Bolão HACKDAY",
                "time_1": "Brasil",
                "time_2": "Argentina",
                "resultado_time_1": 3,
                "resultado_time_2": 1,
                "admin": "Bruno Melo",
                "encerrado": 1
            },

            "Bolao":
            {
                "titulo": "Imagina na copa",
                "time_1": "Brasil",
                "time_2": "Uruguai",
                "resultado_time_1": 0,
                "resultado_time_2": 0,
                "admin": "JJ",
                "encerrado": 0
            },

            "Bolao":
            {
                "titulo": "Campeonato Carioca",
                "time_1": "Flamengo",
                "time_2": "Fluminence",
                "resultado_time_1": 2,
                "resultado_time_2": 2,
                "admin": "Bruno Melo",
                "encerrado": 1
            }
        };

        var template = _.template($("#listar-boloes").html());
        $('#panel-group').html(template({'bolao': boloes}));

    }
});

listarBoloes = function(data){
    console.log(data);
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