#Scrap Hacker News project and save the result in a csv file.
# The csv file should have the following columns: title, link, points, comments, author, rank. 
# The csv file should be sorted by rank in ascending order.




from turtle import title
from urllib import response
import requests
from bs4 import BeautifulSoup
import csv



def get_hacker_news():
    url = "https://news.ycombinator.com/news"
    response = requests.get(url).text


    #doc
    soup = BeautifulSoup(response, 'html.paser')

    first_row = soup.find('tr', class_ = 'athing')

    #extract title

    title = first_row.find('span', class_ = 'titleline').find('a').text
    link = first_row.find('span', class_ = 'titleline').find('a').text
    score = first_row.find('span', class_ = 'titleline').find('a').text
    
