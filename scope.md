# eBay price scraper

lets create a python program that returns the last few sold item prices on ebay for a given search term. For now we will keep it terminal based but next video lets turn it into a flask app.

* take a search term
* return X amount of SOLD listings
* auctions only
* scrape prices, date, bids, title
* save to a database

## notes

searchterm is a partial match. to make sure it is exactly what we want add in a function that matches the search term to resulting dictionary and remove unwated items.

* use ' ' to target search more

