from flask import Flask, request, render_template
from chatgpt import run_chat_gpt  # Import the function from your script

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        loader_path = request.form.get('loader')  # Get loader path from form
        response = run_chat_gpt(loader_path)  # Run your chatgpt script with the loader path
        return render_template('index.html', response=response)  # Display the result on the page
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
