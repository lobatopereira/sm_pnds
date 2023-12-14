setInterval(function(){
    $.get('/api/notification/badge-rejected/',function(data) {
        document.getElementById("notifbadgeReject").innerHTML = data.value;
    });
}, 1);
console.log(data.value)