import os
import glob

currentDir = os.getcwd()

def saveFile(filename, content):
	targetDir = currentDir + "/codefiles/"
	if not os.path.isdir(targetDir):
		os.mkdir(targetDir)
	absolute = targetDir + filename
	tf = open(absolute, 'w')
	tf.write(content)

def getFilelist():
	filelist = glob.glob(currentDir+'/codefiles/*')
	return [filename.split('/')[-1] for filename in filelist]

def getFilecontent(filename):
	return open(currentDir+'/codefiles/'+filename).read()
