import feedparser

from bs4 import BeautifulSoup

class ResourcesCollector:

	resources_url = [
		('lifehacker','http://feeds.gawker.com/lifehacker/full'),
		('jezebel','http://feeds.gawker.com/jezebel/full'),
		('gawker','http://feeds.gawker.com/gawker/full'),
		('jalopnik','http://feeds.gawker.com/jalopnik/full'),
		('io9','http://feeds.gawker.com/io9/full'),
		('kotaku','http://feeds.gawker.com/kotaku/full'),
		('deadspin','http://feeds.gawker.com/deadspin/full'),
		('gizmodo','http://feeds.gawker.com/gizmodo/full')
	]


	def snapshot(self):
		resources = list()
		for url in self.resources_url:
			text = ''
			feeds = feedparser.parse(url[1])
			items = feeds['items']
			for item in items:
				summary = item['summary']
				soup = BeautifulSoup(summary)
				try:
					content = soup.find('p',{'class':'first-text'}).get_text()
				except Exception:
					content = soup.get_text()
				text += content
				
			resources += [(url[0],text)]
		return resources
