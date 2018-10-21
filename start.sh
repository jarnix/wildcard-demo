#! /usr/bin/env sh

gunicorn --bind=0.0.0.0:8080 --chdir=/app --log-level=INFO wildcard_demo:app
