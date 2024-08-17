from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        user_input = request.form['input_text']
        result = run_script(user_input)
    return render_template('index.html', result=result)

def run_script(user_input):
    # Replace this with your actual Python script logic
    return f"Hello, {user_input}! Your script ran successfully."

if __name__ == '__main__':
    app.run(debug=True)
