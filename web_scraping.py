import requests 
from bs4 import BeautifulSoup 

new_res = requests.get('https://news.ycombinator.com/') 

soup = BeautifulSoup(new_res.text, 'html.parser')
print(soup.body.content) 
print(soup.title)
print(soup.a)
print(soup.find_all('div')) 
print(soup.find(id='score_27112960')) 
print(soup.select('#score_27112960'))

votes = soup.select('.score')
link = soup.select('.storylink')
print(votes[0].get('id'))  

def create_custom_hackernews_for_me(links,votes):
    hn=[] 
    for idx,item in enumerate(links):
      title = link[idx].getText()
      href = links[idx].get('herf', None) 
      points = int(votes[idx].getText().replace(' points',''))
      print(points)
      a=[] 
      if points > 100:
          a.append(points)
      print(a)
      hn.append({'title':title,'link':href})

    return hn 

print(create_custom_hackernews_for_me(link,votes)) 

