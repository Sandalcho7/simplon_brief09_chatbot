// Ouverture et fermeture du chat

document.addEventListener("DOMContentLoaded", function() {
    // Get references to the chat header, body, input, and window
    const chatWindow = document.querySelector('.chatbot-window');
    const chatHeader = document.querySelector('.chatbot-header');

    // Add click event listener to the chat header button
    chatHeader.addEventListener('click', function() {
        // Toggle the 'open' class on the chat window
        chatWindow.classList.toggle('open-chat');
    });
});


// Gestion des messages

document.addEventListener("DOMContentLoaded", function() {
    // Get references to the input field, send button, and chat body wrapper
    const inputFieldEl = document.querySelector('.chatbot-input input');
    const sendButtonEl = document.querySelector('.chatbot-input .chatbot-send-btn');
    const chatBodyWrapperEl = document.querySelector('.message-container-wrapper');

    // Add an event listener to the send button
    sendButtonEl.addEventListener('click', () => {
        // Get the value of the input field
        const message = inputFieldEl.value;
        
        // Check if the input field is not empty
        if (message.trim() !== '') {
            // Create a new message container element for user message
            const userMessageContainerEl = document.createElement('div');
            userMessageContainerEl.classList.add('message-container');
            
            // Create a new user element for user message
            const userElementEl = document.createElement('div');
            userElementEl.textContent = 'You';
            userElementEl.classList.add('user');
            
            // Create a new message element for user message
            const userMessageElement = document.createElement('div');
            userMessageElement.textContent = message;
            userMessageElement.classList.add('message');

            // Append user and message elements to the user message container
            userMessageContainerEl.appendChild(userElementEl);
            userMessageContainerEl.appendChild(userMessageElement);
            
            // Append the user message container to the message container wrapper
            chatBodyWrapperEl.appendChild(userMessageContainerEl);

            // Scroll chat body wrapper to the bottom to show the latest message
            chatBodyWrapperEl.scrollTop = chatBodyWrapperEl.scrollHeight;

        
            // Create a new message container element for bot response
            const botMessageContainerEl = document.createElement('div');
            botMessageContainerEl.classList.add('bot-message-container');

            // Create a new bot element for bot response
            const botElementEl = document.createElement('div');
            botElementEl.textContent = 'Gerd Müller';
            botElementEl.classList.add('bot');

            // Create a new message element for bot response
            const botMessageElementEl = document.createElement('div');
            fetch('http://localhost:8000/' + message, {method: 'POST'})
                .then(response => {
                    return response.json();
                })
                .then(data => {
                    botMessageElementEl.innerText = data;
                    // Scroll chat body wrapper to the bottom to show the latest message
                    chatBodyWrapperEl.scrollTop = chatBodyWrapperEl.scrollHeight;
                });
            botMessageElementEl.classList.add('bot-message');

            // Append user and message elements to the bot message container
            botMessageContainerEl.appendChild(botElementEl);
            botMessageContainerEl.appendChild(botMessageElementEl);

            // Append the bot message container to the message container wrapper
            chatBodyWrapperEl.appendChild(botMessageContainerEl);
            
            // Clear the input field after sending the message
            inputFieldEl.value = '';
        }
    });

    // Optionally, you may also want to send the message when pressing Enter
    inputFieldEl.addEventListener('keydown', (event) => {
        if (event.key === 'Enter') {
            // Prevent the default behavior of the Enter key (submitting the form)
            event.preventDefault();
            
            // Trigger a click on the send button
            sendButtonEl.click();
        }
    });
});