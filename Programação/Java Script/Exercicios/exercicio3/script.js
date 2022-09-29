function contar(){
    var i = document.getElementById('numero1')
    var f = document.getElementById('numerof')
    var p = document.getElementById('passo')
    var res = document.getElementById('res')

    if(i.value.length==0||f.value.length==0||p.value.length==0){
        window.alert('[ERRO]!!!😵 , Digite algo para ser possivel a execção do cauculo....')
        res.innerHTML = 'Impossivel contar..'
    }else{
        res.innerHTML = 'Contando...'
        var ini = Number(i.value)
        var fim = Number(f.value)
        var pula = Number(p.value)
        if( ini < fim){
            //contagem crescente
            for(var c = ini;c <= fim ; c+= pula ){
                res.innerHTML += ` ➡️${c}`
            }
           res.innerHTML += `✌️` 
        }else{
            //contagem regressiva
            for(var c = ini ; c >= fim; c -= pula){
                res.innerHTML += ` ➡️${c}`
            }
            res.innerHTML += `✌️` 
        }
    }
}