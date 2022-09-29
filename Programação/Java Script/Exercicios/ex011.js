var idade = 70
if (idade < 16){
     console.log('Infelizmente não tem idade suficiente para votar')
}
else{
    if(idade >= 16 && idade < 18 ){
        console.log('Voto é opcional  ..')
    }
    if(idade >= 18 && idade < 65){
        console.log('O voto é obrigatorio')
    }
    if(idade >= 65){
        console.log('O voto é opcional')
    }
}