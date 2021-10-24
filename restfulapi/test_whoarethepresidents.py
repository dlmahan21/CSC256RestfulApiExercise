import pytest
import requests
from whoarethepresidents import whoAreThePresidents

url_ddg = "https://api.duckduckgo.com"
def test_ddg0():
    resp = requests.get(url_ddg + "/?q=DuckDuckGo&format=json")
    rsp_data = resp.json()
    assert "DuckDuckGo" in rsp_data["Heading"]

def test_whoAreThePresidents():
  the_presidents= ["Washington", "Adams", "Jefferson", "Madison", "Monroe", "Jackson", "Buren", "Harrison",
                   "Tyler", "Taylor", "Lincoln", "Garfield", "Wilson", "Reagan", "Obama", "Trump", 
                   "Polk", "Fillmore", "Pierce", "Buchanan", "Johnson", "Grant", "Hayes", "Arthur", 
                   "Cleveland", "McKinley", "Roosevelt", "Taft", "Harding", "Coolidge", "Hoover", "Truman", 
                   "Eisenhower", "Kennedy", "Nixon", "Ford", "Carter", "Bush", "Clinton", "Biden"]
  presidents = whoAreThePresidents()
  for last_name in the_presidents:
    assert last_name in presidents
  
