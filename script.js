async function calculate() {
    const file = document.getElementById("fileInput").files[0];
    const weights = document.getElementById("weights").value;
    const impacts = document.getElementById("impacts").value;

    const resultDiv = document.getElementById("result");
    resultDiv.innerHTML = "Calculating...";

    const formData = new FormData();
    formData.append("file", file);
    formData.append("weights", weights);
    formData.append("impacts", impacts);

    try {
        const response = await fetch("http://127.0.0.1:5000/calculate", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        let html = "<h3>Result</h3><table border='1'><tr><th>Option</th><th>Score</th><th>Rank</th></tr>";
        data.results.forEach(r => {
            html += `<tr><td>${r.option}</td><td>${r.score}</td><td>${r.rank}</td></tr>`;
        });
        html += "</table>";

        resultDiv.innerHTML = html;

    } catch (err) {
        resultDiv.innerHTML = "Backend not connected (this is OK for demo)";
    }
}

