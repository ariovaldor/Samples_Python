from flask import  Flask,jsonify

app = Flask(__name__)
#@app.route('/<int:id>')
@app.route('/')

def pessoa():

#def pessoa(id):
#    return jsonify({'id': id, 'nome': 'Rafael','profissao':'Analista'})
    return jsonify({'nome': 'Rafael','profissao':'Analista'})

if __name__ == '__main__':
    app.run(debug=True)
