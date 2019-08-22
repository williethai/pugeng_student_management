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
function classScheduleCreate(nid, class_to_schedule, study_time, token) {
        var postData = {}
        postData['nid'] = nid
        postData['class_to_schedule'] = class_to_schedule
        postData['study_time'] = study_time
        $.ajax({
            url: '/student/add_class_schedule',
            type: 'POST',
            headers:{'X-CSRFToken': token},
            data: postData,
            success:function (arg) {
                var dict = JSON.parse(arg);
                if(dict.status){
                
                }
            }
        })
    }
function classScheduleCreate(nid, class_to_schedule, start_date, graduation_date, token) {
        var postData = {}
        postData['nid'] = nid
        postData['class_to_schedule'] = class_to_schedule
        postData['start_date'] = start_date
        postData['graduation_date'] = graduation_date
        $.ajax({
            url: '/student/add_class_schedule',
            type: 'POST',
            headers:{'X-CSRFToken': token},
            data: postData,
            success:function (arg) {
                var dict = JSON.parse(arg);
                if(dict.status){
                
                }
            }
        })
    }