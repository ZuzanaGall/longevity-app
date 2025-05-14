from flask import Flask, render_template, request
import openai

app = Flask(__name__)
openai.api_key = "TU_VLOŽ_API_KĽÚČ"  # napr. "sk-..."

@app.route("/", methods=["GET", "POST"])
def index():
    advice = None
    if request.method == "POST":
        sleep = request.form["sleep"]
        exercise = request.form["exercise"]
        diet = request.form["diet"]
        stress = request.form["stress"]
        other = request.form["other"]

        prompt = f"""
Ty si AI longevity coach. Používateľ má tieto návyky:
- Spí: {sleep}
- Pohyb: {exercise}
- Strava: {diet}
- Stres: {stress}
- Iné návyky: {other}

Navrhni 3 konkrétne kroky, ktoré môže spraviť už dnes, aby znížil svoj biologický vek. Buď praktický a vecný.
"""

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert AI longevity coach."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )

        advice = response['choices'][0]['message']['content']

    return render_template("index.html", advice=advice)

if __name__ == "__main__":
    app.run(debug=True)
