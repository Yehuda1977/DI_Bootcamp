let table = document.getElementById('sampleTable');

console.log(table)


const insert_Row = () => {
    let newRow = document.createElement('tr')

    table.appendChild(newRow).innerHTML = "<td>hi</td><td>hi</td>"
 
}