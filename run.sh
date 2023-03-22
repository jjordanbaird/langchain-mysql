#!/bin/bash

export OPENAI_API_KEY=$1

if [ -z "$OPENAI_API_KEY" ]
then
      echo "\OPENAI_API_KEY cannot be empty, usage: run.sh <openai api key>"
else
    if [ -d "venv" ] 
    then
        source venv/bin/activate
    else
        python -m venv venv
        source venv/bin/activate 
        pip install -r requirements.txt
    fi 

    python setup_mysql.py

    docker run --name mysql-langchain-container \
        -v $(pwd)/data:/var/lib/mysql \
        -e MYSQL_ROOT_PASSWORD=password \
        -e MYSQL_DATABASE=sample_db \
        -p 3306:3306 \
        -d mysql:latest
    
    python process.py

fi

