const API_PATH = 'http://localhost:8000/'

// Ouverture et fermeture du chat
document.addEventListener("DOMContentLoaded", function() {
    const chatWindow = document.querySelector('.chatbot-window');
    const chatHeader = document.querySelector('.chatbot-header');

    chatHeader.addEventListener('click', function() {
        chatWindow.classList.toggle('open-chat');
    });
});


// Gestion des messages
document.addEventListener("DOMContentLoaded", function() {
    const inputFieldEl = document.querySelector('.chatbot-input input');
    const sendButtonEl = document.querySelector('.chatbot-input .chatbot-send-btn');
    const chatBodyWrapperEl = document.querySelector('.message-container-wrapper');

    sendButtonEl.addEventListener('click', () => {
        const message = inputFieldEl.value;
        

        if (message.trim() !== '') {
            const userMessageContainerEl = document.createElement('div');
            userMessageContainerEl.classList.add('message-container');
            
            const userElementEl = document.createElement('div');
            userElementEl.textContent = 'You';
            userElementEl.classList.add('user');
            
            const userMessageElement = document.createElement('div');
            userMessageElement.textContent = message;
            userMessageElement.classList.add('message');

            userMessageContainerEl.appendChild(userElementEl);
            userMessageContainerEl.appendChild(userMessageElement);
            
            chatBodyWrapperEl.appendChild(userMessageContainerEl);

            chatBodyWrapperEl.scrollTop = chatBodyWrapperEl.scrollHeight;

            const botMessageContainerEl = document.createElement('div');
            botMessageContainerEl.classList.add('bot-message-container');

            const botElementEl = document.createElement('div');
            botElementEl.textContent = 'Gerd Müller';
            botElementEl.classList.add('bot');

            const botMessageElementEl = document.createElement('div');
            fetch(API_PATH + message, {method: 'POST'})
                .then(response => {
                    return response.json();
                })
                .then(data => {
                    botMessageElementEl.innerText = data;
                    chatBodyWrapperEl.scrollTop = chatBodyWrapperEl.scrollHeight;
                });
            botMessageElementEl.classList.add('bot-message');

            botMessageContainerEl.appendChild(botElementEl);
            botMessageContainerEl.appendChild(botMessageElementEl);
            chatBodyWrapperEl.appendChild(botMessageContainerEl);

            inputFieldEl.value = '';
        }
    });

    inputFieldEl.addEventListener('keydown', (event) => {
        if (event.key === 'Enter') {
            event.preventDefault();
            sendButtonEl.click();
        }
    });
});