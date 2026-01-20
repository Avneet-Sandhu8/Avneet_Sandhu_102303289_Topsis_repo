async function calculate() {
    const file = document.getElementById("fileInput").files[0];
    const weights = document.getElementById("weights").value;
    const impacts = document.getElementById("impacts").value;

    if (!file) {
        alert("Please upload CSV file");
        return;
    }

    const formData = new FormData();
    formData.append("file", file);
    formData.append("weights", weights);
    formData.append("impacts", impacts);

    const response = await fetch("http://127.0.0.1:5000/calculate", {
        method: "POST",
        body: formData
    });

    const data = await response.json();
    document.getElementById("result").innerText =
        JSON.stringify(data, null, 2);
}
