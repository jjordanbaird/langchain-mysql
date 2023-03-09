#!/bin/bash

docker run --name mysql-langchain-container \
  -v $(pwd)/data:/var/lib/mysql \
  -e MYSQL_ROOT_PASSWORD=password \
  -e MYSQL_DATABASE=sample_db \
  -p 3306:3306 \
  -d mysql:latest
