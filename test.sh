#!/bin/bash

line="monitor = ,preferred,auto,auto"

# 1. Wir löschen den Präfix "monitor = " 
# 2. Wir splitten den Rest anhand der Kommas
readarray -t werte < <(echo "$line" | awk -F',' '{
    sub(/^.*= /, ""); # Löscht alles vom Anfang bis "= "
    for(i=1; i<=NF; i++) print $i
}')

# Test der Ausgabe:
echo "Wert 1 (leer): '${werte[0]}'"
echo "Wert 2: '${werte[1]}'"
echo "Wert 3: '${werte[2]}'"
echo "Wert 4: '${werte[3]}'"
