from flask import Flask,render_template, request
import json
from Model.user import Usuarios
app = Flask(__name__)

@app.route('/')
def get_user():

	 	return render_template('index.html')
	 	
@app.route('/cadastro',methods=['POST'])
def create_user():
		novo_usuario = Usuarios()
		print "passei aqui %s" %request.form['email']
	 	novo_usuario.nome =  request.form['nome']
	 	novo_usuario.telefone =  request.form['telefone']
	 	novo_usuario.email =  request.form['email']

	 	novo_usuario.save()
	 	print 'voce fez um post'
	 	
	 	return render_template('index.html')
	 
@app.route('/usuarios/',methods=['GET','POST'])
def list_users():
	 
	 if request.method == 'POST':
	 	print 'voce fez um post'
	 	print request.form['nome']
	 else:
	 	return render_template('index.html')		
	 


if __name__ == "__main__":
	app.run(debug=True)


