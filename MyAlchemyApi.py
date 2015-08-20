# -*- coding: utf-8 -*-
from alchemyapi import AlchemyAPI
import pprint

class MyAlchemyApi():

	def __init__(self):
		self.ap = AlchemyAPI()

	def analyze_single_tweet(self, tweet):
		response = self.ap.sentiment('text', tweet['text'])		

		ret = {
			'text' : tweet['text'],
			'language' : None,
			'type' : None,
			'score' : None,
			'error' : None
		}
		if response['status'] == 'OK':
			ret['type'] = response['docSentiment']['type']
			if 'language' in response:
				ret['language'] = response['language']
			if 'score' in response['docSentiment']:
				ret['score'] = response['docSentiment']['score']
			ret['error'] = None
		else:
			ret['error'] = response['statusInfo']

		return ret

	def analyze_multiple_tweet(self, tweets):
		ret = []
		for t in tweets:
			ret.append(self.analyze_single_tweet(t))
		return ret


if __name__=='__main__':
	#testing analyze single tweet
	ap = MyAlchemyApi()
	print '\n\nAnalyzing single tweet'
	pprint.pprint(ap.analyze_single_tweet({'text' : 'que dia bom hoje!'}))

	#testing analyze multiple tweets
	print '\n\nAnalyzing multiple tweet'
	ret = ap.analyze_multiple_tweet([
					{'text' : 'O preço do tomate está muito caro'},
					{'text' : 'O dia está chuvoso'}
				])
	pprint.pprint(len(ret))
	pprint.pprint(ret)
	



