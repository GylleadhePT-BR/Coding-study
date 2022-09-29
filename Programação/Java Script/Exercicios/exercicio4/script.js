function tabuada(){
    var n = document.getElementById('numero')
    var tabu = document.getElementById('tab')

    if(n.value.length==0){
        window.alert('[ERRO]!! digite algum numero para ser cauculado...')
    }else{
        var nt = Number(n.value) //converte as variaveis para ser um numero
        var c = 1
        tabu.innerHTML = '' //faz com que o espaço da tabuada fique limpe a cada novo cauculo
        while (c <= 10){
            var item = document.createElement('option')
            item.text = `${nt} x ${c} = ${nt*c}`
            tabu.appendChild(item)
            c++
        }
    }
}