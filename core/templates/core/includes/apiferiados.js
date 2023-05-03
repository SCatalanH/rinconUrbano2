let url = "https://api.control-z.cl/api/feriados"
$get(url, function(respuesta)  {

    let feriado = respuesta [respuesta.length -1]

    $("#feriado").text(feriado.nombre + " - " + feriado)
},"json")
