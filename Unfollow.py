'''This Program is to unfollow the user on Twitter who doesn't follow you'''


import tweepy as tw

consumer_key= '*********'
consumer_secret= '*******************'

access_token= '******************************'
access_token_secret= '*******************************'

''' You can grt consumer key and consumer secter as API key and secret 
 And Access token and secret from logging into twitter developer website'''

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)



users = api.get_follower_ids(screen_name = 'koun_himanshu')
USERS = api.get_friend_ids(screen_name = 'koun_himanshu')


a=0
for i in USERS:
    if users.count(i) == 1:
        pass

    else:
        api.destroy_friendship(id = i)
        print('Unfollowed')
        a += 1

print('Unfollwed',a,'peolpe')
