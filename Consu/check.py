

import pdf2txt
import os




def pdf2txt(name):
	
	os.system("ls")


if __name__ == '__main__':
	for file in os.listdir("./"):
		path = "./" + file
		try:
			for f in os.listdir(path):
				
				print file
		except:
			pass
