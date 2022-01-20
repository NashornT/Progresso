const array = [1,2,3,4,5,6,7];

const Tot = array.reduce(total);

function total (total,num){
    return total + num;
}

total();

console.log(Tot)
