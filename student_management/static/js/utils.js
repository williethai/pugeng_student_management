function onDlistInput(inp) {
    var val = inp.value;
    var opts = inp.list.childNodes;
    if(val === '') {
        inp.list.value = 0
        return
    }
    inp.list.value = -1
    for (var i = 0; i < opts.length; i++) {
        if (opts[i].value === val) {
            inp.list.value = opts[i].id
            break;
        }
    }
}