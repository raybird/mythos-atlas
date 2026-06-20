#!/bin/bash
# Usage: ./populate.sh [--mode new|enrich|analyze|ref|explore] [--batch N] [--random]
set -e
cd "$(dirname "$0")"
python3 populate.py "$@" >> populate.log 2>&1
