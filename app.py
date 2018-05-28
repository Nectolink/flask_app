from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')

def main():
    return render_template('index.html')
@app.route('/home')	
def home():
    return render_template('home.html')

if __name__ == "_main_":
    app.run(debug=True, host="0.0.0.0", port=80)