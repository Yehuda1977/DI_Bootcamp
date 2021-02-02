//<html>
//<body>
//  <div id="container">Users:</div>
//  <ul class="list">
//    <li>John</li>
//    <li>Pete</li>
//  </ul>
//  <ul class="list">
//    <li>David</li>
//    <li>Sarah</li>
//    <li>Dan</li>
//  </ul>
//</body>
//</html>
// 1. Change the name “Pete” to “Richard”
// 2. Change each first name of the <ul> by your name
// 3. Add at the end of each <ul>, a <li> that says “Hey students”
// 4. Delete the <li> Sarah
// 5. Bonus
//      Add a class “student_list” to both of the <ul>
//      Add the class “university” and “attendance” to the first <ul>

let list = document.getElementsByClassName('list')
let pete = list[0].lastElementChild;
console.log(pete.textContent);
pete.innerHTML = 'Richard'
console.log(pete.textContent);


newLi = document.createElement('li');
newLi.innerHTML = 'Hey students' 


for(l of list){
    l.firstElementChild.innerHTML = "Yehuda"
}

list[0].appendChild(newLi)
list[1].appendChild(newLi)
// for(l of list){
//     l.appendChild(newLi);
// }



