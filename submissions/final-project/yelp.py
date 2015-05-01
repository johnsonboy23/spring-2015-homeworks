import rauth
import time
import csv
import re

f = open('cuisine.csv','r')
reader = csv.reader(f, delimiter = ',')
names = []
for i in reader:
	for j in i:
		names.append(j)
f.close()

def main():
	api_calls = []
	for name in names:
		params = get_search_parameters(name)
		api_calls.append(get_results(params))
		for i in api_calls:
			for j in i['businesses']:
				categories = {}
				for k in j.keys():
					if k == "rating" or k == "review_count" or k == "name" or k == "categories":
						try:
							temp = str(j[k])
							if k == 'categories':
								print name,
								'''type_cuisine = str()
								for list1 in j[k]:
									for list2 in list1:
										type_cuisine = type_cuisine + ";" + list2

										
								print type_cuisine[1:],'''
							else:
								
								print temp,",", 
						except:
							continue
				print
			

def get_results(params):

	#Obtain these from Yelp's manage access page
	consumer_key = ''
	consumer_secret = ''
	token = ''
	token_secret = ''

  	#consumer_key = "HzKsySt6ZmIDDhHHWzHjEA"
	#consumer_secret = "AKBuFHvUyjFD8PprkhUfG9O3BMo"
	#token = "id1705AwXNyeGyM7qNKermXRjBZuNoGZ"
	#token_secret = "btxB6sbHWahC_s9RqsuQ0sqrtLk"
	
	session = rauth.OAuth1Session(
		consumer_key = consumer_key
		,consumer_secret = consumer_secret
		,access_token = token
		,access_token_secret = token_secret)
		
	request = session.get("http://api.yelp.com/v2/search",params=params)
	
	data = request.json()
	session.close()
	
	return data
		
def get_search_parameters(name):
	params = {}
	params["term"] = name
	params["location"] = "New York, NY"

	return params

if __name__=="__main__":
	main()


