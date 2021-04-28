from flask import Flask, render_template,request
import tweepy
from  datetime import timedelta, datetime

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
        # print(twet)
        '''
        for tweet in tweepy.Cursor(api.search, q=f'{place} {needs} verified',result_type='recent').items(100):
            if tweet.created_at >= a_day_before:
                tweeted_or_not = tweet.text[0:2]
                if tweeted_or_not!='RT':
                    text_tweeter = tweet.text
                    date_created = tweet.created_at
                    # day_created = date_created.strftime('%a')
                    # date_created = date_created.strftime('%w')
                    # year_created = date_created.strftime('%Y')
                    # final_time = f"{day_created} {date_created}, {year_created}"
                    url_of_tweet = f"https://twitter.com/{tweet.user.screen_name}/status/{tweet.id}"
                    # print(f'{text_tweeter} {date_created} {url_of_tweet}')
        '''
        # tweets_context = [{
        #     'text':text_tweeter,
        #     'time_created':date_created,
        #     'url_tweet':url_of_tweet
        # }]
        # print(f'{text_tweeter} {date_created} {url_of_tweet}')
                    # print(f"https://twitter.com/{tweet.user.screen_name}/status/{tweet.id}")
        return render_template('result.html',tweets_context=twet,a_day_before=a_day_before)
    return render_template('index.html')