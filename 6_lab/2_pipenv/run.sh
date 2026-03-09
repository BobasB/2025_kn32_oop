#!/bin/bash

export ENVIRONMENT=development
pipenv install
pipenv run python ../app.py
