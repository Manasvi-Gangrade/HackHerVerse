const voiceCommandBtn = document.getElementById('voiceCommandBtn');
const outputDiv = document.getElementById('output');

voiceCommandBtn.addEventListener('click', async () => {
    const response = await fetch('/voice_command', { method: 'POST' });
    const data = await response.json();
    outputDiv.textContent = `Received Command: ${data.command}`;
});
