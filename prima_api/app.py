from flask import  Flask

app = Flask(__name__)
@app.route('/')

def prima_api():
    return 'PRIMEIRA API'

if __name__ == '__main__':
    app.run(debug=True)
