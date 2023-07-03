#!/bin/bash

echo "Welcome to 9xGen! The home for all your mod7 needs."
echo " "
echo "[1] 10-digit key for Windows 95 Retail copies"
echo "[2] 11-digit CD key for Office 97"
echo "[3] Key for Windows 95 OEM copies"
echo " "

read -p "Input choice: " choice
case $choice in
    1) python 10key.py;;
    2) python 11key.py;;
    3) python oemkey.py;;
esac