import requests
from bs4 import BeautifulSoup

slist = []

for i in range(10,20):
    res = requests.post('http://cs.unm.edu/~chavoshi/debot/api.php', data={'api_key':'uSTTnDjq7DmKgaYpBAklP4wBsIKAiHfDp0mEtxUq', 'srv_type': '3','date_1': '2018-01-'+str(i), 'date_2': '2018-01-'+str(i)})

    res = BeautifulSoup(res.text, "lxml")
    sname = res.response.day.findAll("screen_name") #will have the list of <screen_name>abc</screen_name>

    for i in sname:
        slist.append(str(i)[13:-14])

    print slist
    print "done"




	
