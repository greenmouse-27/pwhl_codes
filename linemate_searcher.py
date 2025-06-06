import pandas as pd

teamname = str(input('What team do you want to look at?:')).upper()

while teamname not in ['MINNESOTA','MN','MINNESOTA FROST','FROST','FORST','FRUST','BOSTON','BOS','FLEET','FREET','BOSTON FLEET','MONTREAL','MTL','VICTOIRE','MONTREAL VICTOIRE','VICTWAR','NEW YORK','NEW YORK SIRENS', 'NY','SIRENS', 'WEE WOOS','OTTAWA','OTT','OTTOWA','CHARGE','OTTAWA CHARGE','CHORGE','TORONTO','TOR','TORONTO SCEPTRES','SCEPTRES','SCEPTERS']:
    print('Sorry, I do not recognize that team name. Could you try again?')
    teamname = str(input('What team do you want to look at? Please enter Boston, Minnesota, Montreal, New York, Ottawa, or Toronto:')).upper()
    
if teamname in ['MINNESOTA','MN','MINNESOTA FROST','FROST','FORST','FRUST']:
    ds = pd.read_csv('MinnesotaFrost_test.csv')
    print('IN FROST WE FRUST')
elif teamname in ['BOSTON','BOS','FLEET','FREET','BOSTON FLEET']:
    ds = pd.read_csv('BostonFleet.csv')
    print('GO FLEET GO!')
elif teamname in ['MONTREAL','MTL','VICTOIRE','MONTREAL VICTOIRE','VICTWAR']:
    ds = pd.read_csv('MontrealVictoire.csv')
    print('ALLEZ LA VICTOIRE!')
elif teamname in ['NEW YORK','NEW YORK SIRENS', 'NY','SIRENS', 'WEE WOOS']:
    ds=pd.read_csv('NewYorkSirens.csv')
    print('WEE WOO!')
elif teamname in ['OTTAWA','OTT','OTTOWA','CHARGE','OTTAWA CHARGE','CHORGE']:
    ds = pd.read_csv('OttawaCharge.csv')
    print('GO CHARGE GO!')
elif teamname in ['TORONTO','TOR','TORONTO SCEPTRES','SCEPTRES','SCEPTERS']:
    ds=pd.read_csv('TorontoSceptres.csv')
    print('LET\'S GO T.O.!')
else:
    print('Sorry, I do not recognize that team name')
    quit

player_name = str(input('Enter player last name, with no accents:')).title()

if player_name == 'Mcmahon':
    player_name='McMahon'
if player_name == 'Mcquigge':
    player_name ='McQuigge'

playercount = ds['P1'].where(ds['P1']==player_name).dropna().count() + ds['P2'].where(ds['P2']==player_name).dropna().count() + ds['P3'].where(ds['P3']==player_name).dropna().count()
print(str(player_name)+' played '+str(playercount)+' times')

while playercount ==0:
    print('I don\'t recognize that name - could you check the spelling?')
    player_name = str(input('Enter player last name only, with no accents, and proper capitalization:'))
    playercount = ds['P1'].where(ds['P1']==player_name).dropna().count() + ds['P2'].where(ds['P2']==player_name).dropna().count() + ds['P3'].where(ds['P3']==player_name).dropna().count()
    print(str(player_name)+' played '+str(playercount)+' times')
    

linemates_counts = {}

linemates=[]

for position in ['P1','P2','P3']:
    for mate in ['P1','P2','P3']:
        if position!=mate:
            for player in ds[mate].where(ds[position]==player_name).dropna().values:
                if player not in linemates:
                    linemates.append(player)
                    linemates_counts[player]=1
                else:
                    linemates_counts[player]=linemates_counts[player]+1


print(linemates_counts)
if sum(linemates_counts.values())/playercount>1:
    linemates_times = sum(linemates_counts.values())/2
else:
    linemates_times = sum(linemates_counts.values())

print(str(player_name)+' was (probably) listed without linemates '+str(playercount - linemates_times)+' times')

linemates_counts={}
linemates=[]

are_you_done = 'no'
are_you_done = str(input('Do you want to add a second player? (yes/no):'))

if are_you_done in ['yes','YES','Yes']:
    player2_name = str(input('Enter second player last name:'))
    
    for position in ['P1','P2','P3']:
        for mate in ['P1','P2','P3']:
            for third in ['P1','P2','P3']:
                if position!=mate and position!=third and mate!=third:
                    for player in ds[third].where(ds[position]==player_name).dropna().where(ds[mate]==player2_name).dropna().values:
                        if player not in linemates:
                            linemates.append(player)
                            linemates_counts[player]=1
                        else:
                            linemates_counts[player]=linemates_counts[player]+1
                        
          
    print(linemates_counts)
