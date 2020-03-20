let startGameButton = document.getElementById("startGameButton")
startGameButton.addEventListener("click", makeApiCall);

async function postData(url = '', data = {}) {
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
  

let inputButton = document.getElementById("inputButton")
inputButton.addEventListener("click", function () {
    console.log("The button is cliccced")
    /*
    $.ajax({
        type: "POST",
        url: "localhost:5000/postmethod",
        data: data,
        success: success,
        dataType: dataType
      });
      */
    postData('/postmethod', { answer: 42 })
    .then((data) => {
       console.log(data); // JSON data parsed by `response.json()` call
    });
});


async function makeApiCall(event) {
    const response = await fetch('/game-data' + event.target.value)
    const jsonData = await response.json()
    console.log(jsonData) 
};
