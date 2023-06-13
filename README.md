# Telegram Space

A collection of scripts designed to download images from SpaceX launches, NASA's [Astronomy Picture of the Day (APOD)](https://apod.nasa.gov/apod/astropix.html) and [Earth Polychromatic Imaging Camera (EPIC)](https://epic.gsfc.nasa.gov/)

## Installing

Download the project to your local machine.

Python3 should already be installed. 
Use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

Using virtual environment [virtualenv/venv](https://docs.python.org/3/library/venv.html) is recommended for project isolation.

Program can be run as is, however to increase NASA's hourly/daily requests limit, obtaining [NASA API Key](https://api.nasa.gov/#signUp) is recommended. 

Store it in .env file in root folder of the project as "NASA_TOKEN"
```
NASA_TOKEN = 'abc12defg345hi6gk78lmn9op012qrs345tuvw6xyz'
```

## Using the program

Currently, you need to manually edit main function in `main.py` to specify which images to download and their number.  
Run program when ready
```commandline
python3 main.py
```