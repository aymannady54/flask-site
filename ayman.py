from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')

def ayman():
    return render_template('ayman.html')


if __name__ == '__main__':
    app.run(debug=True)
