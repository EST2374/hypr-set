#!/bin/bash

SETTING=$1
ARG=$2
ARG2=$3
VALUE=$4
CONFIG="$HOME/Work/hypr-set/hyprland.conf"
# CONFIG_REAL="$HOME/.config/hypr/monitors.conf"

    if [[ "$#" -ne 4 ]]; then
        echo "Usage: hypr-set [setting] [arg]"
        exit
    fi


set_monitor() {
    # TODO 
    # Multi Monitor setup

    CUR_MONITOR_CONF=$(grep "monitor =" "$CONFIG")

    readarray -t values < <(echo "$CUR_MONITOR_CONF" | awk -F',' '{
    sub(/^.*= /, ""); # Löscht alles vom Anfang bis "= "
    for(i=1; i<=NF; i++) print $i
}')

    if [[ "$ARG" == "show" ]]; then
        ANZ_MONITOR=$(hyprctl monitors -j | jq 'length')
        NAME_MONITOR=$(hyprctl monitors -j | jq -r '.[].name')
        RES_MONITOR_WIDTH=$(hyprctl monitors -j | jq -r '.[].width')
        RES_MONITOR_HEIGHT=$(hyprctl monitors -j | jq -r '.[].height')
        POS_MONITOR=$(hyprctl monitors -j | jq -r '.[].id')
        SCALE_MONITOR=$(hyprctl monitors -j | jq -r '.[].scale')
    
        echo "Monitor(s): $ANZ_MONITOR"
        echo "Name(s): $NAME_MONITOR"
        echo "Current Resolution: "$RES_MONITOR_WIDTH"x"$RES_MONITOR_HEIGHT""
        echo "Current Position: $POS_MONITOR "
        echo "Current Scale: $SCALE_MONITOR"
    fi
    
    # TODO
    # VALUE error handling
    if [[ "$ARG" == "set" ]]; then
        if [[ "$ARG2" == "scale" ]]; then
            sed -i "s|$CUR_MONITOR_CONF|monitor = ${values[0]},${values[1]},${values[2]},$VALUE|" "$CONFIG"
        fi

        if [[ "$ARG2" == "position" ]]; then
            sed -i "s|$CUR_MONITOR_CONF|monitor = ${values[0]},${values[1]},$VALUE,${values[3]}|" "$CONFIG"
        fi
        
        if [[ "$ARG2" == "resolution" ]]; then
            sed -i "s|$CUR_MONITOR_CONF|monitor = ${values[0]},$VALUE,${values[2]},${values[3]}|" "$CONFIG"
        fi

        if [[ "$ARG2" == "name" ]]; then
            sed -i "s|$CUR_MONITOR_CONF|monitor = $VALUE,${values[1]},${values[2]},${values[3]}|" "$CONFIG"
        fi
    fi

}




main() {
    if [[ "$SETTING" == "monitor" ]]; then
        set_monitor 
    fi

    if [[ "$SETTING" == "programs" ]]; then
        set_monitor 
    fi

    if [[ "$SETTING" == "autostart" ]]; then
        set_monitor 
    fi

    if [[ "$SETTING" == "looks" ]]; then
        set_monitor 
    fi
    
    if [[ "$SETTING" == "input" ]]; then
        set_monitor 
    fi

    if [[ "$SETTING" == "keybindings" ]]; then
        set_monitor 
    fi
    
    if [[ "$SETTING" == "windows" ]]; then
        set_monitor 
    fi


}

main
