import os
import subprocess
import time
import threading

_cwd = os.getcwd() + '/compileenv/'

class Command(object):

	def __init__(self, cmd):
		self.cmd = cmd
		self.process = None
		self.out = None
		self.err = None
		self.returncode = None
		self.data = None

	def run(self, data, timeout, env):
		self.data = data
		environ = dict(os.environ).update(env or {})

		def target():
			self.process = subprocess.Popen(self.cmd,
					shell=True,
					env=environ,
					stdin=subprocess.PIPE,
					stdout=subprocess.PIPE,
					stderr=subprocess.PIPE,
					cwd=_cwd,
					bufsize=0,
			)

			self.out, self.err = self.process.communicate(self.data)
		thread = threading.Thread(target=target)
		thread.start()

		thread.join(timeout)
		if thread.is_alive():
			self.process.terminate()
			thread.join()
		self.returncode = self.process.returncode
		return self.out, self.err
'''
def _subprocessPopen(cmd,stdin=subprocess.PIPE,stdout=subprocess.PIPE,\
		stderr=subprocess.PIPE,cwd=_cwd,shell=True):
	return subprocess.Popen(cmd,stdin=stdin,stdout=stdout,\
			stderr=stderr,cwd=cwd,shell=shell)
'''
def _scriptrun(cmd, filename):
	#p = _subprocessPopen(cmd)
	#result =  p.stdout.read()+p.stderr.read()
	cmdprocess = Command(cmd)
	cmdout, cmderr = cmdprocess.run(data=None,timeout=5000, env=None)
	os.remove(filename)

	result = cmdout + cmderr

	return result.replace('\n','<br />')

def _compilerun(compilecmd, runcmd, filename):
	#p = _subprocessPopen(compilecmd)
	#compileresult=p.stdout.read()+p.stderr.read()
	compiling = Command(compilecmd)
	compileout, compileerr = compiling.run(data=None, timeout=None, env=None)
	compileresult = compileout +  compileerr

	cmdprocess = Command(runcmd)
	cmdout, cmderr = cmdprocess.run(data=None, timeout=5000, env=None)
	runresult = cmdout + cmderr
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
			compilecmd = 'gcc -Wall -lm %s -o %s'%(sourcefilename, filenamenosubfix)
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
			compilecmd = "g++ -Wall -lm %s -o %s"%(sourcefilename, filenamenosubfix)
			#runcmd = './%s'%filenamenosubfix
			runcmd = './%s'%(filenamenosubfix)
			result =  _compilerun(compilecmd, runcmd, filenamenosubfix)
			#runfilename = _cwd + filenamenosubfix
			runfilename = filenamenosubfix
			if os.path.isfile(runfilename):
				os.remove(runfilename)
			os.remove(sourcefilename)
			return result
