$(document).ready(() => {
    function ping(times)
    {
        var pk=$('#pk').innerHTML()
        $.ajax({
            url: "http://www.hulstjes.nl/api/connection/",
            type: "post",
            dataType: 'json',
            contentType: 'application/json',
            data: JSON.stringify({ "player": pk,}),
            processData: false,
            succes: function () {

            },
        });
    };
    function gamestart(){
        $.get("http://www.hulstjes.nl/api/draw/"+$.("#pk").innerHTML,function(data){
            alert(data)
        };)
    };
}