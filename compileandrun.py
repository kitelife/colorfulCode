import os
import subprocess
import time

_cwd = os.getcwd() + '/compileenv/'

def _subprocessPopen(cmd,stdin=subprocess.PIPE,stdout=subprocess.PIPE,\
		stderr=subprocess.PIPE,cwd=_cwd,shell=True):
	return subprocess.Popen(cmd,stdin=stdin,stdout=stdout,\
			stderr=stderr,cwd=cwd,shell=shell)

def _scriptrun(cmd, filename):
	p = _subprocessPopen(cmd)
	p.stdin.write(" \n")
	result =  p.stdout.read()+p.stderr.read()
	os.remove(filename)
	return result.replace('\n','<br />')

def _compilerun(compilecmd, runcmd, filename):
	p = _subprocessPopen(compilecmd)
	compileresult=p.stdout.read()+p.stderr.read()
	p = _subprocessPopen(runcmd)
	runresult = p.stdout.read()+p.stderr.read()
	return ('<b>Compile Output:</b><br />'+compileresult+\
			'<br /><b>Run Output:</b><br />' + runresult).\
			replace('\n','<br />')

def compilerunCode(sourcecode, lang):
	if not os.path.isdir(_cwd):
		os.mkdir(_cwd)
	os.chdir(_cwd)

	if lang == 'python':
		filename = (str)(time.time())+'.py'
		open(filename, 'w').write(sourcecode)
		cmd = 'python %s' % filename
		return _scriptrun(cmd, filename)
	elif lang == 'ruby':
		filename = (str)(time.time())+'.rb'
		open(filename, 'w').write(sourcecode)
		cmd = 'ruby %s' % filename
		return _scriptrun(cmd, filename)
	else:
		filenamenosubfix = (str)(time.time())
		if lang == 'c':
			sourcefilename = filenamenosubfix+'.c'
			open(sourcefilename, 'w').write(sourcecode)
			compilecmd = 'gcc -Wall %s -o %s'%(sourcefilename, filenamenosubfix)
			#runcmd = './%s'%filenamenosubfix
			runcmd = './%s'%filenamenosubfix
			result = _compilerun(compilecmd, runcmd, filenamenosubfix)
			#runfilename = _cwd + filenamenosubfix
			runfilename = filenamenosubfix
			if os.path.isfile(runfilename):
				os.remove(runfilename)
			os.remove(sourcefilename)
			return result

		elif lang == 'c++':
			sourcefilename = filenamenosubfix + '.cpp'
			open(sourcefilename, 'w').write(sourcecode)
			compilecmd = "g++ -Wall %s -o %s"%(sourcefilename, filenamenosubfix)
			#runcmd = './%s'%filenamenosubfix
			runcmd = './%s'%(filenamenosubfix)
			result =  _compilerun(compilecmd, runcmd, filenamenosubfix)
			#runfilename = _cwd + filenamenosubfix
			runfilename = filenamenosubfix
			if os.path.isfile(runfilename):
				os.remove(runfilename)
			os.remove(sourcefilename)
			return result
