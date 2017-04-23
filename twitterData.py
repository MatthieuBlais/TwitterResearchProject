import tweepy
import time
import twitterAuth
import datetime
from nltk.tokenize import TweetTokenizer
tknzr = TweetTokenizer()
api = twitterAuth.api

#MAIN FUNCTIONS
def getCustomersId( screenName ):
    _followersId = getFollowersId( screenName )
    print "I got all followers : " + str(len(_followersId))
    _customersIds = []
    for follower in _followersId:
        #if isCustomer(follower):
        _customersIds.append(str(follower))
    return _customersIds

def getCustomersIdByCompanyName( screenName ):
    _followersId = getFollowersIdByCompanyName( screenName )
    print "Number of Followers of " + screenName +": "+str(len(_followersId))
    _customersIds = []
    for follower in _followersId:
        #if isCustomer(follower):
        _customersIds.append(str(follower))
    return _customersIds

def getCompaniesFriendshipById ( userId ):
    _ids = getFriendsIdById( userId )
    _companies = []
    for _id in _ids:
        _profile = getProfileUserById(_id)
        if isCompany( _profile ):
            _companies.extend(_profile)
    return _companies

def getCompanyIds( companyNames ):
    _companyIds = []

    if len(companyNames) > 1:
        for companyName in companyNames:
            try:
                id = api.get_user(screen_name=companyName).id_str
            except tweepy.error.TweepError:
                False
            if id != False:
                _companyIds.append(id)
    else:
        user = api.get_user(screen_name="beautybridge")
        _companyIds.append(user.id_str.encode('utf-8'))

    return _companyIds

#DETAIL DATA
def getCustomersDetails( userIds ):
    _customers = []
    count=0
    for _user in userIds:
        count = count +1
        print str(count)+"/"+str(len(userIds))+" customer details"
        time.sleep(15)
        try:
            _user = api.get_user(user_id=_user)
            if isActive(_user) and isCustomer(_user):
                _customers.append({
                    "customerId" : _user.id_str.encode('utf-8'),
                    "name": _user.screen_name.encode('utf-8'),
                })
        except tweepy.error.TweepError:
            print "ERROR TIME OUT"
    return _customers

def getCompanyDetails ( userIds ):
    _companies = []
    count = 0
    for _user in userIds:
        count = count +1
        print "companyDetails : " +str(count) +"/"+str(len(userIds))
        print _user
        if isActive(_user) and isCompany(_user):
            _companies.append( getProfileUserById ( _user ))
    return _companies

def getLinksBetweenCompanyCustomers ( companyId, customerIds ):
    _link = []
    for customerId in customerIds:
        _link.append({
            "companyId" : companyId,
            "customerId" : customerId
        })
    return _link

def getLinksBetweenFollowedCompanyCustomers ( customerId, companyIds ):
    _link = []
    for companyId in companyIds:
        _link.append({
            "companyId" : companyId,
            "customerId" : customerId
        })
    return _link
#"ShaunFKiely"
#37945647
#GET DATA
def getFollowersId( screenName ):
    _ids = []
    print screenName
    for page in tweepy.Cursor(api.followers_ids, user_id=screenName).pages():
        _ids.extend(page)
        time.sleep(60)

    return _ids

def getFollowersIdByCompanyName( screenName ):
    _ids = []
    for page in tweepy.Cursor(api.followers_ids, screen_name=screenName).pages():
        _ids.extend(page)
        time.sleep(60)
    return _ids



def getFriendsIdByName( screenName ):
    _ids = []
    for page in tweepy.Cursor(api.friends_ids, screen_name=screenName).pages():
        _ids.extend(page)
        time.sleep(60)
    return _ids

def getFriendsIdById( userId ):
    _ids = []
    try:
        for page in tweepy.Cursor(api.friends_ids, user_id=userId).pages():
            _ids.extend(page)
            time.sleep(60)
        return _ids
    except tweepy.error.TweepError:
        print "ERROR TIME OUT"
        return []
    return

def getProfileUserById ( userId ):
    try:
        print userId
        time.sleep(15)
        user = api.get_user(user_id=userId)
        return {
            "description" : user.description.encode("utf-8"),
            "url" : user.url,
            "user_id": user.id_str,
            "screen_name": user.screen_name.encode("utf-8")
        }
    except tweepy.error.TweepError:
        print "ERROR TIME OUT"
        return []
    return


