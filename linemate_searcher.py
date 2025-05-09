import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

teamname = str(input('What team do you want to look at? I recognize most forms/combinations of team and city names:')).upper()

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
    print('GO T.O.!')
else:
    print('Sorry, I do not recognize that team name')
    quit
# print(ds)

player_name = str(input('Enter player last name, with no accents:')).title()
playercount = ds['P1'].where(ds['P1']==player_name).dropna().count() + ds['P2'].where(ds['P2']==player_name).dropna().count() + ds['P3'].where(ds['P3']==player_name).dropna().count()
print(str(player_name)+' played '+str(playercount)+' times')

# print(ds[ds.applymap(lambda x: x == player_name).any(axis=1)])

linemates_counts = {}

linemates=[]

for player in ds['P2'].where(ds['P1']==player_name).dropna().values:
    if player not in linemates:
        linemates.append(player)
        linemates_counts[player]=1
    else:
        linemates_counts[player]=linemates_counts[player]+1 

for player in ds['P3'].where(ds['P1']==player_name).dropna().values:
    if player not in linemates:
        linemates.append(player)
        linemates_counts[player]=1
    else:
        linemates_counts[player]=linemates_counts[player]+1 
        
for player in ds['P1'].where(ds['P2']==player_name).dropna().values:
    if player not in linemates:
        linemates.append(player)
        linemates_counts[player]=1
    else:
        linemates_counts[player]=linemates_counts[player]+1 
        
for player in ds['P3'].where(ds['P2']==player_name).dropna().values:
    if player not in linemates:
        linemates.append(player)
        linemates_counts[player]=1
    else:
        linemates_counts[player]=linemates_counts[player]+1 

for player in ds['P1'].where(ds['P3']==player_name).dropna().values:
    if player not in linemates:
        linemates.append(player)
        linemates_counts[player]=1
    else:
        linemates_counts[player]=linemates_counts[player]+1 

for player in ds['P2'].where(ds['P3']==player_name).dropna().values:
    if player not in linemates:
        linemates.append(player)
        linemates_counts[player]=1
    else:
        linemates_counts[player]=linemates_counts[player]+1

print(linemates_counts)

linemates_counts={}
linemates=[]

are_you_done = 'no'
are_you_done = str(input('Do you want to add a second player? (yes/no):'))

if are_you_done in ['yes','YES','Yes']:
    player2_name = str(input('Enter second player last name:')).title()
    
    for player in ds['P3'].where(ds['P1']==player_name).dropna().where(ds['P2']==player2_name).dropna().values:
        if player not in linemates:
            linemates.append(player)
            linemates_counts[player]=1
        else:
            linemates_counts[player]=linemates_counts[player]+1
            
    for player in ds['P3'].where(ds['P2']==player_name).dropna().where(ds['P1']==player2_name).dropna().values:
        if player not in linemates:
            linemates.append(player)
            linemates_counts[player]=1
        else:
            linemates_counts[player]=linemates_counts[player]+1
    
    for player in ds['P2'].where(ds['P1']==player_name).dropna().where(ds['P3']==player2_name).dropna().values:
        if player not in linemates:
            linemates.append(player)
            linemates_counts[player]=1
        else:
            linemates_counts[player]=linemates_counts[player]+1
            
    for player in ds['P2'].where(ds['P3']==player_name).dropna().where(ds['P1']==player2_name).dropna().values:
        if player not in linemates:
            linemates.append(player)
            linemates_counts[player]=1
        else:
            linemates_counts[player]=linemates_counts[player]+1
    
    for player in ds['P1'].where(ds['P2']==player_name).dropna().where(ds['P3']==player2_name).dropna().values:
        if player not in linemates:
            linemates.append(player)
            linemates_counts[player]=1
        else:
            linemates_counts[player]=linemates_counts[player]+1
            
    for player in ds['P1'].where(ds['P3']==player_name).dropna().where(ds['P2']==player2_name).dropna().values:
        if player not in linemates:
            linemates.append(player)
            linemates_counts[player]=1
        else:
            linemates_counts[player]=linemates_counts[player]+1
            
    print(linemates_counts)
