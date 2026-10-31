function addtype_popup() {
    //show the add type popup
    console.log("mr")
    var popup = document.getElementsByClassName("addtype-popup")[0];
    popup.style.display = "inline";
}


function checkin() {

    // initial json object
    const jsonObject = {};

    // add things to json

    // get elements for use
    var itemnames = document.getElementsByClassName("itemname");
    var itemcounts = document.getElementsByClassName("numberInput");
    var numitems = document.getElementsByClassName("itemholder").length; // had item instead of itemholder. spent 2 hours debugging this

    // initialize arrays to put info into
    var names = [];
    var counts = [];

    //loop and add items to array
    for(var i = 0; i < numitems; i++) {
        counts[i] = itemcounts[i].valueAsNumber;
        names[i] = itemnames[i].innerText;
    }

    //add arrays to the json
    jsonObject.names = names;
    jsonObject.counts = counts;

    // turn obj into json
    const jsonString = JSON.stringify(jsonObject);

    // POST request using fetch()
    fetch([window.location.href, "/add-count"].join(""), {
        // Adding method type
        method: "POST",
        // Adding body or contents to send
        body: jsonString,
        // Adding headers to the request
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    })
    // reload page
    location.reload();
}
function update_running_total() {
    var number = get_total_items()
    var runningtotal = document.getElementsByClassName("total")
    var checkoutbutton = document.getElementsByClassName("checkout-button")[0]
    runningtotal[0].innerText = `Running total: ${number}`
    if (number == 0) {
        console.log("disabling")
        checkoutbutton.disabled = true
    }
    else {
        console.log("enablimng")
        checkoutbutton.disabled = false
    }
}

function get_total_items() {
    var elements = document.getElementsByClassName("numberInput");
    var number = 0;

    // im dumb as bricks, had number[i] instead of elements[i]

    for(var i = 0; i < elements.length; i++) {
        number += elements[i].valueAsNumber;
    }
    return number
}