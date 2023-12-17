$(document).ready(function() {
    // var websocket = null

    // $('#btn-chat').click(function() {
    //     var message = $('#btn-input').val()
    //     websocket.send(message)
    //     $('#btn-input').val('')
    // })

    // $('#btn-input').keypress(function(e) {
    //     if (e.which == 13) {
    //         $('#btn-chat').click()
    //     }
    // })
    
    // $('#btn-connect').click(function() {
    //     openSocket()
    // })

    // function openSocket() {
    //     if (websocket == null) {
    //         websocket = new WebSocket('ws://' + window.location.host + '/chat/connect/')
    //         websocket.onopen = function() {
    //             console.log('Connected to a websocket')
    //         }
    //         websocket.onmessage = function(e) {
    //             var data = JSON.parse(e.data)
    //             var message = data['message']
    //             var handle = data['handle']
    //             var time = data['time']
    //             $('#chat').append('<li class="left clearfix"><span class="chat-img pull-left"><img src="http://placehold.it/50/55C1E7/fff&text=U" alt="User Avatar" class="img-circle" /></span><div class="chat-body clearfix"><div class="header"><strong class="primary-font">' + handle + '</strong><small class="pull-right text-muted"><span class="glyphicon glyphicon-time"></span>' + time + '</small></div><p>' + message + '</p></div></li>')
    //         }
    //         websocket.onclose = function() {
    //             console.log('Disconnected from a websocket')
    //             closeSocket()
    //         }
    //     }
    // }

    // function closeSocket() {
    //     websocket.close()
    //     websocket = null
    // }

})