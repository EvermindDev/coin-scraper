# Coin Scraper

## Installation
1. Clone:
   `git clone https://github.com/Oare/coin-scraper.git`    
    or download the [zip](https://github.com/Oare/coin-scraper/archive/refs/heads/main.zip)<br/><br/>

2. Create Virtual Environment<br/> 
    - `pip install virtualenv`
    - `virtualenv .venv`<br/><br/>

3. Activate the virtual environment<br/>
    - `source .venv/bin/activate`<br/><br/>

4. Install dependencies<br/>
    - `pip install -r requirements.txt`<br/><br/>

5. Configuration. Copy config.cfg.example to config.cfg
   - `cp config.cfg.example config.cfg`

## Usage
   - Run `app.py` file from IDE <br/>
   or from command line <br/>
   - `python -m app`

## Analyzer and statistics
### To configure the analyzer mode, in `config.cfg` edit `mode` parameter
    - disabled: Data analysis will be skipped, and no statistical data will be displayed.
    - scrape-analyze: This mode will scrape the data again, perform analysis, and display statistics.
    - analysis: This mode will analyze the existing data and display statistics.

    - you can modify the historical data range by adjusting the `historical_time_range` parameter.


### Here is an example of the output statistics displayed on the console
![Screenshot](assets/statistic.png)

## Deactivation
   Deactivate the virtual environment
      - `source .venv/bin/deactivate`