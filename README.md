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

5. Install Chrome Web Driver
    - Get the latest Chrome web driver from https://sites.google.com/chromium.org/driver/downloads
    - Extract and move the binary to bin: 
      - For Linux `unzip chromedriver_linux64.zip -d .venv/bin/`
      - For Windows extract `chromedriver_win32.zip` to `.venv/bin/`
    - Make it executable `chmod +x .venv/bin/chromedriver`<br/><br/>