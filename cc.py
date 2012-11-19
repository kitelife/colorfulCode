import os
from bottle import get,post,request,template,static_file,run
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
	return static_file(filename,root=os.getcwd()+'/static')

# debug=True
# In debug mode, Bottle is much more verbose and provides helpful debugging information
# whenever an error occurs. It also disables optimisations that might get in your way
# Here is an incomplete list of things that change in debug mode:
#        The default error page shows a traceback.
#        Templates are not cached
#        Plugins are applied immediately
#
# Just make sure to not use the debug mode on a production server.
#
# Bottle runs on the built-in wsgiref WSGIServer by default. This
# non-threading HTTP server is perfectly fine for development and
# early production, but may become a performance bottleneck when 
# server load increases.
# There are three ways to eliminate this bottleneck:
#	Use a multi-threaded or asynchronous HTTP server
#	Spread the load between multiple Bottle instances.
#	Do both.
#
# reloader=True
# During development, you have to restart the server 
# a lot to test your recent changes. The auto reloader
# can do this for you. Every time you edit a module file,
# the reloader restarts the server process and loads the
# newest version of your code.
#
run(host='127.0.0.1', port=8080, debug=True, reloader=True)
