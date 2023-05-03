
$.getJSON('https://mindicador.cl/api', function(data) {
    var dailyIndicators = data;

    $("#indicador").text(" El valor actual de la UF es $ " + + dailyIndicators.uf.valor)


}).fail(function() {
    console.log('Error al consumir la API!');
});

