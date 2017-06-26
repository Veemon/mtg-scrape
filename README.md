# MTG-Scraper  
This is an image scraper for Magic The Gathering cards, scraping images from the gatherer website.
On a moderate connection this has been found to take approximately 15 minutes for 15'000 cards.

## File Descriptions  
### run.bat  
Basic run file for windows. Runs pre-req checks and executes all scripts.

#### init.py  
Initialises directory structure.

#### scrape.py
Defines a spider for scrapy that collects card ID's.

#### move.py  
Moves scraped ID CSV's to their respective color directories.

#### download.py  
Creates a multi-process downloader that downloads card images from the collected ID files.

## Disclaimer  
This is for educational resources. I am not responsible for any server damages that may occur.
