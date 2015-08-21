"""Cloud Foundry test"""
from flask import Flask,send_from_directory,request
import os
import MyTwitterSearch
import json
import MyTwitterSentimentAnalyzer


app = Flask(__name__)

# On Bluemix, get the port number from the environment variable VCAP_APP_PORT
# When running this app on the local machine, default the port to 8080
port = int(os.getenv('VCAP_APP_PORT', 8080))

@app.route('/')
def hello_world():
	return send_from_directory('html', 'home.html')



@app.route('/search/term')
def search_term_and_analyze():
	term = request.args.get('q', '')
	if term:
		tsa = MyTwitterSentimentAnalyzer.MyTwitterSentimentAnalyzer()
		res = tsa.search_term_and_analyze(term, 3)
		return json.dumps(res)


#serve html
@app.route('/html/<path:path>')
def send_html(path):
	return send_from_directory('html', path)

#serve js
@app.route('/js/<path:path>')
def send_js(path):
	return send_from_directory('js', path)


#serve css
@app.route('/css/<path:path>')
def send_css(path):
	return send_from_directory('css', path)



if __name__ == '__main__':
	app.run(host='0.0.0.0', port=port, debug=True)



