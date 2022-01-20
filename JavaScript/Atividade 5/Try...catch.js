function parâmetros(arr , numb){
    try{
        if(!arr && !numb)  
            throw new ReferenceError('Envie os parâmetros.');

        if (typeof arr !== 'object' )
            throw new TypeError('Arr precisa ser do tipo Object.');

        if (typeof numb !== 'number')
            throw new TypeError('Numb precisa ser do tipo Number.');

        if (arr.length !== numb)
            throw new RangeError('Tamanho inválido.');
    
        return arr;
    }
    catch(e){
        if (e instanceof ReferenceError){
        console.log('Este é um ReferenceError!!')
        console.log(e.message);
        }else if (e instanceof TypeError){
        console.log('Este é um TypeError!!')
        console.log(e.message);
        }else if (e instanceof RangeError){
        console.log('Este é um RangeError')
        console.log(e.message);
        }else{
        console.log('Error não previsto!!' + e)
        }
    }
}
console.log(parâmetros([],'a'));
