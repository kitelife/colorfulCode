import os
import subprocess
import time

cwd = os.getcwd() + '/compileenv/'

def subprocessPopen(cmd,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,cwd=cwd,shell=True):
	return subprocess.Popen(cmd,stdin=stdin,stdout=stdout,stderr=stderr,cwd=cwd,shell=shell)

def scriptrun(cmd, filename):
	p = subprocessPopen(cmd)
	result =  p.stdout.read()+p.stderr.read()
	os.remove(filename)
	return result.replace('\n','<br />')

def compilerun(compilecmd, runcmd, filename):
	p = subprocessPopen(compilecmd)
	compileresult=p.stdout.read()+p.stderr.read()
	p = subprocessPopen(runcmd)
	runresult = p.stdout.read()+p.stderr.read()
	result='<b>Compile Output:</b><br />'+compileresult+'<br /><b>Run Output:</b><br />' + runresult
	runfilename = cwd + filename
	if os.path.isfile(runfilename):
		os.remove(cwd+filename)
	os.remove(runfilename+'.c')
	return result.replace('\n','<br />')

def compilerunCode(sourcecode, lang):
	if not os.path.isdir(cwd):
		os.mkdir(cwd)
	if lang == 'python':
		filename = cwd+(str)(time.time())+'.py'
		open(filename, 'w').write(sourcecode)
		cmd = 'python %s' % filename
		return scriptrun(cmd, filename)
	elif lang == 'c':
		filenamenosubfix = (str)(time.time())
		sourcefilename = cwd + filenamenosubfix+'.c'
		open(sourcefilename, 'w').write(sourcecode)
		compilecmd = 'gcc -Wall %s -o %s'%(sourcefilename, filenamenosubfix)
		runcmd = './%s'%filenamenosubfix
		return compilerun(compilecmd, runcmd, filenamenosubfix)
