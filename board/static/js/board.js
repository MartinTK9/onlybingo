$(document).ready(function() {
    var seconds=$('#seconds').val();
    if (localStorage.getItem("host") == "true") {
        drawball()
    }
    else {
        getball()
    }


    //Needs to run on non-host in board view
    function getball(){
        var ball=0;
        $.get("http://www.hulstjes.nl/api/drawn/" + $("#pk").val(),function(data) {
                ball = Object.values(data)[1]
                document.getElementById('ball').innerHTML = ball
                console.log($('#ball').innerHTML);
        })
        setInterval(function(){
           $.get("http://www.hulstjes.nl/api/drawn/" + $("#pk").val(),function(){
               ball = Object.values(data)[1]
               document.getElementById('ball').innerHTML = ball
               console.log($('#ball').innerHTML);
           })
        },seconds*500)
    }
    //Needs to run on host browser in board view
    function drawball(){
        var url = "http://www.hulstjes.nl/api/draw/" + $("#pk").val();
        var ball = 0;
        setInterval(function(){
            $.get(url, function (data) {
                ball = Object.values(data)[1]
                document.getElementById('ball').innerHTML = ball
                console.log($('#ball').innerHTML);
            })

        },seconds*1000)
    }
});