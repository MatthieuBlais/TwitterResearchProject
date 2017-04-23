import twitterData as twitter
import csvFile as csv
import time
"""
companyNames = ["BuyVansShoes",

                "ShaunFKiely",
                "MadisonZyluk",
                "StarFactoryPR",
                "chartjungle",
                "recycle_now",
                "Rockler",
                "DureeAndCompany",
                "PizzaHacker",
                "RickyProehl",
                "OregonianSports",
                "TrueFilmPro",
                "Audiolines",
                "HRS",
                "BestFares",
                "sphinn",
                "beautybridge",
                "bigelowtea",
                "ThaDevineMsB",
                "WaveWaterWorks",
                "TutoringHut",
                "successforce",
                "BeautySweetSpot",
                "transmediale",
                "fardhie",
                "CCateringC",
                "joshuabaer",
                "RoswellPark",
                "Corposflex",
                "SportGossiper",
                "nytvf",
                "WestbrookVR",
                "eAssistancePro",
                "Hieu9",
                "wemoto",
                "EarnSeo",
                "AmericanSalon",
                "MayaTheRD",
                "BeautiMed",
                "athenspc",
                "onstartups",
                "wetaber",
                "queenoflight88",
                "EonlineTutors",
                "NormandieA",
                "LatinoUSA",
                "focalstudio",
                "TicketNetwork",
                "MiggyLikey",
                "Andolasoft",
                "FTColdSpring"

                ]
companyNames = ["ShaunFKiely"]

count = 0
followedCompanyTweets = []
customers = []
customers2 = []
companies = []
linkCustomerFollowedCompanies = []
linkCompanyCustomers =[]
companyIds = twitter.getCompanyIds(companyNames)
companies.extend(companyIds)
print "nbr companies : " + str(len(companies))
for company in companyIds:
    count = count +1
    customerIds = twitter.getCustomersId ( company )
    print "companies: "+str(count)+"/" + str(len(companyIds))
    customers.append(twitter.extendWithoutDuplicate(customers, customerIds))
    linkCompanyCustomers.append(twitter.getLinksBetweenCompanyCustomers( company, customerIds))
    count2 =0
    for customerId in customerIds:
        count2 = count2 +1
        followedCompaniesCustomer = twitter.getCompaniesFriendshipById( customerId )
        print "customerIds: "+str(count2)+"/" + str(len(customerIds))
        companies.append(twitter.extendWithoutDuplicate(companies, followedCompaniesCustomer))
        linkCustomerFollowedCompanies.append(twitter.getLinksBetweenFollowedCompanyCustomers (customerId, followedCompaniesCustomer))
        count3 =0
        for followedCompany in followedCompaniesCustomer:
            count3 = count3+1
            followedCompanyTweets = twitter.getTweetUserById(followedCompany)
            print "tweets: " + str(count3)+"/"+str(len(followedCompaniesCustomer))

companies = twitter.getCompanyDetails( companies )
customers = twitter.getCustomersDetails( customers )
csv.saveData(companies, customers, followedCompanyTweets, linkCompanyCustomers, linkCustomerFollowedCompanies)
"""
companyNames = ["beautybridge"]
#For all companies tested
for companyName in companyNames:
    #Get Followers
    customerIds = twitter.getCustomersIdByCompanyName ( companyName )
    #Check follower
    #For All Followers
    counter2=0
    for customerId in customerIds:
        if counter2 < 200:
            counter2 = counter2 +1
        else:
        #Get Friends
            try:
                customer = twitter.api.user_timeline(user_id=customerId, count=20)
                time.sleep(5)
                counter2 = counter2+1
                print "Customer of company "+str(counter2)+"/"+str(len(customerIds))
                if twitter.isCustomer(customer):
                    friendProfiles = twitter.getCompaniesFriendshipByIdv2( customerId )
                    #Get Tweets Friends
                    counter =0
                    for friendProfile in friendProfiles:
                        counter = counter +1
                        print "Tweets of friends: "+ str(counter)+"/"+str(len(friendProfiles))
                        tweets = twitter.getTweetUserById(friendProfile)
                         #Save
                        if len(tweets)>0:
                            csv.saveNewData(companyName, customerId, tweets)
            except twitter.tweepy.error.TweepError:
                print "ERROR TIME OUT"




