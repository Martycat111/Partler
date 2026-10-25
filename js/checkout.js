
function checkout() {
    console.log("tbd")

    // POST request using fetch()
    fetch(window.location.href, {
    
        // Adding method type
        method: "POST",
    
        // Adding body or contents to send
        body: JSON.stringify({
            title: "foo",
            body: "bar",
            userId: 1
        }),

        // Adding headers to the request
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    })

    // Converting to JSON
    .then(response => response.json())
    
    // Displaying results to console
    .then(json => console.log(json));

}
function update_running_total() {
    // Partial Source - https://stackoverflow.com/a/5338729
    // Posted by erickb, modified by community. See post 'Timeline' for change history
    // Retrieved 2026-10-24, License - CC BY-SA 4.0

    var elements = document.getElementsByClassName("numberInput");
    var number = 0;

    // im dumb as bricks, had number[i] instead of elements[i]

    for(var i = 0; i < elements.length; i++) {
        number += elements[i].valueAsNumber;
    }
    var runningtotal = document.getElementsByClassName("total")
    runningtotal[0].innerText = `Running total: ${number}`
}