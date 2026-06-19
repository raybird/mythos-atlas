#!/bin/bash
set -e
cd "$(dirname "$0")"
python3 populate.py >> populate.log 2>&1
