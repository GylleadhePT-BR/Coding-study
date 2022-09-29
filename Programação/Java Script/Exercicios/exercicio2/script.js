function verificar(){
    var data = new Date()
    var ano = data.getFullYear()
    var nasc = document.getElementById('nascimento')
    var res = document.getElementById('res')
    if (nasc.value.length == 0 || nasc.value > ano){
        window.alert('Verifique os dados e tente novamente..')
    } 
    else{
        var fsex = document.getElementsByName('sex')
        var idade = ano - Number(nasc.value)
        var genero = ''
        var img = document.createElement('img')
        img.setAttribute('id','foto')
        if (fsex[0].checked){
            genero = 'homem'
            if(idade >=0 && idade <= 5){
                res.innerHTML=`Analisamos um bebê menino de ${idade} anos`
                img.setAttribute('src','bebê -h.jpg')
            }else if (idade > 5 && idade<=11){
                res.innerHTML=`Analisamos um garoto de ${idade} anos`
                img.setAttribute('src','criança -h.jpg')
            }else if (idade >11 && idade <=18){
                res.innerHTML=`Analisamos um adolescente de ${idade} anos`
                img.setAttribute('src','adolescente -h.jpg')
            }else if (idade >18 && idade <=30){
                res.innerHTML=`Analisamos um jovem de ${idade} anos`
                img.setAttribute('src','jovem -h.jpg')
            }else if (idade >30 && idade <=60){
                res.innerHTML=`Analisamos um Homem de ${idade} anos`
                img.setAttribute('src','adulto -h.jpg')
            }else{
                res.innerHTML=`Analisamos um Idoso de ${idade} anos`
                img.setAttribute('src','idoso -h.jpg')
            }
        }else if (fsex[1].checked){
            genero = 'mulher'
            if(idade >=0 && idade <= 5){
                res.innerHTML=`Analisamos um bebê feminino de ${idade} anos`
                img.setAttribute('src','bebê -m.jpg')
            }else if (idade > 5 && idade<=11){
                res.innerHTML=`Analisamos uma garoto de ${idade} anos`
                img.setAttribute('src','criança -m.jpg')
            }else if (idade >11 && idade <=18){
                res.innerHTML=`Analisamos uma adolescente de ${idade} anos`
                img.setAttribute('src','adolescente -m.jpg')
            }else if (idade >18 && idade <=30){
                res.innerHTML=`Analisamos uma jovem de ${idade} anos`
                img.setAttribute('src','jovem -m.jpg')
            }else if (idade >30 && idade <=60){
                res.innerHTML=`Analisamos uma Mulher de ${idade} anos`
                img.setAttribute('src','adulta -m.jpg')
            }else{
                res.innerHTML=`Analisamos uma Idosa de ${idade} anos`
                img.setAttribute('src','idosa -m.jpg')
            }
        }
        res.style.textAlign='center'
        res.appendChild(img)
    } 
}
