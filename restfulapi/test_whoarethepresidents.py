import pytest
import requests
from whoarethepresidents import whoAreThePresidents

url_ddg = "https://api.duckduckgo.com"
def test_ddg0():
    resp = requests.get(url_ddg + "/?q=DuckDuckGo&format=json")
    rsp_data = resp.json()
    assert "DuckDuckGo" in rsp_data["Heading"]

def test_whoAreThePresidents():
  the_presidents= ["Lincoln", "Trump", "Washington", "Adams", "Jefferson", "Madison", "Monroe", "Jackson",
                   "Tyler", "Taylor", "Garfield", "Wilson", "Reagan", "Obama", "Buren", "Harrison",
                   "Polk", "Fillmore", "Pierce", "Buchanan", "Johnson", "Grant", "Hayes", "Arthur", 
                   "Cleveland", "McKinley", "Roosevelt", "Taft", "Harding", "Coolidge", "Hoover", "Truman", 
                   "Eisenhower", "Kennedy", "Nixon", "Ford", "Carter", "Bush", "Clinton", "Biden"]
  presidents = whoAreThePresidents()
  for last_name in the_presidents:
    president_found = any(last_name in president for president in presidents)
    assert president_found
  
