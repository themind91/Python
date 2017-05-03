import urllib2 as urlDown
import itertools as tools
import re

# adding an user agent to request
def download(url,user_agent='wswp',num_retries = 2):
	print 'Downloading the url', url
	headers = {'User-agent': user_agent}
	request = urlDown.Request(url, headers=headers)
	try:
		html = urlDown.urlopen(request).read()
	except urlDown.URLError as e:
		print 'Download error', e.reason
		html = None

		if num_retries > 0:
			if hasattr(e,'code') and 500 <= e.code < 600:
				#recursivamente pega 5xx erros de http
				return download(url, num_retries-1)
	return html	

def crawler_sistemap(url):
	sitemap = download(url)
	links = re.findall('<loc>(.*?)</loc>', sitemap)
	for link in links:
		html = download(link)

def verifyErrors():
	max_errors = 5

	num_errors = 0

	for page in tools.count(1):
		url = 'http://example.webscraping.com/view/-%d' % page
		html = download(url)
		if html is None:
			num_errors+=1
		if num_errors == max_errors:	
			break
		else:
			print 'sucess'
			num_errors = 0			


print verifyErrors()
print crawler_sistemap('http://example.webscraping.com/sitemap.xml')