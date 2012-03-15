import os
import glob

_currentDir = os.getcwd()

def saveFile(filename, content):
	targetDir = _currentDir + "/codefiles/"
	if not os.path.isdir(targetDir):
		os.mkdir(targetDir)
	absolute = targetDir + filename
	tf = open(absolute, 'w')
	tf.write(content)

def getFilelist():
	# get the file list under folder codefiles
	filelist = glob.glob(_currentDir+'/codefiles/*')
	return [filename.split('/')[-1] for filename in filelist]

def getFilecontent(filename):
	return open(_currentDir+'/codefiles/'+filename).read()
