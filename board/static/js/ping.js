$(document).ready(() => {
    function ping(times)
    {
        $.ajax({
            url: "http://www.hulstjes.nl/api/connection/",
            type: "get",
            succes: function () {

            },
        });
    };

}