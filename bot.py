from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('bot.html')

@app.route('/get-response', methods=['POST'])
def get_response():
    user_message = request.json.get('message')
    # Here you can implement your logic to generate a response based on the user_message
    bot_response = "Suck my dick nigga!"
    return jsonify(response=bot_response)

if __name__ == '__main__':
    app.run(debug=True)