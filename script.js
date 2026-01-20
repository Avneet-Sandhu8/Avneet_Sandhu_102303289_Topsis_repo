document.getElementById("form").addEventListener("submit", async function(e) {
  e.preventDefault();

  const file = document.getElementById("file").files[0];
  const weights = document.getElementById("weights").value;
  const impacts = document.getElementById("impacts").value;
  const email = document.getElementById("sendEmail").checked
                  ? document.getElementById("email").value
                  : "";

  const formData = new FormData();
  formData.append("file", file);
  formData.append("weights", weights);
  formData.append("impacts", impacts);
  formData.append("email", email);

  document.getElementById("result").innerHTML = "Processing...";

  const res = await fetch("/calculate", {
    method: "POST",
    body: formData
  });

  const data = await res.json();

  let html = "<table><tr><th>Option</th><th>Score</th><th>Rank</th></tr>";

  data.results.forEach(r => {
    html += `<tr>
      <td>${r.option}</td>
      <td>${r.score.toFixed(6)}</td>
      <td>${r.rank}</td>
    </tr>`;
  });

  html += "</table>";

  document.getElementById("result").innerHTML = html;
});
