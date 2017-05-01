import urllib2 as urlDown

def download(url):
	print 'Downloading the url', url
	try:
		html = urlDown.urlopen(url).read()
	except urlDown.URLError as e:
		print 'Download error', e.reason
		html = None
	return html	

print download('https://www.facebook.com')