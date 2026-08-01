# -*- coding: utf-8 -*-
from mplhockey import PWHLRink
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from unidecode import unidecode

plt.rcParams['figure.dpi'] = 200

def get_SHAA(ps,pg,ts,tg):
    shaa = pg/ps-tg/ts
    return shaa

def get_SP(ps,ts):
    sp = np.divide(ps,ps.sum()) - np.divide(ts,ts.sum())
    return sp

#this is not really xG but the PWHL doesn't have nearly as much data available as the NHL
#it's what we're got so far
def get_xG(ps,ts,tg):
    xG = ps*tg/ts
    return xG

ds = pd.read_csv('./PBP_PWHL_20252026_shots.csv')
players = pd.read_csv('./PWHL_Playerdata_2.csv')
rink = PWHLRink(units='m')

##convert PWHL shot location data to the axes that mplhockey expects
ds['xLocation']=ds['xLocation']/10-30
ds['yLocation']=ds['yLocation']/10-15

#make some plotting grids
x_grid = np.linspace(0,30,31)
y_grid = np.linspace(-13,13,27)

X,Y = np.meshgrid(x_grid,y_grid)
posns = np.vstack([X.ravel(),Y.ravel()])

# PWHL data has some errors in it: 
# notably the left-to-right shot position information is swapped from normal cartesian coordinates
# this section deals with that and puts all shots on the same side of the centre line as the net being shot at
# future work: filter out any shots that actually were taken from behind centre (e.g. some empty net goals)
ds2=ds
for loc in ds['xLocation'].index:
    if ds['xLocation'][loc]<0:
        ds2['xLocation'][loc] = -1*ds['xLocation'][loc]
    else:
        ds2['yLocation'][loc] = -1*ds['yLocation'][loc]

ds2 = ds2[['Shooter','xLocation','yLocation','shotQuality']].dropna()

shotquality_dict = {
    'Quality goal':1,
    'Non quality goal':1,
    'Quality on net':2,
    'Non quality on net':2}

#give shot quality irrespective of goal status a numerical value
#not currently in use but when multiple years of data are included might be able to filter by this
ds2['shotQuality_num'] = [shotquality_dict[i] for i in ds2['shotQuality']]

#edit this to try different bin sizes for the 2D histogram
bins = 6

# up the min_shots number if you want only players with more robust numbers
min_shots = 10
plot_types = ['SHAA','SP','xG']
posn_dict={
    'F':'forward',
    'D':'defender'
}

# loop through players that meet the criteria above and save plots of their shots!
for POSN in ['F','D']:
    list_of_posn_players = players.loc[players['pos']==POSN]['PlayerID'].values
    ds3 = ds2.loc[ds2['Shooter'].isin(list_of_posn_players)]
    ds4 = ds3.loc[ds3['shotQuality'].isin(['Quality goal','Non quality goal'])]  
    
    fig, ax = plt.subplots()
    rink.draw(ax=ax,display_range='ozone')
    ax.set_axis_off()
    totalshots, xedges, yedges, image = plt.hist2d(ds3['xLocation'],ds3['yLocation'],bins=bins,alpha=0.5,range=[[0, 30.5], [-13, 13]],cmap='Greens')
    plt.colorbar(label='# '+posn_dict[POSN]+' shots from grid cell')
    plt.title(posn_dict[POSN]+' shot location frequency')
    plt.savefig('./Figures/'+posn_dict[POSN]+'_average_shot_location.png')
    
    fig, ax = plt.subplots()
    rink.draw(ax=ax,display_range='ozone')
    ax.set_axis_off()
    totalgoals, xedges2, yedges2, image2 = plt.hist2d(ds4['xLocation'],ds4['yLocation'],bins=bins,alpha=0.5,range=[[0, 30.5], [-13, 13]],cmap='Blues')
    plt.colorbar(label='# '+posn_dict[POSN]+' goals from grid cell')
    plt.title(posn_dict[POSN]+' goal location frequency')
    plt.savefig('./Figures/'+posn_dict[POSN]+'_average_goal_location.png')
    
    for playerid in ds3['Shooter'].unique():
        if ds3.where(ds3['Shooter']==playerid).dropna().count()['Shooter']>min_shots and players.where(players['PlayerID']==playerid).count()['PlayerID']>0: 
            playershots, xedges1, yedges1, = np.histogram2d(ds3.where(ds['Shooter']==playerid).dropna()['xLocation'],ds3.where(ds['Shooter']==playerid).dropna()['yLocation'],bins=bins,range=[[0, 30.5], [-13, 13]])
            playergoals, xedges3, yedges3, = np.histogram2d(ds4.where(ds['Shooter']==playerid).dropna()['xLocation'],ds4.where(ds['Shooter']==playerid).dropna()['yLocation'],bins=bins,range=[[0, 30.5], [-13, 13]])
    
            if 'xG' in plot_types:
                fig, ax = plt.subplots()
                rink.draw(ax=ax,display_range='ozone')
                ax.set_axis_off()
                im = ax.pcolormesh(xedges, yedges, get_xG(playershots,totalshots,totalgoals).T, alpha=0.5,cmap='Reds',vmin=0,vmax=4)
                fig.colorbar(im, ax=ax,label='xG')
                plt.title(players.where(players['PlayerID']==playerid).dropna()['Name'].values[0].split(" ",1)[-1]+' expected goals by shot location')
                plt.savefig('./Figures/'+unidecode(players.where(players['PlayerID']==playerid).dropna()['Name'].values[0].split(" ",1)[-1])+'_xG_2526.png')
    
            if 'SHAA' in plot_types:
                fig, ax = plt.subplots()
                rink.draw(ax=ax,display_range='ozone')
                ax.set_axis_off()
                im = ax.pcolormesh(xedges, yedges, get_SHAA(playershots,playergoals,totalshots,totalgoals).T,alpha=0.5, cmap='bwr',vmin=-0.3,vmax=0.3)
                fig.colorbar(im, ax=ax,label='SH% - avg SH%')
                plt.title(players.where(players['PlayerID']==playerid).dropna()['Name'].values[0].split(" ",1)[-1]+' SH%AA for a '+posn_dict[POSN])
                plt.savefig('./Figures/'+unidecode(players.where(players['PlayerID']==playerid).dropna()['Name'].values[0].split(" ",1)[-1])+'_SHAA_2526.png')
    
            if 'SP' in plot_types:
                fig, ax = plt.subplots()
                rink.draw(ax=ax,display_range='ozone')
                ax.set_axis_off()
                im = ax.pcolormesh(xedges, yedges, get_SP(playershots,totalshots).T,alpha=0.5, cmap='bwr',vmin=-0.15,vmax=0.15)
                fig.colorbar(im, ax=ax,label='player positional shooting preference, %pts')
                plt.title(players.where(players['PlayerID']==playerid).dropna()['Name'].values[0].split(" ",1)[-1]+' shot location vs avg '+posn_dict[POSN])
                plt.savefig('./Figures/'+unidecode(players.where(players['PlayerID']==playerid).dropna()['Name'].values[0].split(" ",1)[-1])+'_SP_2526.png')
    


