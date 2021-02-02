// Exercise 1 : Change The Navbar
//  <div id="navBar">
//     <ul>
//         <li><a href="#">Profile</a></li>
//         <li><a href="#">Home</a></li>
//         <li><a href="#">My Friends</a></li>
//         <li><a href="#">Messenger</a></li>
//         <li><a href="#">My Pics</a></li>
//     </ul>
// </div>`
// 1. In the div above, change the value of the identity attribute (id) 
// from navBar to socialNetworkNavigation, using the setAttribute method.
// 2. We are going to add a new li to the ul.
//      1. First, create a new li tag (use the createElement method)
//      2. Then create a new text node with “Logout” as its specified text.
//      3. Append the text node to the newly created list node (li).
//      4. Finally, append this updated list node to the unordered list above, 
//      using the a(ppendChild method.
// 3. Bonus
//      Use the firstElementChild and the lastElementChild properties 
//      to retrieve the first and last li elements under the parent ul node. 
//      Display the text of each link.(Hint: textContent property).


let elem = document.getElementById('navBar');
console.log(elem)
// 1. In the div above, change the value of the identity attribute (id) 
// from navBar to socialNetworkNavigation, using the setAttribute method.
elem.setAttribute('id', 'socialNetworkNavigation')
console.log(elem)

// 2. We are going to add a new li to the ul.
//      1. First, create a new li tag (use the createElement method)
let newLi = document.createElement('li')
//      2. Then create a new text node with “Logout” as its specified text.
let newTextNode = document.createTextNode('Logout');
//      3. Append the text node to the newly created list node (li).
newLi.appendChild(newTextNode);
//      4. Finally, append this updated list node to the unordered list above, 
//      using the appendChild method.
let list = document.getElementsByTagName('ul');
console.log(list[0])
list[0].appendChild(newLi)

let firstLi = list[0].firstElementChild;
console.log(firstLi.textContent)

let lastLi = list[0].lastElementChild;
console.log(lastLi.textContent)
