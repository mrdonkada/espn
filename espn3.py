def leaders3(stat):
    #Scrapes th ESPN leadeerboards for players' batting averages
    URL = 'http://espn.go.com/mlb/stats/batting/_/qualified/true'
    req = requests.get(URL)
    soup = BeautifulSoup(req.text, 'html.parser')

    first_page = soup.find('a', text='TOP')['href']
    if URL != first_page:
        URL = first_page
        req = requests.get(URL)
        soup = BeautifulSoup(req.text, 'html.parser')
    else:
        pass

    #Creates a file with the initial html code of the page
    with open("espn_page.txt", "w") as initial_file:
        initial_file.write(str(soup))

    stat_list = []
    i=0

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

    class MyError(Exception):
        def __init__(self, value):
            self.value = value
        def __str__(self):
            return repr(self.value)

    if stat == "AB":
        with open("leaderboard.txt", "w") as my_file:
            my_file.write("Name,Team,AB" + "\n")
            for j in range(len(stat_list)):
                player = stat_list[j][1]
                team = stat_list[j][2]
                ab = stat_list[j][3]
                my_file.write(
                player + "," +
                team + "," +
                ab + "\n"
                )

    elif stat == "R":
        with open("leaderboard.txt", "w") as my_file:
            my_file.write("Name,Team,R" + "\n")
            for j in range(len(stat_list)):
                player = stat_list[j][1]
                team = stat_list[j][2]
                r = stat_list[j][4]
                my_file.write(
                player + "," +
                team + "," +
                r + "\n"
                )

    elif stat == "H":
        with open("leaderboard.txt", "w") as my_file:
            my_file.write("Name,Team,H" + "\n")
            for j in range(len(stat_list)):
                player = stat_list[j][1]
                team = stat_list[j][2]
                h = stat_list[j][5]
                my_file.write(
                player + "," +
                team + "," +
                h + "\n"
                )

    elif stat == "2B":
        with open("leaderboard.txt", "w") as my_file:
            my_file.write("Name,Team,2B" + "\n")
            for j in range(len(stat_list)):
                player = stat_list[j][1]
                team = stat_list[j][2]
                doubles = stat_list[j][6]
                my_file.write(
                player + "," +
                team + "," +
                doubles + "\n"
                )

    elif stat == "3B":
        with open("leaderboard.txt", "w") as my_file:
            my_file.write("Name,Team,3B" + "\n")
            for j in range(len(stat_list)):
                player = stat_list[j][1]
                team = stat_list[j][2]
                triples = stat_list[j][7]
                my_file.write(
                player + "," +
                team + "," +
                triples + "\n"
                )

    elif stat == "HR":
        with open("leaderboard.txt", "w") as my_file:
            my_file.write("Name,Team,HR" + "\n")
            for j in range(len(stat_list)):
                player = stat_list[j][1]
                team = stat_list[j][2]
                hr = stat_list[j][8]
                my_file.write(
                player + "," +
                team + "," +
                hr + "\n"
                )

    elif stat == "RBI":
        with open("leaderboard.txt", "w") as my_file:
            my_file.write("Name,Team,RBI" + "\n")
            for j in range(len(stat_list)):
                player = stat_list[j][1]
                team = stat_list[j][2]
                rbi = stat_list[j][9]
                my_file.write(
                player + "," +
                team + "," +
                rbi + "\n"
                )

    elif stat == "SB":
        with open("leaderboard.txt", "w") as my_file:
            my_file.write("Name,Team,SB" + "\n")
            for j in range(len(stat_list)):
                player = stat_list[j][1]
                team = stat_list[j][2]
                sb = stat_list[j][10]
                my_file.write(
                player + "," +
                team + "," +
                sb + "\n"
                )

    elif stat == "CS":
        with open("leaderboard.txt", "w") as my_file:
            my_file.write("Name,Team,CS" + "\n")
            for j in range(len(stat_list)):
                player = stat_list[j][1]
                team = stat_list[j][2]
                cs = stat_list[j][11]
                my_file.write(
                player + "," +
                team + "," +
                cs + "\n"
                )

    elif stat == "BB":
        with open("leaderboard.txt", "w") as my_file:
            my_file.write("Name,Team,CS" + "\n")
            for j in range(len(stat_list)):
                player = stat_list[j][1]
                team = stat_list[j][2]
                bb = stat_list[j][12]
                my_file.write(
                player + "," +
                team + "," +
                bb + "\n"
                )

    elif stat == "SO":
        with open("leaderboard.txt", "w") as my_file:
            my_file.write("Name,Team,SO" + "\n")
            for j in range(len(stat_list)):
                player = stat_list[j][1]
                team = stat_list[j][2]
                so = stat_list[j][13]
                my_file.write(
                player + "," +
                team + "," +
                so + "\n"
                )

    elif stat == "AVG":
        with open("leaderboard.txt", "w") as my_file:
            my_file.write("Name,Team,AVG" + "\n")
            for j in range(len(stat_list)):
                player = stat_list[j][1]
                team = stat_list[j][2]
                avg = stat_list[j][14]
                my_file.write(
                player + "," +
                team + "," +
                avg + "\n"
                )

    elif stat == "OBP":
        with open("leaderboard.txt", "w") as my_file:
            my_file.write("Name,Team,OBP" + "\n")
            for j in range(len(stat_list)):
                player = stat_list[j][1]
                team = stat_list[j][2]
                obp = stat_list[j][15]
                my_file.write(
                player + "," +
                team + "," +
                obp + "\n"
                )

    elif stat == "SLG":
        with open("leaderboard.txt", "w") as my_file:
            my_file.write("Name,Team,SLG" + "\n")
            for j in range(len(stat_list)):
                player = stat_list[j][1]
                team = stat_list[j][2]
                slg = stat_list[j][16]
                my_file.write(
                player + "," +
                team + "," +
                slg + "\n"
                )

    elif stat == "OPS":
        with open("leaderboard.txt", "w") as my_file:
            my_file.write("Name,Team,OPS" + "\n")
            for j in range(len(stat_list)):
                player = stat_list[j][1]
                team = stat_list[j][2]
                ops = stat_list[j][17]
                my_file.write(
                player + "," +
                team + "," +
                ops + "\n"
                )

    elif stat == "WAR":
        with open("leaderboard.txt", "w") as my_file:
            my_file.write("Name,Team,WAR" + "\n")
            for j in range(len(stat_list)):
                player = stat_list[j][1]
                team = stat_list[j][2]
                war = stat_list[j][18]
                my_file.write(
                player + "," +
                team + "," +
                war + "\n"
                )

    elif stat == "all":
        with open("leaderboard.txt", "w") as my_file:
            my_file.write("Name,Team,AB,R,H,2B,3B,HR,RBI,SB,CS,BB,SO,AVG,OBP,SLG,OPS,WAR" + "\n")
            for j in range(len(stat_list)):
                player = stat_list[j][1]
                team = stat_list[j][2]
                ab = stat_list[j][3]
                r = stat_list[j][4]
                h = stat_list[j][5]
                doubles = stat_list[j][6]
                triples = stat_list[j][7]
                hr = stat_list[j][8]
                rbi = stat_list[j][9]
                sb = stat_list[j][10]
                cs = stat_list[j][11]
                bb = stat_list[j][12]
                so = stat_list[j][13]
                avg = stat_list[j][14]
                obp = stat_list[j][15]
                slg = stat_list[j][16]
                ops = stat_list[j][17]
                war = stat_list[j][18]
                my_file.write(
                player + "," +
                team + "," +
                ab + "," +
                r + "," +
                h + "," +
                doubles + "," +
                triples + "," +
                hr + "," +
                rbi + "," +
                sb + "," +
                cs + "," +
                bb + "," +
                so + "," +
                avg + "," +
                obp + "," +
                slg + "," +
                ops + "," +
                war + "\n"
                )

    else:
        raise MyError("Sorry, I can't accept that. Have you tried all caps?")

    print stat_list
