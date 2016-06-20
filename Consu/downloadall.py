import urllib
from sgmllib import SGMLParser
import os

class URLLister(SGMLParser):
    def reset(self):                              
        SGMLParser.reset(self)
        self.urls = []

    def start_a(self, attrs):                     
        href = [v for k, v in attrs if k=='href'] 
        if href:
            self.urls.extend(href)

def get_pdf_links(url):
	print url
	# get urls from url
	try:
		usock = urllib.urlopen(url)
	except:
		print "Webpage not opened"
		if not os.path.exists("NotDownloaded"): os.makedirs("NotDownloaded")
		with open("NotDownloaded/links.txt", 'a') as f:
			f.write(url)
		return []
	parser = URLLister()
	parser.feed(usock.read())         
	usock.close()                     
	parser.close() 
	# filter urls                   
	for url in parser.urls:
		if ".pdf" in url:
			if ("item" not in url) and ("Item" not in url) \
			 and ("iten" not in url) and ("docs" not in url) and \
			 ("distribuidos-no-inicio-da-sessao" not in url):
				pdf.append(url)
	# print pdf
	print len(pdf)
	return pdf

def download_pdf(url, i):
	# get the name o the original file
	rest, name = url.rsplit('/', 1)
	name = "{}/".format(i) + name
	print name
	# download content
	try:
		urllib.URLopener().retrieve(url, name)
	except:
		print "Could not be downloaded"
		if not os.path.exists("NotDownloaded"): os.makedirs("NotDownloaded")
		with open("NotDownloaded/links.txt", 'a') as f:
			f.write(url)
	
def main():
	# The url that is commom between all urls
	rooturl = "http://www.sg.unicamp.br/consu/pautas-e-atas/ano-"

	anos = [2009, 2011, 2012]
	#loop the urls
	for i in anos :	
		year = i
		# Get all interesting urls on a certain url
		 # pdfs = get_pdf_links(rooturl + '{}'.format(year))
		i = i - 2000
		# create file
		if not os.path.exists("{}".format(i)): os.makedirs("{}".format(i))

		# download the content of a url (pdf in this case)
		for url in pdfs:
			download_pdf(url, i)

if __name__ == "__main__":
	main()





