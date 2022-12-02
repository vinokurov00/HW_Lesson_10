from flask import Flask
import utils

app = Flask(__name__)

@app.route("/")
def index():
    candidates = utils.get_all()

    result = '<br>'

    for candidate in candidates:
        result += candidate["name"] + '<br>'
        result += candidate["position"] + '<br>'
        result += candidate["skills"] + '<br>'
        result += '<br>'
    return f"<pre> {result} </pre>"

@app.route("/candidates/<int:pk>")
def get_candidate(pk):
    candidate = utils.get_by_pk(pk)
    result = '<br>'

    result += candidate["name"] + '<br>'
    result += candidate["position"] + '<br>'
    result += candidate["skills"] + '<br>'

    return f"""
        <img src="{candidate['picture']}">
        <pre> {result} </pre>
    """


@app.route("/skills/<skill>")
def get_candidates_by_skills(skill):
    candidates = utils.get_by_skill(skill.lower())

    result = '<br>'

    for candidate in candidates:
        result += candidate["name"] + '<br>'
        result += candidate["position"] + '<br>'
        result += candidate["skills"] + '<br>'
        result += '<br>'
    return f"<pre> {result} </pre>"


if __name__ == '__main__':
    app.run(debug=True)