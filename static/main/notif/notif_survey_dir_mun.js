setInterval(function(){
    $.get('/api/notification/survey/dir/mun',function(data) {
        document.getElementById("notifsurveydirmun").innerHTML = data.value;
    });
}, 5000);
console.log(data.value)