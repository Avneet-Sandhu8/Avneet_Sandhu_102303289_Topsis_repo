from flask import Flask, request, jsonify, render_template
import pandas as pd
from topsis.core import run_topsis
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    file = request.files["file"]
    weights = request.form["weights"]
    impacts = request.form["impacts"]
    email = request.form.get("email")

    input_file = "input.csv"
    output_file = "output.csv"
    file.save(input_file)

    run_topsis(input_file, weights, impacts, output_file)

    df = pd.read_csv(output_file)

    # send email if provided
    if email:
        send_email(email, output_file)

    result = []
    for _, row in df.iterrows():
        result.append({
            "option": row[0],
            "score": float(row["Topsis Score"]),
            "rank": int(row["Rank"])
        })

    return jsonify({"results": result})

def send_email(to_email, file_path):
    msg = EmailMessage()
    msg["Subject"] = "TOPSIS Result"
    msg["From"] = "avneetsandhu719@gmail.com"
    msg["To"] = to_email
    msg.set_content("Attached is your TOPSIS result CSV file.")

    with open(file_path, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="text",
            subtype="csv",
            filename="result.csv"
        )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login("avneetsandhu719@gmail.com", "gvohmpoyqludpoxx")
        smtp.send_message(msg)

if __name__ == "__main__":
    app.run(debug=True)

