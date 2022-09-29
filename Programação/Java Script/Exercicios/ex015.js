let numeros = [3,6,5,1,8,6,9,5,7,]
numeros.push(1)
numeros.sort()
for(let pos in numeros){
    console.log(`Numero ${numeros[pos]} na posição ${pos}`)
}