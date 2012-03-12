import os
from bottle import get,post,request,route,template,static_file,run
import pygmentsColorer
import fileoperation
import compileandrun

langlist = pygmentsColorer.getLexers()
stylelist = pygmentsColorer.getStyles()

@get('/')
def getindex():
	return template('index', langtypes=langlist,styles=stylelist);

@get('/filelist.json')
def getfilelist():
	codefilelist = fileoperation.getFilelist()
	codefilelist.sort()
	codelistJson={}
	index = 0
	for codefile in codefilelist:
		codelistJson[index]=codefile
		index += 1
	return codelistJson
@post('/getfilecontent')
def getFilecontent():
	return pygmentsColorer.getColorfilecontent(request.forms.get('codefilename'))

@post('/')
def postindex():
	lang=request.forms.get('lang')
	style=request.forms.get('style')
	code = ""
	if request.files:
		code = request.files.codefile.file.read()
		if request.forms.get('save'):
			filename = request.files.codefile.filename
			fileoperation.saveFile(filename, code)
		request.files.codefile.file.write("")
	else:
		code=request.forms.get('code')
	return pygmentsColorer.getColorCode(code, lang, style)

@post('/compilesourcecode')
def compileSourceCode():
	sourcecode=request.forms.get('sourcecode')
	langtype = request.forms.get('langtype')
	return compileandrun.compilerunCode(sourcecode, langtype)

@get('/static/<filename>')
def server_static(filename):
	path=os.getcwd()+'/static'
	return static_file(filename,root=os.getcwd()+'/static')

run(host='192.168.1.32', port=8080)
