$(document).ready(function() {
    var seconds=$('#seconds').val();
    //Needs to run on non-host in room view
    function gamestarted() {
        setInterval(function(){
            $.get("http://www.hulstjes.nl/api/drawn/" + $("#pk").val(),function(){

            }).fail(function(){
                console.log("game hasnt started yet")
            }).done(function(){
                window.clearInterval();
                window.location.replace("http://www.hulstjes.nl/" + $('#pk').val() + "/" + $('#player').val());
            })
        },1000);
    };
    //Needs to run on non-host in board view
    function getball(){
        var ball=0;
        $.get("http://www.hulstjes.nl/api/drawn/" + $("#pk").val(),function(data) {

            $('#ball').innerText = Object.values(data)[1];
            ball=Object.values(data)[1]
        })
        setInterval(function(){
           $.get("http://www.hulstjes.nl/api/drawn/" + $("#pk").val(),function(){
               var newball=Object.values(data)[1];
               $('#ball').innerText = newball
           })
        },seconds*500)
    }
    //Needs to run on host browser in board view
    function drawball(){
        var url = "http://www.hulstjes.nl/api/draw/" + $("#pk").val();

        setInterval(function(){
            $.get(url, function (data) {
                $('#ball').innerText = Object.values(data)[1]
            })
        },seconds*10000)
    }
});