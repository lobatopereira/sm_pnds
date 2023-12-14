setInterval(function(){
    $.get('/api/notification/implementasaun/rejeitadu/funsionariu/postu/',function(data) {
        document.getElementById("notifimplementasaunrejeitadufunpost").innerHTML = data.value;
    });
}, 5000);
console.log(data.value)