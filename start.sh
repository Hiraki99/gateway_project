#!/bin/bash
# $app = "runGateway.py"
test=`ps aux | grep "runGateway" | grep -v grep -c`
if [ $test == 0 ]; then
        #pip install -r requirements.txt
        python3 runGateway.py --env=gateway >> logs-gateway.log  &
        echo "[INFO] Service is starting"
        exit
else
        echo "[WARN] Service is already running"
        exit
fi
