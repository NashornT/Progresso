function operador(){

    let n1 = Number(prompt('1° Número'));
    let n2 = Number(prompt('2° Número'));
    let n3 = n1 + n2;
    
    if (n3 > 10 && n3 < 20){
        if (n1 === n2){
            alert(`Os números ${n1} e ${n2} são iguais. Sua soma é ${n3} que é maior que 10 e menor que 20. ` );
        }else{
            alert(`Os números ${n1} e ${n2} são diferentes. Sua soma é ${n3} que é maior que 10 e menor que 20. ` );
        }

    }else if (n3 > 10 && n3 > 20)
        if (n1 === n2){
            alert(`Os números ${n1} e ${n2} são iguais. Sua soma é ${n3} que é maior que 10 e maior que 20. ` );
        }else{
            alert(`Os números ${n1} e ${n2} são diferentes. Sua soma é ${n3} que é maior que 10 e maior que 20. ` );
    }else if (n3 < 10 ){
        if (n1 === n2){
            alert(`Os números ${n1} e ${n2} são iguais. Sua soma é ${n3} que é menor que 10 e menor que 20. ` );
        }else{
            alert(`Os números ${n1} e ${n2} são diferentes. Sua soma é ${n3} que é menor que 10 e menor que 20. ` );
        }
        
    }else if (n3 >10 ){
        if (n1 === n2 && n1 == 10 && n2 == 10){
            alert(`Os números ${n1} e ${n2} são iguais. Sua soma é ${n3} que é maior que 10 e igual a 20. ` );
        }else{
            alert(`Os números ${n1} e ${n2} são diferentes. Sua soma é ${n3} que é maior que 10 e maior que 20. ` );
        }
    }
        


}
console.log(operador());