
// fonction de jQuery qui s'execute une fois le DOM ready
$(document).ready(function() {

    var csrf_token = $("input[name='csrfmiddlewaretoken']").val()

    // GET Ajax demo
    $(".get_button").click(function() {
        $.ajax({
            url: "/account/ajax/",
            type: "get",
            data: {
                button_text: $(this).text()
            },
            success: function(response) {
                $(".get_button").text(response.seconds)
                $("#seconds").append("<li>" + response.seconds + "</li>")
            }
        })
    })

    // POST Ajax demo [!] need to add csrf_token in ajax.html template
    $("#seconds").on("click", "li", function() {
        $.ajax({
            url: "/account/ajax/",
            type: "post",
            data: {
                text: $(this).text(),
                csrfmiddlewaretoken: csrf_token,
            },
            success: function(response) {
                $("#right").append("<li>" + response.data + "</li>")
            }
        })
    })
})