function palindromo(){
    var palin = prompt('Digite um palindromo');
    let novoP = palin.split('').reverse().join('');
    if (palin == novoP){
        alert(`A palavra ${palin} é um palindromo.`)
    }else{
       alert(`A palavra ${palin} não é um palindromo.`)
    }
}

palindromo();