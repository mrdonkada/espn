import requests
from bs4 import BeautifulSoup

def leaders(STAT):
    #Scrapes espn.com and returns a leaderboard of the desired statistic
    url = 'http://espn.go.com/mlb/stats/batting/_/qualified/true'
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')

    #Saves the initial html code to a text file
    with open("espn_page.txt", "w") as initial_file:
        initial_file.write(str(soup))

    #Scrapes the column headers and creates a dict that maps the header to
    #its hyperlink, which gives an ordered leaderboard of the desired stat.
    headers = soup.find('tr', attrs={'class':'colhead'})
    links = headers.find_all('a')
    link_dict = {}
    for i in links:
        link_dict[i.get_text()] = i.get('href')

    print link_dict

    #Raises exception when an unacceptable parameter is given to the function.
    class MyError(Exception):
        def __init__(self, value):
            self.value = value
        def __str__(self):
            return repr(self.value)

    #Passes the desired hyperlink through the url
    for key in link_dict:
        if key==STAT:
            url = link_dict[key]
        else:
            raise MyError("Sorry, I can't accept that. Have you tried all caps?")

    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    print url

    stat_list = []
    i=0

    #Fills stat_list with all the statistics of every desired player and
    #scrapes multiple pages if there is more than one.
    while True:
        if soup.find('a', text='NEXT'):
            all_players = soup.find_all('tr',
            attrs={'class': ['oddrow', 'evenrow']})
            for player in all_players:
                stat_list.append(player.find_all('td'))

                #Removes the tags and leaves only the desired text.
                for n in range(0, len(stat_list[i])):
                    stat_list[i][n] = stat_list[i][n].get_text()
                i+=1

            #Finds the url for the next page of the leaderboard
            next_link = soup.find('a', text='NEXT')['href']
            soup = BeautifulSoup(requests.get(next_link).text, 'html.parser')

        if not soup.find('a', text='NEXT'):
            all_players = soup.find_all('tr',
            attrs={'class': ['oddrow', 'evenrow']})
            for player in all_players:
                stat_list.append(player.find_all('td'))

                #Removes the tags and leaves only the desired text.
                for n in range(0, len(stat_list[i])):
                    stat_list[i][n] = stat_list[i][n].get_text()
                i+=1
            break

    print stat_list
