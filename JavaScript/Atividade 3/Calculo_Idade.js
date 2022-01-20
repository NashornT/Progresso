function calculoid(anos){
    return `Daqui a ${anos} anos, ${this.nome} terá ${this.idade + anos} anos de idade.`;

}

const pe1 = {
    nome : 'José',
    idade: 21
};

const pe2 = {
    nome : 'Gustavo',
    idade: 22
};

const pe3 = {
    nome: 'Vanessa',
    idade: 18
};

const pe4 = {
    nome: 'Angela',
    idade: 23
};


console.log(calculoid.call(pe3,10));