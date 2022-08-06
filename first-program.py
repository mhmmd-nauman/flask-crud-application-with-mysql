from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = 'many-secret-key'

@app.route('/')
def index():
     return render_template('first-program.html')

if __name__ == "__main__":
    app.run(debug=True)