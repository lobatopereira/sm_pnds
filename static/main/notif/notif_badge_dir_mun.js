setInterval(function(){
    $.get('/api/notification/badge/dir/mun/',function(data) {
        document.getElementById("notifbadgedirmun").innerHTML = data.value;
    });
}, 3000);
console.log(data.value)