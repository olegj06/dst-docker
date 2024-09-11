#!/bin/bash

DIR=test-log

if [ ! -d $DIR ]; then 
mkdir ./$DIR
fi

docker-compose up -d