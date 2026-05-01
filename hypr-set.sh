#!/bin/bash

SETTING=$1
ARG=$2
ARG2=$3
VALUE=$4
DEFAULT_CONF="$HOME/Work/hypr-set/default_hyprland.conf"
CONFIG="$HOME/Work/hypr-set/hyprland.conf"
#CONFIG_REAL="$HOME/.config/hypr/conf/style.conf"

print_help() {
    local context="${1:-general}"

    case "$context" in
        general)
            echo "Usage: hypr-set [setting] [arg] [arg2] [value]"
            echo ""
            echo "Settings:"
            echo "  monitor      Monitor config"
            echo "  autostart    Autostart programs"
            echo "  environment  Environment variables"
            echo "  look         Look and feel (Borders, Gaps, Colors)"
            echo "  input        Input"
            echo "  keybinding   Keybindings"
            echo "  window       Windowrules"
            echo ""
            echo "For more help: hypr-set [setting] help"
            ;;

        monitor)
            echo "Usage: hypr-set monitor [arg] [arg2] [value]"
            echo ""
            echo "  monitor show"
            echo "  monitor set scale     <wert>        e.g. 1.5"
            echo "  monitor set position  <x>x<y>       e.g. 0x0"
            echo "  monitor set resolution <WxH>@<Hz>   e.g. 1920x1080@60"
            echo "  monitor set name      <name>        e.g. DP-1"
            echo "  monitor set all                     (interactive)"
            ;;

        autostart)
            echo "Usage: hypr-set autostart [arg] [programm]"
            echo ""
            echo "  autostart show"
            echo "  autostart new    <programm>    e.g. waybar"
            echo "  autostart delete <programm>"
            ;;

        look)
            echo "Usage: hypr-set look set [arg2] [value]"
            echo ""
            echo "  look set border_size  <px>      e.g. 2"
            echo "  look set gaps_in      <px>      e.g. 5"
            echo "  look set gaps_out     <px>      e.g. 10"
            echo "  look set acol1        <hex>     e.g. ff00ff"
            echo "  look set acol2        <hex>     e.g. 00ffff"
            ;;

        input)
            echo "Usage: hypr-set input set [arg2] [value]"
            echo ""
            echo "  input set layout  <layout>    e.g. de"
            echo "  input set scroll  true|false"
            ;;

        *)
            echo "Unknown: '$context'"
            echo "Settings: monitor|autostart|environment|look|input|keybinding|window"
            ;;
    esac
    exit 0
}

