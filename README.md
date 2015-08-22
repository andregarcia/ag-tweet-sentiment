# ag-tweet-sentiment


### Application
This is the source code of a web application that uses IBM's AlchemyAPI to perform sentiment analysis on twitter data.

visit http://ag-tweet-sentiment.mybluemix.net/ to see this application in action.  
visit http://ag-tweet-sentiment.mybluemix.net/html/about.html for more info on this application  


### Deploy
To deploy this web application you must create a file named config.py on the root folder with the following format:  

consumer_key = "XXXXX"  
consumer_secret = "XXXXX"  
access_key = "XXXXX"  
access_secret = "XXXXX"  

replacing XXXXX with the values of your twitter application (you must create a twitter application to get this values. See https://apps.twitter.com/)  

you must also have a api_key.txt file generated using your alchemy api key. This file will be created if you follow the steps here: (http://www.alchemyapi.com/developers/getting-started-guide/using-alchemyapi-with-python) 

if you have followed this steps you may run the application locally by executing flask_main.py (i.e. 'python flask_main.py')

you may deploy this application on bluemix with the following commands:  
cf login -a https://api.ng.bluemix.net  
cf push application-name  



