# EonTest
Part two of Eon Labs coding test

*You must have pandas, pathlib, and pytrends libraries installed on your computer for this code to work.*

1. The idea behind this challenge was relatively simple (especially considering the hint provided).
I've had plenty of experience in gathering data online so I knew the pytrends library would be
the library to use for this task. I knew I could use keywords and dates with pytrends and outsource the
findings to a csv file using pandas. So, I started by importing those.

2. all in all, the code probably took me 30 minutes to finish since the pytrends library is straight forward.

3. There is another way to complete this task and that would be to use the Google trends API, but this would have
only introduced more challenges into the solution. So, I went with the most efficient solution and used the pytrends
library.

4. I settled on the current approach because of it's efficiency. It's also a much more simple implementation of a
solution considering the guts of the code are hidden in the library.

5. To run this file, you must download the python file on your own computer and have python3 installed. Once downloaded, 
open your command line/terminal and call python3 followed by the name of the python file. i.e. "python3 Eon.py". Once run,
there should be a new csv file saved to the same directory as the "Eon.py" file. This is a two column csv file consisting of
the dates and frequency of bitcoin searches across Google.
