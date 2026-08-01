# pwhl_codes
Codes for investigating and plotting PWHL data.

## linemates_search
Can tell you which other player(s) any player was most often listed as linemates with according to the lineups posted before games. Currently only covers 2024-2025 Regular season. Code written by Erin, posted lineups compiled by Arin of the PWHL Discord. 

## shot_data
Will generate plots of where average forwards and defenders are shooting and scoring from, as well as maps of how much more or less players shoot from a position than the average player at their position, how many goals a player is expected to score based on where they shoot from and league avgerage shooting percentages, and a player's shooting percentage above average by location.

This code uses data obtained via Lars Skytte's (hockey-statistics.com) web scraper for PWHL data. I used it to extract information on the most recent season (2025-2026 at time of writing) and have uploaded it in the .csv files in the shot_data folder.

# Instructions
You will need an installation of python with the pandas package. Anaconda is most often used for this (as the python installation) but there are lots of other ways to do it too. For the shot plotting codes, you will also need the matplotlib and [mplhockey](https://github.com/mlsedigital/mplhockey) packages. If you want to use the python script (as opposed to the Jupyter notebook) for shot plotting, which saves images, you will also need the unidecode package.

## Linemate searcher
in the linemates_search directory, run `python linemate_searcher.py` in the command line and follow the instructions. 

## Shot plotting
Both a jupyter notebook and a python script are included in the shot_data folder. The Jupyter notebook is recommended if you are familar with the format and want to fiddle with the settings yourself. The python script will generate and save a LOT of plots once that you can then peruse. 

# Future Work
- update lineups to include 2025 playoffs and 2025-2026 regular season and playoffs
- improve filtering of forward/defense status
- subdivide results by LW/RW/C/LD/RD (positional) information
- update shot plotter to grab most recent data from the PWHL site
