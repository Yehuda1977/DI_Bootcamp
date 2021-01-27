// You know the infamous song “99 Bottles of Beer?”

// You need to generate in JavaScript the lyrics to the song 99 Bottles of Beer as an output.

// Ask the user to input a starting number of bottles of beer, and start the bottles falling.
// But instead of 1 falling each time, the number falling goes up by one each time.

// ==============================

// 99 bottles of beer on the wall
// 99 bottles of beer
// Take 1 down, pass it around
// 98 bottles of beer on the wall
// 98 bottles of beer on the wall
// 98 bottles of beer
// Take 2 down, pass them around
// 96 bottles of beer on the wall
// 96 bottles of beer on the wall
// 96 bottles of beer
// Take 3 down, pass them around
// 93 bottles of beer on the wall

// ==============================

// How will you choose to make the song end?
// Make sure you get the grammer right…
// For 1 bottle, you pass “it” around.
// For more than one bottle, you pass “them” around.

const bearBottles = (number) => {
    let takeDown = 1;
    while(number!=1){
        console.log(`
        ${number} bottles of beer on the wall
        ${number} bottles of beer 
        Take ${takeDown} down, pass ${takeDown===1?'it':'them'} around
        No bottles of beer on the wall`)
        number--;
        takeDown++;
    } 
        console.log(`
        ${number} bottle of beer on the wall
        ${number} bottle of beer 
        Take it down, pass it around
        No bottles of beer on the wall`)
   
        
    
}

let number = prompt('How many bottles of beer are on your wall?')
console.log(bearBottles(number))