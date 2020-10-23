from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import pandas as pd

#using the url to connect to the website
page_url = "https://www.iplt20.com/stats/2020/player-points"
uClient = uReq(page_url)

#using beautiful soup to parse the webpage to read
page_soup = soup(uClient.read(), "html.parser")

#inspecting the website html elments and grbbing the top player names
container1 = page_soup.findAll("div", {"class": "top-players__player-name"})

#removing all other symbols except the player name
player_list = []
for play in container1:
    player_list.append(play.text.replace('\n', '').strip())

player_names = []
for names in player_list:
    remove_inbetween_spaces = " ".join(names.split())
    player_names.append(remove_inbetween_spaces)

#saving the player name in a dataframe
df = pd.DataFrame(player_names,columns ={'Player Name'})

#retrieving their corresponding score and typecasting str to float
container2 = page_soup.findAll("td", {"class": "top-players__pts top-players__padded is-active"})

points_list = []
for points in container2:
    points_list.append(points.text.replace('\n', '').strip())

points_list = [float(i) for i in points_list]

df['Points'] = pd.DataFrame(points_list)

# multiplying scores for captain 2x and vc 1.5x
def score_multiplier(captain,vice_captain,team_df):
    cap_index = team_df.index[team_df['Player Name'] == captain]
    vice_cap_index = team_df.index[team_df['Player Name'] == vice_captain]
    team_df.loc[cap_index, 'Points'] = team_df.loc[cap_index, 'Points'] * 2
    team_df.loc[cap_index, 'Player Name'] = captain + ' (C)'
    team_df.loc[vice_cap_index, 'Points'] = team_df.loc[vice_cap_index, 'Points'] * 1.5
    team_df.loc[vice_cap_index, 'Player Name'] = vice_captain + ' (VC)'
    return team_df

def play_replace(player_replace,replace_df,points):
    replace_index = replace_df.index[replace_df['Player Name'] == player_replace]
    replace_df.loc[replace_index, 'Points'] = replace_df.loc[replace_index, 'Points'] - points
    replace_df.loc[replace_index, 'Player Name'] = player_replace + ' (Replaced)'
    return replace_df

def add_ruled_out(player_name,player_df):
    ruled_index = player_df.index[player_df['Player Name'] == player_name]
    player_df.loc[ruled_index, 'Player Name'] = player_name + ' (Ruled out)'
    return player_df

#checking the team players and saving in different data frame
team1 = ['Virat Kohli','KL Rahul','Trent Boult','Nicholas Pooran',
         'Ravi Bishnoi','Navdeep Saini','Pat Cummins','Eoin Morgan',
         'Murali Vijay','Avesh Khan','Krishnappa Gowtham']
team1_df = df[df['Player Name'].isin(team1)]

team1_multi = score_multiplier('Virat Kohli','KL Rahul',team1_df)
df1 = {'Player Name':'Total Score','Points':team1_multi['Points'].sum()}
team1_points = team1_multi.append(df1,ignore_index=True,sort=False)




team2 = ['Steve Smith','Yuzvendra Chahal','Dwayne Bravo','Shreyas Iyer',
         'Mujeeb Ur Rahman','Suryakumar Yadav','Kedar Jadhav','Piyush Chawla',
         'Aaron Finch','Parthiv Patel','Mayank Markande','Chris Morris']
team2_df = df[df['Player Name'].isin(team2)]

team2_multi = score_multiplier('Yuzvendra Chahal','Shreyas Iyer',team2_df)
team2_replace = play_replace('Chris Morris',team2_df,117.5)
team2_ruled_out = add_ruled_out('Dwayne Bravo',team2_df)
df2 = {'Player Name':'Total Score','Points':team2_multi['Points'].sum()}
team2_points = team2_multi.append(df2,ignore_index=True,sort=False)



team3 = ['Sunil Narine','Kane Williamson','Chris Lynn','Kieron Pollard',
         'Krunal Pandya','Deepak Chahar','Ajinkya Rahane','Robin Uthappa',
         'Bhuvneshwar Kumar','Siddarth Kaul','Rahul Tripathi','Shivam Mavi']
