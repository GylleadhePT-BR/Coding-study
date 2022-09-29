var numero = document.getElementById("num");
var contador = 0
function subtrair(){
    contador = contador - 1
    num.innerHTML=`${contador}`
}
function zerar(){
    contador = 0
    num.innerHTML=`${contador}`
}
function somar(){
    contador = contador + 1
    num.innerHTML=`${contador}`
}