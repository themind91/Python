import re
import helloWorld.py as get

def link_crawler(seed_url, link_regex):

	craw_queue = [seed_url]

	while craw_queue:
		url = craw_queue.pop()
		html = get.download(url)
		# filtrando links que se apliquem ao regex
		for link in get_links(html):
			if re.match(link_regex, link):
				craw_queue.append(link)

def get_links(html):
	# a regular expression to extract all links from the webpage    
	webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
	return webpage_regex.findall(html)



link_crawler('http://example.webscraping.com', 'example.webscraping.com/(index|view)/')	
