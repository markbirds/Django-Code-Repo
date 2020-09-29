function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

function get_users(){
    $.get("{% url 'api:userList' %}", function(data, status){
        console.log(data);
    });
}

$(document).ready(function(){
    $("#add").click(function(){
        get_users();
        var url = "http://127.0.0.1:8000/api/create/";

        var name = $('#name').val().trim();
        var age = $('#age').val();
        var language = $('#language').val();
        var likes_programming = $('#likes_programming').prop("checked");
        fetch(url,{
            method: 'POST',
            headers: {
                'Content-type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({
                'name': name,
                'age': age,
                'language': language,
                'programmer': likes_programming
            })
        }).then(function(response){
            console.log(response);
        })
    });
});