set_monitor() {
    if [[ -z "$ARG" || "$ARG" == "help" ]]; then
        print_help "monitor"
    fi

    # TODO
    # Multi Monitor setup

    CUR_MONITOR_CONF=$(grep "monitor =" "$CONFIG")

    readarray -t values < <(echo "$CUR_MONITOR_CONF" | awk -F',' '{
    sub(/^.*= /, ""); for(i=1; i<=NF; i++) print $i
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

        if [[ "$ARG2" == "all" ]]; then
            read -p "Monitor Name: " MONITOR_NAME
            read -p "Monitor Resolution: " MONITOR_RES
            read -p "Monitor Position: " MONITOR_POS
            read -p "Monitor Scale: " MONITOR_SCALE

            sed -i "s|$CUR_MONITOR_CONF|monitor = $MONITOR_NAME,$MONITOR_RES,$MONITOR_POS,$MONITOR_SCALE|" "$CONFIG"
        fi

    else echo "Current Config: $CUR_MONITOR_CONF"


    fi
}



set_autostart() {
    if [[ -z "$ARG" || "$ARG" == "help" ]]; then
        print_help "autostart"
    fi

    # TODO Error handling
    if [[ "$ARG" == "show" ]]; then
        ALL_AUTOSTART=$(grep "exec-once" "$CONFIG" | grep -v "^[[:space:]]*#")
        echo "$ALL_AUTOSTART"
    fi

    if [[ "$ARG" == "new" ]]; then
        last_line=$(grep -n "exec-once" "$CONFIG" | cut -d: -f1 | tail -n 1)
        if [ -n "$last_line" ]; then
            sed -i "${last_line}a exec-once = ${ARG2}" "$CONFIG"
        else
            echo "Error"
        fi
    fi

    if [[ "$ARG" == "delete" ]]; then
        sed -i "/exec-once = $ARG2*/d" "$CONFIG"
    fi
}

set_environment() {
    if [[ -z "$ARG" || "$ARG" == "help" ]]; then
        print_help "environment"
    fi

    # TODO Error handling
    if [[ "$ARG" == "show" ]]; then
        ALL_ENVIRONMENT=$(grep "env" "$CONFIG" | grep -v "^[[:space:]]*#")
        echo "$ALL_ENVIRONMENT"
    fi

    if [[ "$ARG" == "new" ]]; then
        last_line=$(grep -n "env" "$CONFIG" | cut -d: -f1 | tail -n 1)
        if [ -n "$last_line" ]; then
            sed -i "${last_line}a env = $ARG2" "$CONFIG"
        else
            echo "Error"
        fi
    fi

    if [[ "$ARG" == "delete" ]]; then
        sed -i "/env = $ARG2*/d" "$CONFIG"
    fi
}


set_looks() {
    if [[ -z "$ARG" || "$ARG" == "help" ]]; then
        print_help "look"
    fi

    #TODO
    # Error handling
    if [[ "$ARG" == "set" ]]; then

        if [[ "$ARG2" == "border_size" ]]; then
            CUR_BORDERSIZE=$(grep "border_size" "$CONFIG" | grep -v "^[[:space:]]*#")
            sed -i "s|$CUR_BORDERSIZE|\tborder_size = $VALUE|" "$CONFIG"
        fi

        if [[ "$ARG2" == "gaps_in" ]]; then
            CUR_GAPSIN=$(grep "gaps_in" "$CONFIG")
            sed -i "s|$CUR_GAPSIN|\tgaps_in = $VALUE|" "$CONFIG"
        fi

        if [[ "$ARG2" == "gaps_out" ]]; then
            CUR_GAPSOUT=$(grep "gaps_out" "$CONFIG")
            sed -i "s|$CUR_GAPSOUT|\tgaps_out = $VALUE|" "$CONFIG"
        fi

        #TODO
        # if rgba oder normal rgb
        if [[ "$ARG2" == "acol1" ]]; then
            CUR_ACTPRIMCOL1=$(grep "col.active_border" "$CONFIG" | awk '{printf $3}')
            sed -i "s|$CUR_ACTPRIMCOL1|rgb($VALUE)|" "$CONFIG"
        fi

        if [[ "$ARG2" == "acol2" ]]; then
            CUR_ACTPRIMCOL2=$(grep "col.active_border" "$CONFIG" | awk '{printf $4}')
            sed -i "s|$CUR_ACTPRIMCOL2|rgb($VALUE)|" "$CONFIG"
        fi

        if [[ "$ARG2" == "icol" ]]; then
            CUR_INACTPRIMCOL=$(grep "col.inactive_border" "$CONFIG" | awk '{printf $3}')
            sed -i "s|$CUR_INACTPRIMCOL|rgb($VALUE)|" "$CONFIG"
        fi

        if [[ "$ARG2" == "rounding" ]]; then
            CUR_ROUNDING=$(grep "rounding" "$CONFIG" | grep -v "^[[:space:]]*#" | head -n 1)
            sed -i "s|$CUR_ROUNDING|\trounding = $VALUE|" "$CONFIG"
        fi


    fi
}

set_input() {
    if [[ -z "$ARG" || "$ARG" == "help" ]]; then
        print_help "input"
    fi
    # TODO
    # Error handling
    # More Options
    if [[ "$ARG" == "set" ]]; then

        if [[ "$ARG2" == "layout" ]]; then
            CUR_KB_LAYOUT=$(grep "kb_layout" "$CONFIG")
            sed -i "s|$CUR_KB_LAYOUT|\tkb_layout = $VALUE|" "$CONFIG"
        fi

        if [[ "$ARG2" == "scroll" ]]; then
            CUR_SCROLL=$(grep "natural_scroll" "$CONFIG")
            sed -i "s|$CUR_SCROLL|\t\tnatural_scroll = $VALUE|" "$CONFIG"
        fi

    fi
}

#TODO
set_keybindings() {
    if [[ -z "$ARG" || "$ARG" == "help" ]]; then
        print_help "keybinding"
    fi

    # TODO Error handling
    if [[ "$ARG" == "show" ]]; then
        ALL_KEYBINDINGS=$(grep "bind" "$CONFIG" | grep -v "^[[:space:]]*#")
        echo "$ALL_KEYBINDINGS"
    fi

    if [[ "$ARG" == "new" ]]; then

            if [[ "$ARG2" == "keybinding" ]]; then
                marker_line=$(grep -n "# Keybindings end" "$CONFIG" | cut -d: -f1)
                if [[ -n "$marker_line" ]]; then
                    insert_at=$(( marker_line - 1 ))
                    sed -i "${insert_at}i bind = $VALUE" "$CONFIG"
                else
                    echo "Error: Could not find '# Keybindings end' marker"
                fi
            fi

            if [[ "$ARG2" == "keymove" ]]; then
                marker_line=$(grep -n "# keymove end" "$CONFIG" | cut -d: -f1)
                if [[ -n "$marker_line" ]]; then
                    insert_at=$(( marker_line - 1 ))
                    sed -i "${insert_at}i bind = $VALUE" "$CONFIG"
                else
                    echo "Error: Could not find '# Keymove end' marker"
                fi
            fi

            if [[ "$ARG2" == "keyworkspace" ]]; then
                marker_line=$(grep -n "# keyworkspace end" "$CONFIG" | cut -d: -f1)
                if [[ -n "$marker_line" ]]; then
                    insert_at=$(( marker_line - 1 ))
                    sed -i "${insert_at}i bind = $VALUE" "$CONFIG"
                else
                    echo "Error: Could not find '# keyworkspace end' marker"
                fi
            fi

            if [[ "$ARG2" == "keymultimedia" ]]; then
                marker_line=$(grep -n "# keymultimedia end" "$CONFIG" | cut -d: -f1)
                if [[ -n "$marker_line" ]]; then
                    insert_at=$(( marker_line - 1 ))
                    sed -i "${insert_at}i bind = $VALUE" "$CONFIG"
                else
                    echo "Error: Could not find '# keymultimedia end' marker"
                fi
            fi

    fi

    if [[ "$ARG" == "delete" ]]; then
        sed -i "/bind.*$ARG2*/d" "$CONFIG"
    fi

}


set_windows() {

}


make_Marker() {
    #TODO
    # Not change everything
    first_line=$(head -n 1 "$CONFIG")

    if [[ "$first_line" == "#Marked" || "$first_line" == "# Marked" ]]; then
        if [[ "$first_line" != "#Marked" ]]; then
            sed -i "1s|.*|#Marked|" "$CONFIG"
        fi
        return
    fi

    cp "$DEFAULT_CONF" "$CONFIG"
    sed -i "1s|.*|#Marked|" "$CONFIG"
}


main() {

    make_Marker

    if [[ -z "$SETTING" || "$SETTING" == "help" || "$SETTING" == "--help" || "$SETTING" == "-h" ]]; then
        print_help "general"
    fi

    case "$SETTING" in
        monitor)     set_monitor ;;
        environment) set_environment ;;
        autostart)   set_autostart ;;
        look)        set_looks ;;
        input)       set_input ;;
        keybinding)  set_keybindings ;;
        window)      set_windows ;;
        *)
            echo "Unknown Settings: '$SETTING'"
            print_help "general"
            ;;
    esac
}

main
