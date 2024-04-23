# Rachel's Portfolio
This repo holds the code for my partners web portfolio.

The app directory stores the code for the website.
The flickr_api directory holds the code for uploading images to flickr. 
This is where we store the images used in the portfolio.

## Setup

Setting up the flickr API
```
mv flickr_api/config.ini.example flickr_api/config.ini
```
Request an api key and secret from [flickr](https://www.flickr.com/services/api/keys/apply/), use these to fill in config.ini.

## Running

Set up venv with the following commands:
```
python3 -m venv venv
source venv/bin/activate (Linux and MacOS) or .\venv\activate (Windows)
pip install -r requirements.txt
```

To run the portfolio, run the following commands:
```
cd app
flask run
```

To run the flickr app, run the following commands:
```
cd flickr_api
flask run
```