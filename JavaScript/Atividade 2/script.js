function trocador(){
    let contador = 0
    const lista = [1,2,3,4,5,6,7,8,9,10,11,12]
   switch(lista.values(contador)%2== 0 && lista.values(contador) != 0 ){
       case 1 :
           var index =  lista.values(contador).indexOf(contador);
           if (index !== -1){
               lista.values(contador)[index] = 0
           }
           break;
        default :
        alert('Algo deu errado')
   }
}
console.log(trocador());
