const chatBox = document.getElementById("chat-box");

const input = document.getElementById("message");

function addMessage(sender, text) {

    const div = document.createElement("div");

    div.className = `message ${sender}`;

    div.innerHTML = `
    <div class="bubble">
        ${text}
    </div>
    `;

    chatBox.appendChild(div);

    chatBox.scrollTop = chatBox.scrollHeight;

    return div;

}

async function sendMessage() {

    const message = input.value.trim();

    if (message === "") return;

    addMessage("user", message);

    input.value = "";

    const typing = addMessage("bot", "<span class='typing'>Ultra Mind AI is typing...</span>");

    try {

        const response = await fetch("http://127.0.0.1:8000/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message
            })

        });

        const data = await response.json();

        typing.innerHTML = `
        <div class="bubble">
            ${data.response}
        </div>
        `;

    }

    catch {

        typing.innerHTML = `
        <div class="bubble">
            Backend not running.
        </div>
        `;
    }

}