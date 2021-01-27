// Exercise 1 : Keyless Car
// 1. Ask the user for his age, and save the value into a variable
// 2. Create a function called checkDriverAge() that will alert the user if he can drive depending on his age.
//     --if he is too young, alert “Sorry, you are too young to drive this car. Powering off”
//     --if he is old enough, alert “You are old enough to drive, Powering On. Enjoy the ride!”
//     --if he just turned 18, alert “Congratulations on your first year of driving. Enjoy the ride!”
// 3. Instead of using prompt to ask the user for his age, make the checkDriverAge() function 
// accept an argument age, 
// so that if you enter: checkDriverAge(92); 
// it alerts “You are old enough to drive, Powering On. Enjoy the ride!”

const checkDriverAge = (age) => {
    
    if(age<18) {
        alert("Sorry, you are too young to drive this car. Powering off")
    } else if (age===18) {
        alert("Congratulations on your first year of driving. Enjoy the ride!")
    } else {
        alert("You are old enough to drive, Powering On. Enjoy the ride!")
    }
}

// let age = checkDriverAge(Number(prompt("What is your age?")));


// Exercise 2 : What’s In My Wallet ?
//      1. Given a total due and an array representing the amount of change in your pocket, 
//      determine whether or not you are able to pay for the item.
//      Change will always be represented in the following order: quarters, dimes, nickels, pennies.

const changeEnough = (coins, price) => {
    let coinsValue = [coins[0]*.25, coins[1]*.10, coins[2]*.05, coins[3]*.01];
    let sumOfCoins = coinsValue.reduce((a,b)=>a+b)
    if(sumOfCoins>=price){
        return true;
    }
    return false;
}

// console.log(changeEnough([0, 0, 20, 5], 1.05))
// console.log(changeEnough([2, 100, 0, 0], 14.11))



// Exercise 3: Find The Multiples Of 23
// Write a js function that console.log 
// the multiples of 23 less than 500 
// and at the end return the sum of all of them.


let array = [500, 75, 0, 23, 46, 69, 92, 115, 138, 161, 184, 207, 230, 253, 276, 299, 322, 345, 368, 391, 414, 437, 460, 483];

const sumMultiples = (array) => {
    let multiplesOf23 = array.filter(element => element%23===0 && element<500);
    return multiplesOf23.reduce((a,b)=>a+b);
}

// console.log(sumMultiples(array));


// Exercise 4 : Amazon Shopping
// let amazonBasket = {
//     glasses: 1,
//     books: 2,
//     floss: 100
// }
// Create a function called checkBasket().
// It should:
// ask the user for the item he wants
// and let him know if it’s in the basket or not
// Hint: Use the in keyword inside the conditional


let amazonBasket = {
        glasses: 1,
        books: 2,
        floss: 100
    }

const checkBasket = (amazonBasket, item) => {
    console.log(`${(item in amazonBasket) ? 'yes' : 'no'}`)
}

// checkBasket(amazonBasket, 'glasses');
// checkBasket(amazonBasket, 'couch');
// checkBasket(amazonBasket, 'floss');
// checkBasket(amazonBasket, 'orange');


// Exercise 5 : Shopping List
// 1. Create an array called shoppingList with the values “banana”, “orange”, and “apple”.
// 2. Copy these two above objects into your js file
// 3. Create a function called myBill() that takes no argument.
//     Depending on the list of items that you have in your array shoppingList and the prices listed in the prices object,
//     return the price spent on shopping.
// 4. Call the function myBill()
// Bonus: In the function above, only add the price if the item is in stock (use the stock object).
// 5. If the item is in stock, decrease the item’s stock by 1


let stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

let prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 

let shoppingList = ['banana', 'orange', 'apple'];
    


const myBill = () => {
    let sum=0;
    for(let item of shoppingList){
        if(stock[item]!=0){
            sum = sum + prices[item];
            stock[item]--;
        }
    }
    return sum;
}

// console.log(stock)
// console.log(myBill());
// console.log(stock)


// Exercise 6 : Tips
// John and his family went on a holiday and went to 3 different restaurants.
// To tip the waiter a fair amount, John created a simple tip calculator (as a function).

// He likes to tip:
// 20% of the bill when the bill is less than $50,
// 15% when the bill is between $50 and $200,
// and 10% if the bill is more than $200.

// 1. Ask John for the amount of the 3 bills. He has to enter a list of bills, each one separated by a comma.
// 2. Create the program explained above.
// 3. In the end, John would like to have 2 arrays:
// Containing all three tips (one for each bill).
// Containing all three final paid amounts (bill + tip).
// (NOTE: To calculate 20% of a value, simply multiply it with 20/100 = 0.2)


const tipMaker = (billArray) => {
    let tips = []
    for(bill of billArray){
        if(bill<50){
            tips.push(bill*.2);
        } else if(bill>=50 && bill<=200){
            tips.push(bill*.15);
        } else {
            tips.push(bill*.1);
        }
    }
// Now the tips array contains the quantities of all three tips

    let totalBill = [];
    let i=0;
    for(bill of billArray){
        totalBill.push(bill+tips[i]);
        i++;
    }
// Now the totalBill array contains all three final paid amounts (bill + tip)
    
// Now we'll add both arrays to allArrays and return that array
    let allArrays = [[tips], [totalBill]];
    return allArrays; 
}



// console.log(tipMaker([49, 50, 300]))


// I decided to skip exercise #7

