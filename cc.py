from bottle import get,post,request,template,run
import pygmentsColorer

langlist = pygmentsColorer.getLexers()

@get('/')
def getindex():
	return template('index', langtypes=langlist);

@post('/')
def postindex():
	code = request.forms.get('code')
	lang = request.forms.get('lang')
	return pygmentsColorer.colorCode(code, lang)

run(host='192.168.1.32', port=8080)
