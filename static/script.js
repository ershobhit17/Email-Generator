let generatedPitches = null;
let currentTab = 'professional';

function generatePitches() {
    const name = document.getElementById('name').value.trim();
    const skills = document.getElementById('skills').value.trim();
    const company = document.getElementById('company').value.trim();
    const role = document.getElementById('role').value.trim();
    const project = document.getElementById('project').value.trim() || "Full-Stack Web App";

    if (!name || !skills || !company || !role) {
        alert("Please fill all necessary developer parameters! 🛠️");
        return;
    }

    const btn = document.getElementById('submit-btn');
    btn.innerText = "PROCESSING SYSTEM LAYERS...";
    btn.disabled = true;

    fetch('/generate_pitch', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            name: name,
            skills: skills,
            company: company,
            role: role,
            project: project
        })
    })
    .then(res => res.json())
    .then(data => {
        btn.innerText = "GENERATE AI PITCHES";
        btn.disabled = false;

        if(data.success) {
            generatedPitches = data.pitches;
            document.getElementById('copy-btn').disabled = false;
            switchTab(currentTab); // Load active state context
        } else {
            alert("API logic failed: " + data.error);
        }
    })
    .catch(err => {
        btn.innerText = "GENERATE AI PITCHES";
        btn.disabled = false;
        alert("Server Connectivity Error.");
    });
}

function switchTab(tabName) {
    currentTab = tabName;
    
    // UI active buttons toggle
    const buttons = document.querySelectorAll('.tab-btn');
    buttons.forEach(btn => btn.classList.remove('active'));
    
    // Add active class correctly based on click configuration
    const targetIdx = ['professional', 'builder', 'honest'].indexOf(tabName);
    if(targetIdx !== -1) buttons[targetIdx].classList.add('active');

    if (!generatedPitches) return;

    // Render logic updates
    document.getElementById('display-subject').innerText = generatedPitches[tabName].subject;
    document.getElementById('display-body').innerHTML = generatedPitches[tabName].body.replace(/\n/g, "<br>");
}

function copyToClipboard() {
    if (!generatedPitches) return;

    const subject = generatedPitches[currentTab].subject;
    const body = generatedPitches[currentTab].body;
    const fullText = `Subject: ${subject}\n\n${body}`;

    navigator.clipboard.writeText(fullText).then(() => {
        const copyBtn = document.getElementById('copy-btn');
        copyBtn.innerText = "Copied Successfully! ✅";
        copyBtn.style.background = "#10b981";
        
        setTimeout(() => {
            copyBtn.innerText = "Copy Content 📋";
            copyBtn.style.background = "#6366f1";
        }, 2000);
    }).catch(err => {
        alert("Failed to copy text matrix.");
    });
}
