import requests
from bs4 import BeautifulSoup
import mysql.connector

prefix = "https://content.codecademy.com/courses/beautifulsoup/"
webpage_response = requests.get('https://content.codecademy.com/courses/beautifulsoup/shellter.html')

webpage = webpage_response.content
soup = BeautifulSoup(webpage, "html.parser")

turtle_links = soup.find_all("a")
links = []
#go through all of the a tags and get the links associated with them:
for a in turtle_links:
  links.append(prefix+a["href"])
    
#Define turtle_data:
turtle_data = {}

#follow each link:
for link in links:
  webpage = requests.get(link)
  turtle = BeautifulSoup(webpage.content, "html.parser")
  turtle_name = turtle.select(".name")[0]
  turtle_data[turtle_name.get_text()] = []
  webpage = requests.get(prefix + turtle_name.get_text().lower() + '.html')
  turtle = BeautifulSoup(webpage.content, "html.parser")
  stats = []
  items = turtle.find_all('ul')
    
  print(type(items))
  for i in items:
      print(i)
      stats.append(i.get_text())
  turtle_data[turtle_name] = stats

print("password:")
statdb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = input(),
        database="turtles"
        )

mycursor = statdb.cursor()

for t in turtle_data:
  sql = "INSERT INTO stats (name, age, weight, sex, breed, source) VALUES (%s, %s, %s, %s, %s)"
  val = (t[0], t[1], t[2], t[3], t[4])

mycursor.execute(sql, val)
statdb.commit()

sql = "SELECT * FROM stats"
mycursor.execute(sql)
statdb.commit()
