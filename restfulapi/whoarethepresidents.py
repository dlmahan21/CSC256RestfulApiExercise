import requests
url_ddg = "https://api.duckduckgo.com"

def whoAreThePresidents():
  response= requests.get(url_ddg + "/?q=presidents+of+the+united+states&format=json")
  resp_data= response.json()
  topic_list = resp_data['RelatedTopics']
  president_names=[]
  for topic in topic_list:
      president_names.append(topic['Text'])
  return president_names
