# Folder Cleaner Script
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) ![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg) ![GitHub](https://img.shields.io/github/license/mazzya/folder-cleaner)
### This script allows you to clean up a directory. The script expects the directory path as an argument. 

**WARNING** : The script will clean all the contents of the directory without any verification, make sure that what you are going to clean is not important data.

## What is the purpose of this script ?
The goal is to automate the script to clean the folders every x times, for example a registry folder that needs to be cleaned every day because it takes up a lot of space.
## What is the correct way to use this script ?
### *Windows* 
If you want to automate the script in Windows, you must create a `.bat` file that runs the script. To automate it, you can use **Task Scheduler**, see here [Schedule Python Script in Windows](https://datatofish.com/python-script-windows-scheduler/)
### *Mac OS X / Linux*
If you want to automate the script in OSX or Linux, you must create a **cron job**, see here [Schedule a Python Script using Cron Job](https://gavinwiener.medium.com/how-to-schedule-a-python-script-cron-job-dea6cbf69f4e)
## Usage
```
usage : cleaner.py [-h] [-p PATH]

options arguments : 
    -h, --help          show this help message and exit
    -p, --path          folder path to clean
```
## Example
```
$ python cleaner.py -p D:\User\Documents\logs
```
#### Discord Server
We have a discord server in case you have any questions or want to be informed about the project news. Do not hesitate to [join us](https://discord.gg/mZF9ywQzdg), we are waiting for you.
