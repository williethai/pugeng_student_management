function onInput() {
    var val = $(this).value;
    console.log(val)
    var opts = document.getElementById('dlist').childNodes;
    for (var i = 0; i < opts.length; i++) {
        if (opts[i].value === val) {
            // An item was selected from the list!
            // yourCallbackHere()
            alert(opts[i].value);
            break;
        }
    }
}