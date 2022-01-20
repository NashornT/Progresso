function getAdimins (map){
    let ADMmap = [];
    for ([key,value] of map ){
        if (value === 'Admin'){
            ADMmap.push(key)  
        }    
    }
    return ADMmap;
}

const map = new Map();

map.set('Gustavo','Admin');
map.set('Renata','Jogador1');
map.set('Marcos','Jogador2');
map.set('Paloma','Admin');

console.log(getAdimins(map));