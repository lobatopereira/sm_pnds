setInterval(function(){
    $.get('/api/notification/monitoring-implementasaun-rejeitadu/',function(data) {
        document.getElementById("notifmonitoringimplementasaunrejeita").innerHTML = data.value;
    });
}, 5000);
console.log(data.value)