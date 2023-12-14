setInterval(function(){
    $.get('/api/notification/implementation/dir/mun',function(data) {
        document.getElementById("notifimplementasaundirmun").innerHTML = data.value;
    });
}, 5000);
console.log(data.value)