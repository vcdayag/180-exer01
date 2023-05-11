#!/bin/bash

gnome-terminal -- bash -c "python3 ./server.py $1 5050 1; exec bash"
gnome-terminal -- bash -c "python3 ./client.py; exec bash"