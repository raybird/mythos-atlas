#!/bin/bash
# Mythos Atlas daemon — runs populate.py every hour at minute :10
# Workflow per run: generate entry → git commit → git push → cleanup temp files
# Usage: nohup ./daemon.sh & (or add to systemd/supervisor)

REPO="$(cd "$(dirname "$0")" && pwd)"
cd "$REPO"

while true; do
    # Calculate seconds until next :10 of the hour
    MIN=$(date +%M)
    SEC=$(date +%S)
    CURRENT_SEC=$((10#$MIN * 60 + 10#$SEC))
    TARGET_SEC=$((10 * 60))  # minute 10 = 600 seconds
    if [ $CURRENT_SEC -ge $TARGET_SEC ]; then
        # Past :10, target next hour
        DELAY=$((3600 - CURRENT_SEC + TARGET_SEC))
    else
        DELAY=$((TARGET_SEC - CURRENT_SEC))
    fi

    echo "$(date): Sleeping ${DELAY}s until next :10 mark..."
    sleep "$DELAY"
    
    echo "$(date): Running populate.py (generate → commit → push → cleanup)..."
    python3 "$REPO/populate.py" >> "$REPO/populate.log" 2>&1
    echo "$(date): populate.py finished (exit code: $?)"
done
