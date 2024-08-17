from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

@app.route('/run_script', methods=['POST'])
def run_script():
    data = request.get_json()
    user_input = data.get('input_text')
    result = f"Hello, {user_input}! This is the result of your script."
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
