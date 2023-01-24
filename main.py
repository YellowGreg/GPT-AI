from flask import Flask, request, render_template
from youGPT import ask

app = Flask("app")

@app.route("/", methods=["GET", "POST"])
def _():
    if request.method == "POST":
        question = request.form.get("question")
        answer = ask(question)
        return render_template(
          "chat.html", 
          question=question,
          answer=answer["response"]
        )

    return render_template("chat.html", answer=None)


app.run(
  host="0.0.0.0", 
  port=80
)
