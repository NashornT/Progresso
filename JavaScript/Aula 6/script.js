function calculadora(){
    const operação = prompt('escolha uma operação:\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Divisão real\n6 - Potenciação');
    
    let n1 = Number(prompt('Insira o primeiro valor'));
    let n2 = Number(prompt('Insira o segunda valor'));
    let resultado;

    if (!operação  || operação >= 7){
        alert('Opção Invalida')
        calculadora();
        }else{    
            function Soma(){
                resultado = n1 + n2;
                alert(`${n1}+${n2}=${resultado}`)
                NovaOp();
            }
            
            function Subtração(){
                resultado = n1 - n2;
                alert(`${n1}-${n2}=${resultado}`)
                NovaOp();
            }

            function Multiplicação(){
                resultado = n1*n2;
                alert(`${n1}x${n2}=${resultado}`)
                NovaOp();
            }

            function Divisão(){
                resultado = n1/n2;
                alert(`${n1}/${n2}=${resultado}`)
                NovaOp();
            }
            
            function Divisão_real(){
                resultado = n1%n2;
                alert(`${n1}%${n2}=${resultado}`)
                NovaOp();
            }

            function Potenciação(){
                resultado = n1**n2
                alert(`${n1}^${n2}=${resultado}`)
                NovaOp();

            }

            function NovaOp() {
                let op = prompt('Deseja fazer outra operação?\n1 - Sim\n2 - Não');

                if (op == 1){
                    calculadora();
                }else if (op == 2){
                    alert('Até Mais')
                }else{
                    alert('Opção invalida')
                    NovaOp();
                }
            }

            if (operação == 1) {
                Soma();
            }  else if (operação == 2){
                Subtração();     
            }   else if (operação ==3){
                Multiplicação();
            }   else if (operação == 4){
                Divisão();
            }   else if (operação == 5){
                Divisão_real();
            }   else if(operação == 6){
                Potenciação();
            }   
        }      
}
calculadora();
