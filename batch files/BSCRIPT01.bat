@echo off
start chrome "https://www.google.com"
start chrome "https://www.youtube.com"
start chrome "https://www.facebook.com"
start chrome "https://www.instagram.com"
start chrome "https://www.twitter.com"

pause

start notepad
start calc

REM /t [seconds] [/nobreak]
echo The system will shutdown after 60 secs
timeout /t 60 

shutdown