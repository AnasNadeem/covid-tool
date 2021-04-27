import tweepy
from  datetime import timedelta, datetime
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
    
# api.verify_credentials()
city_state = input('City name').lower()
type_resource = input('Resource type').lower()

current_time = datetime.now()
a_day_before = current_time - timedelta(days=1)
for tweet in tweepy.Cursor(api.search, q=f'{city_state} {type_resource}',result_type='recent').items(100):
    if tweet.created_at >= a_day_before:
        tweeted_or_not = tweet.text[0:2]
        if tweeted_or_not!='RT':
            # print(tweet.text)
            print(f"https://twitter.com/{tweet.user.screen_name}/status/{tweet.id}")

# print(current_time.strftime('%X'))
# search_results = api.search(q="bihar oxygen verified")
# for i in search_results:
#     print( i.created_at, i.text)
# print(search_results.text, search_results.created_at)``