# Rainmail
A Windows Executable written in Python3 to scrape email addresses from country specific google search and keyword...
customizable to improve search results with python functions for specific tasks as different files.
***STILL UNDER DEVELOPMENT***

***Rainmail.exe not available yet***

***The full script Rainmail.py***

Python Dependencies #Python3

pip3 install GoogleScraper

pip3 install bs4 #beautifulsoup

pip3 install urllib3

pip3 install selenium


***On Windows***

On windows, you need to install some extensions manually: Lxml and Chromedriver:

**lxml**

Download the correct wheel file here: http://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml

Then copy the downloaded file in your python root directory: C:\Python34\Scripts
Then from this directory, issue the command in a cmd shell: pip install wheel_file.whl Of course the file has the name as it was downloaded.

**chromedriver**

Download the latest chromedriver from here: https://sites.google.com/a/chromium.org/chromedriver/downloads Then copy the chromedriver.exe in the C:\Python34\ directory.

Then go back to C:\Python34\Scripts\ and issue the command: pip install GoogleScraper
