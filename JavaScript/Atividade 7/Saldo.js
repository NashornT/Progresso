const preços = [10,25,100,349,1010];

const valor =  preços.reduce(valor1);

function valor1 (total,num){
    return total + num;
}



function saldo (){
    var saldo = 2400 ;
    if (saldo < valor){
        console.log('Saldo Insuficiente.')
    }else{
        console.log('Este é o seu saldo restante.')
        console.log("R$"+`${saldo - valor}`);
        return saldo - valor;
        
    }
}

saldo();
valor1();
console.log('Este é o valor total a ser pago.')
console.log("R$"+`${valor}`);