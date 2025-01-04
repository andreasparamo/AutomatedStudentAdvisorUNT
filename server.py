from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/bot')
def bot():
    return "Bot route"

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8000)
    