const nombre = document.getElementById("firstname")
const apellido = document.getElementById("lastname")
const username= document.getElementById("validationCustomUsername")
const acuerdo = document.getElementById("invalidCheck")
const form = documento.getElementById("form")
const parrafo = document.getElementById("warnings")

form.addEventListener("submit", e=>{
    e.preventDefault()
    if(nombre.nodeValue.length <2){
        alert("Nombre muy corto")
    }
})