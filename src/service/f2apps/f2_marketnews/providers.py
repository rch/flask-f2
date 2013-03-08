from lxml import etree
from collections import namedtuple
from StringIO import StringIO
import re, requests


NewsItem = namedtuple('NewsItem',['title','desc','link','date'])


class ParseItemError(Exception): pass


class BaseProvider(object):
	
	MAX_ARTICLES = 3
	
	def __init__(self):
		self.mapping = {}
		self.newsItems = []
		r = requests.get(self.feed)
		self.content = r.content
		
	def __iter__(self):
		if len(self.newsItems) == 0:
			skipped = 0
			for event, element in etree.iterparse(StringIO(self.content), tag='item'):
				try:
					self.newsItems.append(self.parseItem(element))
				except ParseItemError:
					skipped += 1
				if len(self.newsItems) >= self.MAX_ARTICLES + skipped:
					break
		return iter(self.newsItems)	
	
	def parseItem(self, item):
		details = {}
		for element in item.iterchildren():
			if self.mapping.has_key(element.tag):
				field, value = self.adaptElement(element)		
				details[field] = value
		return NewsItem(**details)
	
	def adaptElement(self, element):
		raise NotImplementedError()
	
	@property
	def display(self):
		raise NotImplementedError()
	
	@property
	def feed(self):
		raise NotImplementedError()


class YahooBusinessNews(BaseProvider):

	def __init__(self):
		super(YahooBusinessNews, self).__init__()
		self.id = 'yahooBusinessNews'
		self.mapping = {
			'title':'title',
			'description':'desc',
			'link':'link',
			'pubDate':'date'
		}
		# clean up the description, specific to Yahoo! business RSS (http://news.yahoo.com/rss/business)
		self.patterns = []
		self.patterns.append('\<a.*\\>') # remove the start of the first link '<a .... >' around the image
		self.patterns.append('\<\/a\>') # remove the closing link tag '</a>' around the image
		self.patterns.append('\<br.*\/\>') # find the break and remove it
	
	def adaptElement(self, element):
		value = element.text
		if element.tag == 'description':
			if value.find('<img') > -1:
				for pattern in self.patterns:
					re.sub(pattern, '', value)
			else:
				print value
				raise ParseItemError('no img tag in description')
		field = self.mapping[element.tag]
		return field, value
		
	@property
	def display(self):
		return 'Yahoo Business'
	
	@property
	def feed(self):
		return 'http://news.yahoo.com/rss/business'
			
	
class DefaultProvider(YahooBusinessNews):
	pass
