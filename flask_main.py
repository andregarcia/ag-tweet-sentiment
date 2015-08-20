"""Cloud Foundry test"""
from flask import Flask,send_from_directory
import os
import MyTwitterSearch


app = Flask(__name__)

# On Bluemix, get the port number from the environment variable VCAP_APP_PORT
# When running this app on the local machine, default the port to 8080
port = int(os.getenv('VCAP_APP_PORT', 8080))

@app.route('/')
def hello_world():
	s = 'Hello World Again! I am running on port ' + str(port)
	ts = MyTwitterSearch.TwitterSearch()
	res = ts.search('dilma', 10)
	for r in res:
		s += '<br/><br/>' + r['text']
	return s


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
	app.run(host='0.0.0.0', port=port)



