# dota2stats
Analyze hero win/loss data to determine the "best" heroes from a data set. Can parse datdota and dotabuff table data.

This program can be used to easily analyze the hero results from any given Dota2 tournament, or similar data set.
It will display all heroes in ranked order, as well as which heroes went unpicked in the given data set.

Thanks to [How Not To Sort By Average Rating](http://www.evanmiller.org/how-not-to-sort-by-average-rating.html) for the formula and idea.

Instructions:

1. Copy and paste tabular data from a Dotabuff or Datdota tournament page. [Dotabuff Example](), [DatDota Example](http://www.datdota.com/tournament.php?q=451&tournament=The%20International%202015&p=heroes). Ensure that you start with the hero name column and end with the Win Percent or Losses column, respectively. In Firefox, you can do this by holding Control (or Cmd on OSX) and dragging to select. Chrome requires an [add-on found here](https://chrome.google.com/webstore/detail/copytables/ekdpkppgmlalfkphpibadldikjimijon?hl=en).
2. Paste this data into a text file in the same folder of the program, and save it.
3. Run one of the two executable programs: `dotabuff_sort.py` or `datdota_sort.py`, and give it the filename! You can use [PyCharm](https://www.jetbrains.com/pycharm/download/), which is free and fully cross platform. Or, if you're on Linux or OSX, simply use the terminal.
4. Results should print out to your screen.
