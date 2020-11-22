import requests
from bs4 import BeautifulSoup
import mysql.connector
import base64

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
  turtle_name = turtle.find('p')
  turtle_name = turtle_name.get_text().lower()
  webpage = requests.get(prefix + turtle_name + '.html')
  turtle = BeautifulSoup(webpage.content, "html.parser")
  stats = []
    
  for i in turtle.find_all("li"):
    j = i.get_text().split(' ', 2) 
    if(j[0] == "AGE:"):
        stats.append(float(j[1]))
    elif(j[0] == "WEIGHT:"):
        stats.append(float(j[1]))
    elif(j[0] == "SEX:"):
        if(j[1] == "Male"):
            stats.append('M')
        else:
            stats.append('F')
    else:
        stats.append(j[1] + " " + j[2])
    turtle_data[turtle_name] = stats

<<<<<<< HEAD
print(turtle_data)

statdb = mysql.connector.connect(
        host = "localhost",
        user = "root"
        password = base64.b64decode("dkNBZW9MVXpZdllIOENrYg==")
        database="turtles"
        )
mycursor = statdb.cursor()

for key, val in turtle_data.items():
    insert = "INSERT INTO stats (name, age, weight, sex, breed, source) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (key, val[0], val[1], val[2], val[3], val[4])
    mycursor.execute(insert, values)

statdb.commit()

sql = "SELECT * FROM stats"
mycursor.execute(sql)
statdb.commit()
=======
    statdb = mysql.connector.connect(
	host = "localhost",
        user = "root",
        password = "",
        database="turtles"
        )

    mycursor = statdb.cursor()
    print(stats)
    #sql = "INSERT INTO stats (name, age, weight, sex, breed, source) VALUES (%s, %s, %s, %s, %s)"
    #val = (stats[0], stats[1], stats[2], stats[3], stats[4])

    #mycursor.execute(sql, val)
    #statdb.commit()

    #sql = "SELECT * FROM stats"
    #mycursor.execute(sql)
    #statdb.commit()
>>>>>>> fafd085c41a12fc52bdc64ad1b1e62b82bd4982e
