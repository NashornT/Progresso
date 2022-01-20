function validação(array){
    const alunos = ['João','Paulo','Renato','Andressa','Bianca'];
    const  notas = [5,6,7,4.5,9];
    let média = 6.0;
    let contador = 0
    let Aprovados = []
    let reprovados = []
    let OutroCont = 0

    for (let i = 0 ; i < alunos.length ; i++  ){
        if (notas[contador] >= média){
            Aprovados.push(alunos[OutroCont])
            contador += 1
            OutroCont += 1
        }else if (notas[contador] < média){
            reprovados.push(alunos[OutroCont])
            contador += 1
            OutroCont += 1
        }

    }

console.log(Aprovados);
console.log(reprovados);
console.log(alunos);
}
validação();
