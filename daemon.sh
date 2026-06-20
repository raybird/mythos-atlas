#!/bin/bash
# Mythos Atlas daemon — 探索排程，不再受限於固定框架
# 每小時以不同模式執行 populate.py，輪替探索策略
# Usage: nohup ./daemon.sh & (or add to systemd/supervisor)

REPO="$(cd "$(dirname "$0")" && pwd)"
cd "$REPO"

MODE_CYCLE=(new enrich analyze ref explore)
CYCLE_LEN=${#MODE_CYCLE[@]}
ITER=0

while true; do
    # Calculate seconds until next :10 of the hour
    MIN=$(date +%M)
    SEC=$(date +%S)
    CURRENT_SEC=$((10#$MIN * 60 + 10#$SEC))
    TARGET_SEC=$((10 * 60))  # minute 10 = 600 seconds
    if [ $CURRENT_SEC -ge $TARGET_SEC ]; then
        DELAY=$((3600 - CURRENT_SEC + TARGET_SEC))
    else
        DELAY=$((TARGET_SEC - CURRENT_SEC))
    fi

    echo "$(date): Sleeping ${DELAY}s until next :10 mark..."
    sleep "$DELAY"

    # Pick mode: cycle through modes, with occasional random exploration
    MODE_INDEX=$((ITER % CYCLE_LEN))
    MODE="${MODE_CYCLE[$MODE_INDEX]}"

    # Every 4th run, do a larger batch
    BATCH=1
    RANDOM=""
    if [ $((ITER % 4)) -eq 0 ]; then
        BATCH=3
        RANDOM="--random"
    fi

    echo "$(date): [Iter $ITER] Running populate.py --mode $MODE --batch $BATCH $RANDOM ..."
    python3 "$REPO/populate.py" --mode "$MODE" --batch "$BATCH" $RANDOM >> "$REPO/populate.log" 2>&1
    echo "$(date): populate.py finished (exit code: $?)"

    ITER=$((ITER + 1))
done
