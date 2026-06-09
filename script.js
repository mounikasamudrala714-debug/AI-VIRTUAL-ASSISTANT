async function sendMessage() {

    const input =
        document.getElementById("userInput");

    const message =
        input.value.trim();

    if (message === "") {
        return;
    }

    const chatBox =
        document.getElementById("chatBox");

    const userDiv =
        document.createElement("div");

    userDiv.className =
        "user-message";

    userDiv.innerHTML =
        "You: " + message;

    chatBox.appendChild(userDiv);

    input.value = "";

    const response =
        await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type":
                    "application/json"
            },
            body: JSON.stringify({
                message: message
            })
        });

    const data =
        await response.json();

    const botDiv =
        document.createElement("div");

    botDiv.className =
        "bot-message";

    botDiv.innerHTML =
        "Bot: " + data.reply;

    chatBox.appendChild(botDiv);

    chatBox.scrollTop =
        chatBox.scrollHeight;
}

document.addEventListener(
    "DOMContentLoaded",
    function () {

        document
            .getElementById("userInput")
            .addEventListener(
                "keypress",
                function (event) {

                    if (event.key === "Enter") {
                        sendMessage();
                    }
                });
    });