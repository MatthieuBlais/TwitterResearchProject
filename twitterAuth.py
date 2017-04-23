

"""This script is meant to connect to the Twitter API via the tokens below"""
import tweepy

consumer_key='gm8OWc9XOnBvjfjP79EvM7V2W'
consumer_secret='kGRBQMvdu23gsJ0py8SY8VBIxlxwZ2Ub3sty8tgsBIIx3LCNJz'
access_token_key='1947404870-vzaIkiOrlG1IwfV1gv0K9NF07e8Vlqk5XDcSSqJ'
access_token_secret='RmzOp7kaf9mkMxeqZaOQgHVh1QgbF3D2MzlQjZkueh0gO'


auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
api = tweepy.API(auth)

if(api.verify_credentials):
    print 'We sucessfully logged in'