import httplib2
import urllib
from bs4 import BeautifulSoup
usr_name=dict();
usr_name={'b1xxxxxxx':'xyz'} # usrname:password this only a sample user name and password
conn = httplib2.Http()
conn.follow_redirects=False
headers={"Accept-Encoding": "gzip, deflate",'Content-type': 'application/x-www-form-urlencoded'}
resp, content = conn.request("http://172.16.24.1:1000/logout?05070805041ac6d7") # replace the ip address with that of your firewall
print "logout_sucessfull"
for i in usr_name:
  resp, content = conn.request("http://www.stackoverflow.com")
  stripped = content.split()
  st=stripped[6][6:-7];
  indx=st.index('?');
  magic=st[indx+1:]
  resp, content = conn.request(st)
  print "Using ",i;
  body={"4Tredir":"http://y.co","magic":magic,"username":i,"password":usr_name[i]}
  resp,content = conn.request("http://172.16.24.1:1000", method="POST", headers=headers, body=urllib.urlencode(body) )
  soup = BeautifulSoup(content, 'html.parser')
  if(soup.title.string==u'\n      Firewall Authentication Keepalive Window\n    ') :  
              print "Authenticated with ", i
              break;

