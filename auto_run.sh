#! /bin/bash
ping -c 1 google.com
if [ $? -eq 0 ]; then 
  python3 $PWD/pin_activate_sms.py
else
  echo "not internet connection" 
fi