#!/bin/bash

first=1
second=10

rm ./${first}
rm ./${second}
python main.py 100 ${first} > ${first} &&
python main.py 100 ${second} > ${second} &&
diff -y -W 60 ${first} ${second}