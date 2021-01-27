let calcDisplay = document.getElementById('display');
let calculated = false;

const calculate = () => {
    calculated = true;
    calcDisplay.innerHTML = eval(calcDisplay.innerHTML)
    
}


const my_f = (digit) => {    
        if(calculated){
            calcDisplay.innerHTML = ''
            calculated = false;
        }
        calcDisplay.innerHTML += digit;
}

const reset  = () => {
    calcDisplay.innerHTML = ''
            calculated = false;
}

 









