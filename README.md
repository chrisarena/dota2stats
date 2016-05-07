# dota2stats
Analyze hero win/loss data to determine the "best" heroes from a data set. Can parse datdota and dotabuff table data.

This program can be used to easily analyze the hero results from any given Dota2 tournament, or similar data set.
It will display all heroes in ranked order, as well as which heroes went unpicked in the given data set.

Thanks to [How Not To Sort By Average Rating](http://www.evanmiller.org/how-not-to-sort-by-average-rating.html) for the formula and idea.

Instructions:

1. Copy and paste tabular data from a Dotabuff or Datdota tournament page. [Dotabuff Example](http://www.dotabuff.com/esports/leagues/4479/heroes), [DatDota Example](http://www.datdota.com/tournament.php?q=451&tournament=The%20International%202015&p=heroes). Ensure that you start with the hero name column and end with the Win Percent or Losses column, respectively. In Firefox, you can do this by holding Control (or Cmd on OSX) and dragging to select. Chrome requires an [add-on found here](https://chrome.google.com/webstore/detail/copytables/ekdpkppgmlalfkphpibadldikjimijon?hl=en).
2. Paste this data into a text file in the same folder of the program, and save it.
3. Run one of the two executable programs: `dotabuff_sort.py` or `datdota_sort.py`, and give it the filename! You can use [PyCharm](https://www.jetbrains.com/pycharm/download/), which is free and fully cross platform. Or, if you're on Linux or OSX, simply use the terminal.
4. Results should print out to your screen.


How it works:

What this program does is create a normal distribution around each hero's win rate that most likely contains their "actual" win rate, if infinite games were played. The more data it has (number of games with that hero), the narrower it's able to make the distribution (in technical terms, by lowering the standard deviation), while still being just as sure that it's correct (by default, like most statistics, 95% sure). The decimal number is the farthest leftmost point of the distribution for that hero's winrate. So, it's the winrate that I'm 97.5% sure a hero's actual winrate is GREATER than.

Here's a good graphical depiction of that:

![Image of Normal Distributions](https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Normal_Distribution_PDF.svg/350px-Normal_Distribution_PDF.svg.png)

The yellow, red, and blue curves have the same center (mean value), so they might indicate a hero who went 2-2, a hero who went 10-10, and a hero who went 40-40, respectively. As we get more data, the curve becomes narrower, but keeps the same mean. The green curve (which has a lower mean) might indicate a hero who went 10-20. Doing below-average shifts it to the left, just like doing above-average would shift it to the right. If we take each of those curves and go two standard deviations left on the x-axis from their mean (two σ being ~95% confidence in our result), that value on the curve is our decimal value.

This gives a pessimistic evalution, which accomplishes the same goal as setting a "minimum number of games" in order to be counted, but without needing to exclude heroes who haven't been played much- they're just naturally lower.
