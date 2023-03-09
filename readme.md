# Langchain Mysql

The purpose of this repo is to get a mysql database up and running in docker and make it queryable via langchain. 
Fortunately, langchain makes this very simple. 


## Requirements
OPENAI_API_KEY must be updated in export_key.sh

```
pip install -r requirements.txt     # install required packages

source export_key.sh                # export OPENAI_API_KEY

sh docker-build.sh                  # spin up mysql docker container

python setup_mysql.py               # setup mysql database and Sales table

python process.py                   # run some langchain queries
```
