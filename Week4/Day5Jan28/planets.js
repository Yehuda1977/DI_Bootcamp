// This webpage is just a blank universe, and you’ll fill it with planets 
// and moons in this challenge.
// You only have to work with a JS file

// 1. Create an array of planets of the solar system
// 2. For each planet, in the array, create a div using createElement. 
// This div should have a class named ‘planet’.
// 3. Each planet should have a different background color. 
// (Hint: add a new class to each planet)
// 4. Finally append each div to the body.
// 5. Bonus Do the same process for moons. 
// Be careful, each planet has a certain amount of moons; How should you display them ?

let solarSystem = [
    { 
        name: 'Mercury',
        moons: 0,
        color: 'orange'
    },
    { 
        name:'Venus',
        moons: 0,
        color: 'grey'
 
    },
    { 
        name: 'Earth',
        moons: 1,
        color: 'blue'
    },
    { 
        name: 'Mars',
        moons: 2,
        color: 'red'
 
    },
    { 
        name: 'Jupiter',
        moons: 79,
        color: 'orange'
    },
    { 
        name: 'Saturn',
        moons: 62,
        color: 'pink'
    },
    { 
        name: 'Uranus',
        moons: 27,
        color: 'silver'
    },
    { 
        name: 'Neptune',
        moons: 14,
        color: 'turquise'
    }
];


for(planet of solarSystem){
    let planetDiv = document.createElement('div');
    planetDiv.setAttribute('class', 'planet');
    planetDiv.setAttribute('style', `background-color:${planet.color}`);
    planetDiv.innerHTML = planet.name; 
    document.body.appendChild(planetDiv)
    console.log(planetDiv)
}