def getProfileUserByScreenName ( screenName ):
    user = api.get_user(screen_name=screenName)
    return {
        "description" : user.description,
        "url" : user.url,
        "user_id": user.id_str,
        "screen_name": user.screen_name
    }

def getCompaniesFriendshipById ( userId ):
    _ids = getFriendsIdById( userId )
    _companies = []
    count =0
    for _id in _ids:
        count = count +1
        print "getFriendship: "+str(count)+"/"+str(len(_ids))
        _profile = getProfileUserById(_id)
        if isCompany( _profile ):
            _companies.append(str(_id))
    return _companies

def getCompaniesFriendshipByIdv2 ( userId ):
    _ids = getFriendsIdById( userId )
    #_companies = []
    #count =0
    """for _id in _ids:
        count = count +1
        print "Progress Get Friends: "+str(count)+"/"+str(len(_ids))
        _profile = getProfileUserById(_id)
        if isCompany( _profile ):
            _companies.append(_profile)"""
    return _ids

def getCompaniesFriendshipByName ( screenName ):

    _ids = getFriendsIdByName( screenName )

    _companies = []
    for _id in _ids:
        _profile = getProfileUserById(_id)
        if isCompany( _profile ):
            _companies.append(_profile)
    return _companies

def getTweetUserById ( userId ):
    _tweets = []
    try:
        _items = api.user_timeline(user_id = userId,count=50, exclude_replies=True, include_rts=False)
        time.sleep(5)
        _firstIteration = True
        if len(_items)>19:
            if isActiveV2(_items ) and isCompanyV2(_items[0].author):
                for _item in _items:
                    _tweet = {
                        "description" : _item.author.description.encode("utf-8"),
                        "url" : _item.author.url,
                        "user_id": _item.author.id_str,
                        "screen_name": _item.author.screen_name.encode("utf-8"),
                        "createdAt": _item.created_at,
                        "text": _item.text,
                        "tweetId": _item.id_str,
                        "userId" : userId
                    }
                    if isTweetValid(_item.text):
                        _tweets.append(_tweet)
                return _tweets
    except tweepy.error.TweepError:
        print "ERROR TIME OUT"
        return []
    return _tweets

def isTweetValid(text):
    array = tknzr.tokenize(text)
    if len(array)==1 and "http" in array[0]:
        return False
    for word in array:
        if "@" in word:
            return False
    return True

def getTweetUserByName ( screenName ):
    _tweets = []
    _items = api.user_timeline(screen_name = screenName,count=50)
    for _item in _items:
        _tweet = {
            "created_at": _item.created_at,
            "text": _item.text.encode("utf-8"),
            "tweet_id": _item.id_str,
        }
        _tweets.extend(_tweet)
    return _tweets




#CHECK DATA
def isCompany ( profile ):
    if profile == False or profile == []:
        print "No Profile"
        return False
    if profile.get("url") == "None":
        print "No URL"
        return False
    else:
        return True
    return

def isCompanyV2 ( user ):
   if user.url == "None":
        print "No URL"
        return False
   if user.description == "None" or user.description == "" or user.description == []:
        print "No Description"
        return False
   if user.lang != "en":
       print "No English"
       return False

   return True

def isActive ( user ):
    try:
        _isActive = True
        if user.statuses_count > 50:
            _dates = api.user_timeline(screen_name = user.screen_name,count=20)
            _limitDate = datetime.datetime.now() - datetime.timedelta(days=31)
            for _date in _dates:
                if _date.created_at < _limitDate:
                    _isActive = False

        else:
            _isActive = False
    except tweepy.error.TweepError:
        _isActive = True
    return _isActive


def isActiveV2 ( user ):
    _isActive = True
    days = 31
    _limitDate = datetime.datetime.now() - datetime.timedelta(days=days)
    counter = 0
    for _date in user:
        counter = counter +1
        if _date.created_at < _limitDate:
            _isActive = False
        if counter==20:
            return _isActive
    if counter < 10:
        _isActive = False
    return _isActive


def isCustomer ( user ):
    try:
        if len(user)<1:
            return False
        _isCustomer = True
        if user[0].author.friends_count > 500 or user[0].author.friends_count < 25 or user[0].author.statuses_count<50:
            _isCustomer = False
    except tweepy.error.TweepError:
        _isCustomer = True
    return _isCustomer



def extendWithoutDuplicate ( list, items):
    for item in items:
          if item not in list:
            list.append(item)
    return list

