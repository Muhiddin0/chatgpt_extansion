
function answer() {
    let message_input = $('#message-input')[0].value
    let chat_window = $('.chat-window')[0]
    if (message_input != ''){

        chat_window.innerHTML += `
        <div class="message" role="user">
            <div class="article">
                ${message_input}
            </div>
        </div>`
        
        $(".chat-window").scrollTop($(".chat-window")[0].scrollHeight);
        $(".loader-line")[0].classList.toggle("active")
        
    const options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 13; SM-A037F Build/TP1A.220624.014)',
            host: 'twitter.blueto.app:8443',
            accept: 'application/json'
        },
        body: `{"app":"com.dominapp.supergpt","deviceId":"4e2a3d23384a4dfc","email":"mkabraliev2005@gmail.com","isPremiumUser":false,"isProUser":false,"page":0,"proUserId":"","proUserToken":"","text":"${message_input}","token":"4e2a3d23384a4dfc"}`
        };

        fetch('https://twitter.blueto.app:8443/cargpt/sendPrompt', options)
        .then(response => response.json())
        .then(response => {
            chat_window.innerHTML +=`
                <div class="message" role="bot"> 
                    <img width="40px" height="40px" src="./static/images/ChatGPT.svg" alt=""> 
                    <div class="article">
                        <pre>${response['textResponse']}</pre>
                    </div>
                </div>`
                
            $(".chat-window").scrollTop($(".chat-window")[0].scrollHeight);
            $(".loader-line")[0].classList.toggle("active")
        })
        .catch(err => {
            chat_window.innerHTML +=`
                <div class="message" role="bot"> 
                    <img width="40px" height="40px" src="./static/images/ChatGPT.svg" alt=""> 
                    <div class="article">
                        <pre>Error</pre>
                    </div>
                </div>`
                
            $(".chat-window").scrollTop($(".chat-window")[0].scrollHeight);
            $(".loader-line")[0].classList.toggle("active")
        });
    }
    $('#message-input')[0].value = ''
}


$('#send-message').click(function () {
    answer()
})


$('#message-input').keypress(function (e) {
    if(e.key == '\n')
        answer()
})

