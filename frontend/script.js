async function analyzeResume() {

    const resumeText =
        document.getElementById("resumeText").value;

    const response = await fetch(
        "http://127.0.0.1:8083/analyze-resume",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                resume_text: resumeText
            })
        }
    );

    const data = await response.json();

    let skillsHTML = "";

    data.skills_found.forEach(skill => {
        skillsHTML += `<li>${skill}</li>`;
    });

    let suggestionsHTML = "";

    data.suggestions.forEach(item => {
        suggestionsHTML += `<li>${item}</li>`;
    });

    document.getElementById("result").innerHTML = `
        <div class="card">

            <h2>Resume Analysis</h2>

            <p><strong>Score:</strong> ${data.score}</p>

            <p><strong>Level:</strong> ${data.level}</p>

            <h3>Skills Found</h3>

            <ul>
                ${skillsHTML}
            </ul>

            <h3>Suggestions</h3>

            <ul>
                ${suggestionsHTML}
            </ul>

        </div>
    `;
}


async function loadAnalyses() {

    const response = await fetch(
        "http://127.0.0.1:8083/analyses"
    );

    const data = await response.json();

    let html = "<h2>Stored Analyses</h2>";

    data.forEach(item => {

        let skills = "";

        item.skills_found.forEach(skill => {
            skills += `<li>${skill}</li>`;
        });

        let suggestions = "";

        item.suggestions.forEach(suggestion => {
            suggestions += `<li>${suggestion}</li>`;
        });

        html += `
            <div class="card">

                <p><strong>Score:</strong> ${item.score}</p>

                <p><strong>Level:</strong> ${item.level}</p>

                <h4>Skills</h4>

                <ul>
                    ${skills}
                </ul>

                <h4>Suggestions</h4>

                <ul>
                    ${suggestions}
                </ul>

            </div>
        `;
    });

    document.getElementById("history").innerHTML = html;
}