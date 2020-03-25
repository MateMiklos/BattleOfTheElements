const startGameButton = document.getElementById("startGameButton")
const midBox = document.querySelector(".mid-box")

let GAME

startGameButton.addEventListener("click", makeApiCall);


/*
inputButton.addEventListener("click", function () {
  console.log("The button is cliccced")
  postData('/postmethod', { answer: 42 })
  .then((data) => {
     console.log(data); // JSON data parsed by `response.json()` call
  });
});


async function postData(url, data) {
    // Default options are marked with *
    const response = await fetch(url, {
      method: 'POST', // *GET, POST, PUT, DELETE, etc.
      mode: 'cors', // no-cors, *cors, same-origin
      cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
      credentials: 'same-origin', // include, *same-origin, omit
      headers: {
        'Content-Type': 'application/json'
        // 'Content-Type': 'application/x-www-form-urlencoded',
      },
      redirect: 'follow', // manual, *follow, error
      referrerPolicy: 'no-referrer', // no-referrer, *client
      body: JSON.stringify(data) // body data type must match "Content-Type" header
    });
    return await response.json(); // parses JSON response into native JavaScript objects
}
*/


async function makeApiCall(event) {
	const response = await fetch('/game-data' + event.target.value)
	const jsonData = await response.json()
	GAME = jsonData.game
	startTurn()
};


function createCard(card) {
	let name = card.name
	let manacost = card.manacost
	let abilityDescription = card.abilityDescription
	let elementType = card.elementType
	let spellType = card.spellType
	midBox.innerHTML +=
		`<div class="card">
		  <p class="cardTitleRow">${name} (${manacost})</p>
		  <div class="cardImg"></div>
		  <p class="cardTypeRow">${elementType} - ${spellType}</p>
		  <p class="cardDescription">${abilityDescription}</p>
		  <button class="castButton">cast</button>
		</div>`
}


function startTurn() {
	console.log(GAME.player1.deck)
	GAME = dealBoard1(GAME)
	console.log(GAME.player1.deck.board)
	GAME.player1.deck.board.forEach(element => {
		createCard(element)
	});
}


function dealBoard1() {
	for (let i = 0; i < GAME.player1.deck.boardSize; i++) {
    	try {
    		randIndex = randint(0, GAME.player1.deck.cards.length - 1)
    		GAME.player1.deck.board.push(GAME.player1.deck.cards[randIndex])
    		GAME.player1.deck.cards.splice(randIndex, 1)
    	}
    catch {
      	for (card in deck.cards) {
    		deck.board.push(card)
    		delete deck.cards[deck.cards.indexOf(card)]
      		}
    	}
  	}
}


function randint(min, max) {
  	return Math.floor(Math.random() * (max - min)) + min
}
