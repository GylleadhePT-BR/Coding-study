var num = document.getElementById('numero')
var lista = document.getElementById('list')
var res = document.getElementById('res')
var valores = []

function isNumero(n){
    if(Number(n) >= 1 && Number(n) <= 100){
        return true
    }else{
        return false
    }
}
function inLista(n ,l){
    if (l.indexOf(Number(n)) != -1){
        return true
    }else{
        return false
    }

}

function analisar(){
    if(isNumero(num.value) && !inLista(num.value,valores)){
        valores.push(Number(num.value))
        var item = document.createElement('option')
        item.text = `valor ${num.value} adicionado`
        lista.appendChild(item)
        res.innerHTML=''
    }else{
        alert('[ERRO] VALOR INVÀLIDO OU ENCONTRADO NA LiSTA')
    }
    num.value = ''
    num.focus()
}
 function finalizar(){
     if (valores.length == 0){
         alert('[ERRO] ADICIONE VALORES ANTES DE FINALIZAR!')
     }else{
         var total = valores.length
         var maior = Math.max.apply(Math ,valores)
         var menor = Math.min.apply(Math ,valores)
         var soma = 0
         var media = 0
         for(var pos in valores){
             soma += valores[pos]
         }
         media = soma / total
         res.innerHTML=''
         res.innerHTML += `<p> Ao todo temos ${total} valores! </p>`
         res.innerHTML += `<p> O maior numero dos valores é ${maior} e o menor numero é ${menor} </p>`
         res.innerHTML += `<p> A soma dos valores informados é ${soma} </p>`
         res.innerHTML += `A média aritmética dos valores é igual a ${media}`


     }
 }
