/*
function eventListenersOnFire() {
    let raceSelector = document.querySelector('.race-selector');
    let mainClassSelector = document.querySelector('.main-class-selector');
    let subClassSelector = document.querySelector('.sub-class-selector');
    let finalClassSelector = document.querySelector('.final-class-selector');
    let listOfClassSelectors = [raceSelector, mainClassSelector, subClassSelector, finalClassSelector];
    for (let selector of listOfClassSelectors) {
        selector.addEventListener('change', makeApiCall)
    }
}


async function makeApiCall(event) {
    const response = await fetch('/selector-data/' + event.target.value);
    const classJsonData = await response.json();
    changeSelectorsAndAttributes(classJsonData);
}
*/

let startGameButton = document.getElementById("startGameButton")
startGameButton.addEventListener("click", makeApiCall);

async function makeApiCall(event) {
    const response = await fetch('/game-data' + event.target.value)
    const jsonData = await response.json()
    console.log(jsonData) 
};