team3_df = df[df['Player Name'].isin(team3)]
team3_multi = score_multiplier('Kieron Pollard','Kane Williamson',team3_df)
team3_replace = play_replace('Shivam Mavi',team3_df,52.5)
team3_ruled_out = add_ruled_out('Bhuvneshwar Kumar',team3_df)
df3 = {'Player Name':'Total Score','Points':team3_multi['Points'].sum()}
team3_points = team3_multi.append(df3,ignore_index=True,sort=False)


team4=['Rishabh Pant','David Warner','Imran Tahir','Shubman Gill',
       'Shreyas Gopal','Sandeep Sharma','Vijay Shankar','Moeen Ali',
       'Shimron Hetmyer','Ishant Sharma','Sarfaraz Khan','Varun Chakravarthy']
team4_df = df[df['Player Name'].isin(team4)]
team4_multi = score_multiplier('David Warner','Rishabh Pant',team4_df)
team4_replace = play_replace('Varun Chakravarthy',team4_df,59)
team4_ruled_out = add_ruled_out('Ishant Sharma',team4_df)
df4 = {'Player Name':'Total Score','Points':team4_multi['Points'].sum()}
team4_points = team4_multi.append(df4,ignore_index=True,sort=False)


team5 = ['Ravindra Jadeja','MS Dhoni','Ambati Rayudu','Sheldon Cottrell',
         'Jonny Bairstow','Kuldeep Yadav','Shane Watson','Jaydev Unadkat',
         'Jos Buttler','Manish Pandey','Karn Sharma']
team5_df = df[df['Player Name'].isin(team5)]

team5_multi = score_multiplier('Jos Buttler','MS Dhoni',team5_df)

df5 = {'Player Name':'Total Score','Points':team5_multi['Points'].sum()}
team5_points = team5_multi.append(df5,ignore_index=True,sort=False)

team6=['Andre Russell','Hardik Pandya','Quinton de Kock','Shikhar Dhawan',
       'Marcus Stoinis','Deepak Hooda','Mohammad Shami','Mohammad Nabi',
       'Karun Nair','Manan Vohra','Wriddhiman Saha']
team6_df = df[df['Player Name'].isin(team6)]

team6_multi = score_multiplier('Andre Russell','Hardik Pandya',team6_df)
df6 = {'Player Name':'Total Score','Points':team6_multi['Points'].sum()}
team6_points = team6_multi.append(df6,ignore_index=True,sort=False)

team7 = ['Rohit Sharma','Ben Stokes','Jasprit Bumrah','Ishan Kishan',
         'Sam Curran','Prithvi Shaw','Glenn Maxwell',
         'Jofra Archer','Sanju Samson','Shivam Dube','Washington Sundar']
team7_df = df[df['Player Name'].isin(team7)]

team7_multi = score_multiplier('Rohit Sharma','Glenn Maxwell',team7_df)
df7 = {'Player Name':'Total Score','Points':team7_multi['Points'].sum()}
team7_points = team7_multi.append(df7,ignore_index=True,sort=False)

team8 =['AB de Villiers','Chris Gayle','Kagiso Rabada','Ravichandran Ashwin','Nitish Rana',
       'Dinesh Karthik','Rashid Khan','Shardul Thakur','Mayank Agarwal','Umesh Yadav','Kamlesh Nagarkoti']
team8_df = df[df['Player Name'].isin(team8)]

team8_multi = score_multiplier('Dinesh Karthik','Nitish Rana',team8_df)
df8 = {'Player Name':'Total Score','Points':team8_multi['Points'].sum()}
team8_points = team8_multi.append(df8,ignore_index=True,sort=False)

#total points for each teams
data = [df1['Points'],df2['Points'],df3['Points'],df4['Points'],
        df5['Points'],df6['Points'],df7['Points'],df8['Points']]

team_names = ['Pitch Smashers','Groundbreakers','Blazing Strikers','Kingsguard',
              'DOMinatorS','Dragon Hearts','Team 7','Team 8']
df_table = {'Team Name':team_names,'Scores':data}

#teams scores and standing
standing = pd.DataFrame(df_table).sort_values(by='Scores',ascending=False)

print(standing)