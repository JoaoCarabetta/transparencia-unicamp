import os
import re

def search_and_clean(name, ano):
	

	if ".pdf" in name:
		print name
		
		#rest = name.split("Ata")

		#new_name = ano + "_" + "ata" + "_" + rest[1] + ".pdf"
		# print  new_name

		# rename("{}/{}".format(ano, name), "Organizado/extra/{}".format(new_name))
		
		# number = re.findall("[-+]?\d+[\.]?\d*", name)

		# print type(number[0])

		# print name, new_number
		
			
		"""		
		if 120 < number[0] < 150:

			new_name = str(number[0]) + "_" + "pauta" + "_" + ano +".pdf"
			print name, new_name
			#rename("{}/{}".format(ano, name), "Organizado/pautas/{}".format(new_name))
		"""

def rename(old_name, new_name):
	print old_name, new_name

	try:
		os.rename(old_name, new_name)
	except:
		print "ja renomeado"


for file in os.listdir("./"):
	path = "./" + file
	try:
		for f in os.listdir(path):
		
			search_and_clean(f, file)
	except:
		pass

