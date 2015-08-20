#!/usr/bin/python

from twitter import *


class MyTwitterSearch():

	def __init__(self):
		config = {}
		execfile("config.py", config)

		self.twitter = Twitter(
		        auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))


	def search(self, q, count):
		search_results = []
		query = self.twitter.search.tweets(q = q, count = count)
	
		for result in query["statuses"]:
			search_results.append(result)
			#print "(%s) @%s %s" % (result["created_at"], result["user"]["screen_name"], result["text"])
		return search_results




## testing module
if __name__=='__main__':
	ts = MyTwitterSearch()
	cont = 1
	for x in ts.search('dilma', 10):
		print str(cont) + ')', x['text'], '\n'
		cont += 1
