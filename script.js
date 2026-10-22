function switchTab(tab) {
    console.log("Switching tab to:", tab);
}

function appendLog(message, type = "info") {
    const consoleDiv = document.getElementById('logConsole');
    const timeStr = new Date().toLocaleTimeString();
    const div = document.createElement('div');
    div.className = type === "success" ? "text-emerald-400" : "text-cyan-400";
    div.textContent = `[${timeStr}] ${message}`;
    consoleDiv.appendChild(div);
    consoleDiv.scrollTop = consoleDiv.scrollHeight;
}

function triggerLambdaSimulation() {
    appendLog("Invoking AWS Lambda container handler (app.lambda_handler)...", "info");
    setTimeout(() => {
        appendLog('{"statusCode": 200, "body": "Successfully synchronized CME & GST events."}', "success");
    }, 1500);
}
