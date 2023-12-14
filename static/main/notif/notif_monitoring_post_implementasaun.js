setInterval(function(){
    $.get('/api/notification/monitoring-post-implementasaun/',function(data) {
        document.getElementById("notifMonitoringPOstImplementasaun").innerHTML = data.value;
    });
}, 5000);
console.log(data.value)