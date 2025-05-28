# My spider
 This scrapy spider helps us for download the articles from all tabs of the www.kaldata.com
 site. It covers only the last 3 pages of all tabs. All collected data is stored
 in the Sqlite3 database.

# Requirements
 Python 3.12 - I am using Python 3.12 version on my computer.<br />
 Sqlite3 - Sqlite3 was used as the database for the data we extracted.<br />
 Requests<br />
 pip 24.2 - my pip version is 24.2<br />
 
 scrapy 2.11.2 <br />
<ins>Usage:</ins><br />
 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &nbsp; &nbsp; scrapy < command> [options] [args]<br />
<ins>Available commands:</ins><br />
 bench&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Run quick benchmark test<br />
 check&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Check spider contracts<br />
 crawl&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Run a spider<br />
 edit&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Edit spider<br />
 fetch&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Fetch a URL using the Scrapy downloader<br />
 genspider&nbsp; &nbsp; &nbsp; &nbsp; Generate new spider using pre-defined templates<br />
 list&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; List available spiders<br />
 parse&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Parse URL (using its spider) and print the results<br />
 runspider&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Run a self-contained spider (without creating a project)<br />
 settings&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Get settings values<br />
 shell&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Interactive scraping console<br />
 startproject&nbsp; &nbsp; &nbsp; &nbsp;Create new project<br />
 version&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Print Scrapy version<br />
 view&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Open URL in browser, as seen by Scrapy<br />
<br />
 Use "scrapy <command> -h" to see more info about a command

 jsonschema 4.23.0 - We validate the data type by comparing the content.json and content-validation.json files<br />

 To work properly we need to set ROBOTSTXT_OBEY to false in the settings.py file.

# Thanks
 Feel free to leave a comment and know that I am open to criticism. I hope my project did not waste your time.
