const array = [1,2,3,4,5,6,7,8];

const pares = array.filter(filtro);

function filtro (num){
    return num %2 == 0
}

filtro();
console.log(pares)