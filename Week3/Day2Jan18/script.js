// Daily Challenge

let fruits = ["Banana", "Apples", "Oranges", "Blueberries"];
console.log(fruits);
fruits.shift();
console.log(fruits);
fruits.push('Kiwi');
console.log(fruits);
fruits.splice(0,1);
console.log(fruits);
let reverseFruits = [];
for(let fruit of fruits){
    reverseFruits.unshift(fruit);
}
console.log(reverseFruits);

console.log(fruits); 


// // Favorite Color

// let me = ["my","favorite","color","is","blue"]
// console.log(me.join(' '));

// // Mixup

// let str1 = 'mix'; 
// let str2 = 'pod'; 

// let newWord = (str2.slice(0,2) + str1.slice(-1)) + ' ' + (str1.slice(0,2) + str2.slice(-1))
// console.log(newWord)

// // Calculator

// let num1 = prompt('First number')
// let num2 = prompt('Second number')

// alert(Number(num1) + Number(num2))

// // Finding Nemo

// let string = 'I found Nemo at the order of the word you find!'
// let index = string.indexOf('Nemo');
// if(index != -1){
//     console.log(`I found Nemo at ${index}`)
// } else {
//     console.log('I did not find Nemo')
// }

// // XP Ninja
// // Exercise 3
// let addition = prompt('Enter two number seperated by a comma and a space')
// let additionArray = addition.split(', ');

// let sum = Number(additionArray[0]) + Number(additionArray[1]);
// alert(sum);

