import csv

def saveData(companies, customers, tweets, linkCompanyCustomer, linkFollowedCompanyCustomer):
    saveCompanies(companies)
    saveCustomers (customers)
    saveTweets (tweets)
    saveCompanyCustomeLinks (linkCompanyCustomer)
    saveCustomerFollowedCompanyLinks (linkFollowedCompanyCustomer)
    return

def saveCompanies ( companies):
    print companies
    companies.pop()
    companyArray =[]
    for company in companies:
        company.get("user_id")
        companyArray.append([company.get("user_id"), company.get("screen_name"), company.get("description"), company.get("url")])

   # companyArray = [[company.get("user_id"), company.get("screen_name"), company.get("description"), company.get("url")] for company in companies]

    #write the csv
    with open('companies.csv', 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(["CompanyId","Name","Description", "Url"])
        writer.writerows(companyArray)
    return

def saveCustomers (customers):
    print customers[0]
    customerArray = [[customer.get("customerId"), customer.get("name")] for customer in customers]

    #write the csv
    with open('customers.csv', 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(["CustomerId","Name"])
        writer.writerows(customerArray)
        
    return

def saveTweets (tweets):
    print "tweets : " + str(len(tweets))
    print tweets
    #tweets.pop()
    tweetArray=[]
    for tweet in tweets:
        tweet.get("tweetId")
        tweetArray.append([tweet.get("tweetId"), tweet.get("text"), tweet.get("createdAt"), tweet.get("userId")])

    #write the csv
    with open('tweets.csv', 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(["TweetId","Text","CreatedAt", "CompanyId"])
        writer.writerows(tweetArray)
        
    return

def saveCompanyCustomeLinks (linkCompanyCustomer):
    compcustArray= []
    for test in linkCompanyCustomer:
        for link in test:
            link.get("companyId")
            compcustArray.append([link.get("companyId"), link.get("customerId")])

    #write the csv
    with open('Company_Customer.csv', 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(["CompanyId","CustomerId"])
        writer.writerows(compcustArray)
        
    return

def saveCustomerFollowedCompanyLinks (linkFollowedCompanyCustomer):
    follocustArray= []
    for test in linkFollowedCompanyCustomer:
        for link in test:
            link.get("companyId")
            follocustArray.append([link.get("customerId"), link.get("companyId")])

    #write the csv
    with open('Customer_FollowedComapny.csv', 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(["CustomerId","CompanyId"])
        writer.writerows(follocustArray)

    return


def saveNewData(companyName, customerId, tweets):
    data = []
    for tweet in tweets:
        data.append([companyName,customerId,tweet.get("user_id").encode("utf-8"), tweet.get("description"), tweet.get("tweetId").encode('utf-8'), tweet.get("text").encode('utf-8'), tweet.get("createdAt")])

    with open('twitterData.csv', 'ab') as f:
        writer = csv.writer(f)
        writer.writerows(data)
        print "Save " + str(len(data)) + " tweets"
    return

