setInterval(function(){
    $.get('/api/notification/badge/funsionariu/postu/',function(data) {
        document.getElementById("notifbadgefunpost").innerHTML = data.value;
    });
}, 3000);
console.log(data.value)