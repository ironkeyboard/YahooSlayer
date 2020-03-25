import bs4
import requests
import time
import lxml
from colorama import Fore, init
init()
print(Fore.RED + "▓██   ██▓ ▄▄▄       ██░ ██  ▒█████   ▒█████       ██████  ██▓    ▄▄▄  ░▒████   ██▓▓█████  ██▀███  ")
print(" ▒██  ██▒▒████▄    ▓██░ ██▒▒██▒  ██▒▒██▒  ██▒   ▒██    ▒ ▓██▒   ▒████▄    ▒██  ██░░█   ▀ ▓██ ▒ ██▒")
print("  ▒██ ██░▒██  ▀█▄  ▒██▀▀██░▒██░  ██▒▒██░  ██▒   ░ ▓██▄   ▒██░   ▒██  ▀█▄   ▒██ ██░▒███   ▓██ ░▄█ ▒")
print("  ░ ▐██▓░░██▄▄▄▄██ ░▓█ ░██ ▒██   ██░▒██   ██░     ▒   ██▒▒██░   ░██▄▄▄▄██  ░ ▐██▓░▒██  ▄ ▒██▀▀█▄  ")
print("  ░ ██▒▓░ ▓█   ▓██▒░▓█▒░██▓░ ████▓▒░░ ████▓▒░   ▒██████▒▒░██████▒▓█   ▓██▒ ░ ██▒▓░░█████▒░██▓ ▒██▒")
print("   ██▒▒▒  ▒▒   ▓▒█░ ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░▒░▒░    ▒ ▒▓▒ ▒ ░░ ▒░▓  ░▒▒   ▓▒█░  ██▒▒▒ ░░ ▒░ ░░ ▒▓ ░▒▓░")
print(" ▓██ ░▒░   ▒   ▒▒ ░ ▒ ░▒░ ░  ░ ▒ ▒░   ░ ▒ ▒░    ░ ░▒  ░ ░░ ░ ▒  ░ ▒   ▒▒ ░▓██ ░▒░  ░ ░  ░  ░▒ ░ ▒░")
print(" ▒ ▒ ░░    ░   ▒    ░  ░░ ░░ ░ ░ ▒  ░ ░ ░ ▒     ░  ░  ░    ░ ░    ░   ▒   ▒ ▒ ░░     ░     ░░   ░ ")
print(" ░ ░           ░  ░ ░  ░  ░    ░ ░      ░ ░           ░      ░  ░     ░  ░░ ░        ░  ░   ░     ")
print(" ░ ░                                                                      ░ ░                     ")
print("")
print("The Link Scraper For Yahoo")
print("")
print("Created By IronKey | V1.0 beta | python 3.7.4")
print("")
while True:
	your_keyword = input("enter your dork or search term : ")
	print("")
	linkNumber = int(  input("how many pages deep do you want to scrape? ") ) # <--- Raises Error if input is not a number
	lst = []
	# https://search.yahoo.com/search?p=bruhmoment&pz=10&ei=UTF-8&fr=yfp-t&bct=0&fp=1&b=31&pz=10&bct=0&xargs=0
	link = "https://search.yahoo.com/search?p={}&pz=10&ei=UTF-8&fr=yfp-t&bct=0&fp=1&b={}&bct=0&xargs=0"
	for i in range( linkNumber ): 
	    lst.append( link.format( your_keyword, 1 + (i+1)*10 ) ) 
	print("")
	print("beginning search... ")
	print("")
	print("This may take a while... Please be patient")
	print("")
	for i in lst:
	    source = requests.get(i)
	    bs4call = bs4.BeautifulSoup(source.text, "lxml")
	    links = bs4call.findAll('a', {'class':'ac-algo fz-l ac-21th lh-24'})
	    for link in links:
	    	with open('links.txt', 'a') as out:
	    		out.write(str(link['href']) + "\n")
	print("links scraped and saved to file : links.txt")
	print("")
	deepParseInput = input("would you like to run more dorks? :  ")
	print("")
	if deepParseInput == "n" or deepParseInput == "N":
		break
print("I really hope you liked my program! Bye Bye - IronKey")
print("")
input("Press ENTER to leave the program --> ")
#for link in links:
  #with open('baselinks.txt', 'a') as out:
    #out.write(str(link['href']) + "\n")
