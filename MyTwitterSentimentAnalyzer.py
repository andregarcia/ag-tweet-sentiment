import MyTwitterSearch
import MyAlchemyApi
import pprint



class MyTwitterSentimentAnalyzer():


	def __init__(self):
		self.alcapi = MyAlchemyApi.MyAlchemyApi()
		self.twapi = MyTwitterSearch.MyTwitterSearch()


	def search_term_and_analyze(self, term, max_results):
		search_results = self.twapi.search(term, max_results)
		sentiment_results = self.alcapi.analyze_multiple_tweet(search_results)
		return sentiment_results



#testing module
if __name__=='__main__':
	tsa = MyTwitterSentimentAnalyzer()
	pprint.pprint(tsa.search_term_and_analyze('obama', 2))




