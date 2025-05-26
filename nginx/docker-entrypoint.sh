#!/bin/bash
set -e

wait-for-it django:8000 -- echo "Django server is up!"
nginx -g 'daemon off;'
