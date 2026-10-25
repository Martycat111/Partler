function hide_settings() {
    document.getElementById("settings")
        .style.display = "none";
}
function show_settings() {
    /* Access settings div by id and change 
    the display property to inline, to show the element*/
    document.getElementById("demo").innerText = "Sample text";
    document.getElementById("settings").style.display = "inline";
}
