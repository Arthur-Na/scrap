================================ scrap project ================================

Web scraping with a spider for rakuten.jp site for get data on luxury bags
get the data of the number of pages asked or all and store then in a json file.

scraper in python using scrapy library

================================ How to use it ================================

PS1$ pip install scrapy
// or refer to there web site for futher information

PS1$ cd scrap/rakuten
PS1$ scrapy crawl rakuten_jp_bags -o [output_file].json [-a nb_page=[:digit:]]
