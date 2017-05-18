# Projects
2017 Data Machines Intern Projects

## RSS Feed Reader
Write python code to parse an RSS feed (i.e. the US-Cert security advisory feed) and run a regex (i.e. search for 'cisco') and push to slack (i.e. #security). Alternatively, it should be able to archive the feed to json. Should just be a few lines of code. 

## Scrapy fix
Write scrapy code that reliabily grabs a list of urls, runs them through python-goose, and outputs the data to json. Must fully support utf-8 and also output a list of urls it failed to fetch and why it failed. 

## Ansible all the STIGS
Take the security guidance from NIST SP-800-53 and derivative manuals and find or write idempotent ansible code to implement or audit the controls. Create a coherent project that allows us to select which controls to implement based on risk guidance in SP-800-171.

## Write a darkweb scraper
Write code to index .onion sites. Note: pick a specific .onion that is good for scraping and use that as initial target and test case. Don't venture beyond this specific .onion to avoid downloading illegal data. 

## Wrap Moses Machine Translation software in a REST API using Python Flask
Germanic language translation is fine for now. Matecat as a baseline/example? Should have a simple user interface as well. 

## Crypto-currency transaction database
Set up Abe (https://github.com/bitcoin-abe/bitcoin-abe) or similar to start logging transactions into a database for BitCoin. Do this for as many currencies as possible. Fine if also logs to disk via json. Make the process repeatable. Provide a REST API via Python Flask that allows querying of the database with a cryptocurency address and returns transactions involving that address. 

## Crypto-currency identity database
Write a web scraper that searches the web for cryptocurrency addresses, correctly identifies which currency they belong to (either through address heuristics or NLP) and associates them with an identity (via entity extraction) or website (just grab the url). 

## Web based crontab manager
Manage cron tasks via an intuitive and easy to use web page. A master scheduler. An optimal solution would allow tasks to be restricted by ldap user groups mapped to CRUD operations.
