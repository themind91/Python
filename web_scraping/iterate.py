import itertools

for page in itertools.count(1):
	url = 'http://example.webscraping.com/view/-%d' % page
