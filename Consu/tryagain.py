# organize links files and try to download it again

with open ('links.txt', 'r') as f:
	links = f.read()

links = links.split('.pdf')

links = [l + '.pdf' for l in links]

for l in links:
	import downloadall as down

	down.download_pdf(l, "extra")
