from flask import Flask, render_template,request,jsonify
from newsapi import NewsApiClient
import tweepy
from  datetime import timedelta, datetime
import requests


app = Flask(__name__)

# API key
API_KEY="MidO9QhjECj3pBTUDFC4jTpIw"
# API Secret Key
API_SECRET="vVZ5Mcho45NY6kr3pKYItv1OxldfhuqL2Pam7uw19S0OjYx9po"
# Bearer Token
# AAAAAAAAAAAAAAAAAAAAACkBOwEAAAAAKrz2PWaRlhfPlwxpbWuBEqIga1M%3DSKUjIfItBrGpm1DTUX6DJFRYAoiGI2ug9gxg4ES0EO515zwGFP
# Access token
ACCESS_TOKEN="1210144233157545985-IBDjTH5ywEOk1Zg84KcUMW82YBMl5B"
# Access token secret
ACCESS_TOKEN_SECRET="Qhoeh5wT3AxFYU6JRAjpzPrQig4ldvBWyqfQybcysAU0j"

api_key = API_KEY
api_secret = API_SECRET
access_token = ACCESS_TOKEN
access_token_secret = ACCESS_TOKEN_SECRET

# news api
News_API_KEY = 'd5f86ab6f4ba4e139f282e1472316682'


auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

@app.route('/', methods=['post', 'get'])
def index():
    if request.method == 'POST':
        place = request.form.get('place')
        needs = request.form.get('need')
        current_time = datetime.now()
        a_day_before = current_time - timedelta(days=1)
        twet = [tweet for tweet in tweepy.Cursor(api.search, q=f'{place} {needs} verified',result_type='recent').items(100)]

        return render_template('result.html',tweets_context=twet,a_day_before=a_day_before)
    return render_template('index.html')


# @app.route('/vaccine', methods=['post', 'get'])
# def vaccine():
#     if request.method=='POST':
#         pincode= request.form.get('pincode')
#         date= datetime.today().strftime('%d-%m-%Y')

#         res = requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin", params={"pincode":pincode, "date": date})

#         data = res.json()

#         # print(data['centers'][0]['sessions'][0])
#         return render_template('available-vaccine.html', centers=data['centers'])
#     return render_template('vaccine.html')


@app.route("/vaccine")
def vaccine():
    return render_template('vaccineJs.html')

@app.route("/health")
def homepage():
    newsapi = NewsApiClient(api_key=News_API_KEY)

    topheadlines = newsapi.get_top_headlines(language='en', category='health',country='in')
    # print(th)
    articles = topheadlines['articles']
    # print(articles)
    desc=[]
    news=[]
    images = []
    urls = []
    for i in range(len(articles)):
        myarticles = articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        images.append(myarticles['urlToImage'])
        urls.append(myarticles['url'])
    mylist = zip(news,desc,images,urls)
    return render_template('health.html',context=mylist)