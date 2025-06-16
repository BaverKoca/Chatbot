const chatBox = document.getElementById('chat-box');
const chatForm = document.getElementById('chat-form');
const userInput = document.getElementById('user-input');

function appendMessage(sender, text, question = null) {
    const msgDiv = document.createElement('div');
    msgDiv.className = `message ${sender}`;
    msgDiv.textContent = text;
    chatBox.appendChild(msgDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
    // Add feedback UI for bot answers
    if (sender === 'bot' && question) {
        const feedbackDiv = document.createElement('div');
        feedbackDiv.className = 'feedback-ui';
        feedbackDiv.innerHTML = `
            <button class="like-btn">👍</button>
            <button class="dislike-btn">👎</button>
        `;
        msgDiv.appendChild(feedbackDiv);
        feedbackDiv.querySelector('.like-btn').onclick = () => sendFeedback(question, text, 1, feedbackDiv);
        feedbackDiv.querySelector('.dislike-btn').onclick = () => sendFeedback(question, text, 0, feedbackDiv);
    }
}

async function sendFeedback(question, answer, rating, feedbackDiv) {
    try {
        await fetch('/feedback', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ question, answer, rating })
        });
        feedbackDiv.innerHTML = '<span style="color:#388e3c;">Thank you for your feedback!</span>';
    } catch {
        feedbackDiv.innerHTML = '<span style="color:#d32f2f;">Feedback failed.</span>';
    }
}

chatForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const question = userInput.value.trim();
    if (!question) return;
    appendMessage('user', question);
    userInput.value = '';
    appendMessage('bot', '...', question);
    try {
        const res = await fetch('/ask', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ question })
        });
        const data = await res.json();
        if (!res.ok) throw new Error(data.detail || 'Error');
        chatBox.lastChild.textContent = data.answer;
        // Add feedback UI to the new bot message
        appendMessage('bot', data.answer, question);
        // Remove the previous '...' message
        chatBox.removeChild(chatBox.childNodes[chatBox.childNodes.length - 2]);
    } catch (err) {
        chatBox.lastChild.textContent = 'Error: Could not get response.';
    }
});
