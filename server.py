from flask import Flask, render_template, redirect, url_for, request, session, flash
import feedparser
import models as dbhandler
from urllib.parse import urlparse
import feedfinder2


app = Flask(__name__)

def findrssfeeds(url):
	d = feedparser.parse(url)
	dbhandler.createTable()
	for i in range(len(d.entries)):
	    dbhandler.insertDetail(d.entries[i].title,d.entries[i].link,d.entries[i].published)

@app.route('/', methods=['GET', 'POST'])
def index(details=None,url=None):
    if request.method == 'POST':
    	url = request.form['rssfeed']
    	findrssfeeds(url)
    	data = dbhandler.retrieveDetails()
    	return render_template('home.html',details=data,url=urlparse(url).netloc)
    return render_template('home.html')

@app.route('/rsslink_finder', methods=['GET', 'POST'])
def rsslinkfinder(rssurl=None):
    if request.method == 'POST':
    	weburl = request.form['weburl']
    	c=feedfinder2.find_feeds(weburl)
    	return render_template('rsslink.html',rssurl=c[0])
    return render_template('rsslink.html')

if __name__ == '__main__':
	app.run()