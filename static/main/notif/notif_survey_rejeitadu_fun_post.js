setInterval(function(){
    $.get('/api/notification/survey/rejeitadu/funsionariu/postu/',function(data) {
        document.getElementById("notifsurveyrejeitadufunpost").innerHTML = data.value;
    });
}, 5000);
console.log(data.value)