from bs4 import BeautifulSoup
import sys

f = open("C:\\pythonProjects\\HTML\\followers.html", 'r')

soup = BeautifulSoup(f, 'html.parser')
hrefs = soup.find_all('a')

sys.stdout = open("C:/pythonProjects/HTML/followers.xlsx", "w")

for href in hrefs:
    print(href.get_text())

sys.stdout.close()

f.close()
