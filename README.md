# pwhl_codes
Codes for investigating and plotting PWHL data.

## linemates_search
Can tell you which other player(s) any player was most often listed as linemates with according to the lineups posted before games. Currently only covers 2024-2025 Regular season. Code written by Erin, posted lineups compiled by Arin of the PWHL Discord. 

# Instructions
You will need an installation of python with the pandas package. Anaconda is most often used for this (as the python installation) but there are lots of other ways to do it too. For the upcoming shot and xG plotting codes, you will need the matplotlib and [mplhockey](https://github.com/mlsedigital/mplhockey) packages.

## Linemate searcher
in the linemates_search directory, run `python linemate_searcher.py` in the command line and follow the instructions. 

# Future Work
- update lineups to include 2025 playoffs and 2025-2026 regular season and playoffs
- improve filtering of forward/defense status
- subdivide results by LW/RW/C/LD/RD (positional) information
- upload shot plotter and (verrry) rudimenary xG plotter