# goat_book

## Prepare

Set python env  
````bash
apt install python3-venv
python -m venv venv
````

Active python env and install dependance  
````bash
. venv/bin/active
pip install -r requiremest.txt
pip install selenium
````


## Test
Test django locally
````bash
cd src
pyton manage.py test 
````

## Build images
Build superlists images
````bash
cd ../
docker build -t superlists .

docker run -p 8888:8888 -it superlists

````

## Test in docker
````bash
cd src
TEST_SERVER=http://localhost:8888 pyton manage.py test 
````



