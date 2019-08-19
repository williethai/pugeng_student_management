function send(object)
{
    var urlvariable;
    var csrftoken = getCookie('csrftoken');
    urlvariable = object.value + "/";
    var ItemJSON;
    if (object.checked == true)
        ItemJSON = "{\"present_check\": true}";
    else 
        ItemJSON = "{\"present_check\": false}";
    console.log('---------------')
    
    console.log(object)
    URL = "http://10.99.158.202:8000/api/student_class_schedule/update_student_attendance/" + urlvariable;  //Your URL

    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = callbackFunction(xmlhttp);
    xmlhttp.open("PUT", URL, false);
    xmlhttp.setRequestHeader("Content-Type", "application/json");
    xmlhttp.setRequestHeader("X-CSRFToken", csrftoken);
    //xmlhttp.setRequestHeader('Authorization', 'Basic ' + window.btoa('apiusername:apiuserpassword')); //in prod, you should encrypt user name and password and provide encrypted keys here instead 
    xmlhttp.onreadystatechange = callbackFunction(xmlhttp);
    xmlhttp.send(ItemJSON);
}

function callbackFunction(xmlhttp) 
{
    //alert(xmlhttp.responseXML);
}
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}