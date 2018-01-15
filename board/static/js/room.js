

$(document).ready(function() {
    var url = "http://www.hulstjes.nl/api/draw/" + $("#pk").val();

    $('#startgame').on('click',function() {
        $.get(url, function (data) {

        }).fail(function () {
            alert("Error creating room");
        }).done(function () {
            localStorage.setItem("host",true)
            window.location.replace("http://www.hulstjes.nl/" + $('#pk').val() + "/" + $('#player').val());
        });
    });

});
