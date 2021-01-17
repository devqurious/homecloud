#!/bin/bash
# Script to monitor and restart the mine craft server if necessary.

INSTALL_DIR=/etc/homecloud
python3 $INSTALL_DIR/check_minecraft.py -m 'Welcome to Minecraft on Home Cloud!' >/dev/null 2>&1
ret_code=$?

if [ $ret_code -ne 0 ]; then
    echo 'Minecraft server is not reachable, will try to restart the port-forward'
    if pgrep kubectl; then pkill kubectl; fi
    python3 $INSTALL_DIR/port-forward.py &
else
    echo 'Minecraft server is working fine'
fi

exit 0