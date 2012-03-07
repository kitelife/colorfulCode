from bottle import get,post,request,route,template,run
import pygmentsColorer

langlist = pygmentsColorer.getLexers()
stylelist = pygmentsColorer.getStyles()

@get('/')
def getindex():
	return template('index', langtypes=langlist,styles=stylelist);

@post('/')
def postindex():
	lang=request.forms.get('lang')
	style=request.forms.get('style')
	code = ""
	if request.files:
		code=request.files.codefile.file.read()
	else:
		code=request.forms.get('code')
	return pygmentsColorer.colorCode(code, lang, style)

run(host='192.168.1.32', port=8080)
