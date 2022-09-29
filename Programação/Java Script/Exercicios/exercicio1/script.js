alert('Olá')
var nome = prompt('Qual o seu nome : ')
console.log(`Bom dia ${nome}!!`)
function carregar(){
    var msg = window.document.getElementById('msg')
    var img = window.document.getElementById('imagem')
    var data = new Date()
    var hora = data.getHours()
    msg.innerHTML= `Agora são ${hora} horas...` 
    if (hora >= 0 && hora < 12){
        document.body.style.background='#e2cd9f'
        img.src = 'manha.jpg'
    }
    else if(hora >= 12 && hora < 18){
        document.body.style.background='#b9846f'
        img.src = 'tarde.jpg'
    }else{
        document.body.style.background='#515154'
        img.src  ='noite.jpg'
    }
}
