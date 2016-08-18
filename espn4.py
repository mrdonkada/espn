import requests
from bs4 import BeautifulSoup

def leaders(stat):
    #Scrapes espn.com and returns a leaderboard of the desired statistic
    url = 'http://espn.go.com/mlb/stats/batting/_/qualified/true'
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')

    first_page = soup.find('a', text='TOP')['href']
    if url != first_page:
        url = first_page
        req = requests.get(URL)
        soup = BeautifulSoup(req.text, 'html.parser')
    else:
        pass

    #Saves the initial html code to a text file
    with open("espn_page.txt", "w") as initial_file:
        initial_file.write(str(soup))

    headers = soup.find('tr', attrs={'class':'colhead'})
    header_list = []
    for i in headers:
        header_list.append(i.get_text())

    print header_list

    stat_list = []
    i=0

    while soup.find('a', text='NEXT'):
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
    else:
        all_players = soup.find_all('tr',
        attrs={'class': ['oddrow', 'evenrow']})
        for player in all_players:
            stat_list.append(player.find_all('td'))

            #Removes the tags and leaves only the desired text.
            for n in range(0, len(stat_list[i])):
                stat_list[i][n] = stat_list[i][n].get_text()
            i+=1

    print stat_list
