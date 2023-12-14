setInterval(function(){
    $.get('/api/notification/monitoring-post-implementasaun-rejeitadu/',function(data) {
        document.getElementById("notifmonitoringpostimplementasaunrejeita").innerHTML = data.value;
    });
}, 5000);
console.log(data.value)