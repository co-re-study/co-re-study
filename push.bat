@echo off
git pull origin master
git add .
git commit -m '%date%-commit'
git push origin master
timeout 3