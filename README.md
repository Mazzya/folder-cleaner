# Folder Cleaner
 
### This script allows you to clean up a directory. The script expects the directory path as an argument. 

**WARNING** : The script will clean all the contents of the directory without any verification, make sure that what you are going to clean is not important data.

## What is the purpose of this script? ?
The goal is to automate the script to clean the folders every x times, for example a log folder that needs to be cleaned every day.
## What is the correct way to use this script ?
### *Windows* 
If you want to automate the script in Windows, you must create a `.bat` file that runs the script. To automate it, you can use **Task Scheduler**, see here [Schedule Python Script in Windows](https://datatofish.com/python-script-windows-scheduler/)
### *Mac OS X / Linux*
If you want to automate the script in OSX or Linux, you must create a **cron job**, see here [Schedule a Python Script using Cron Job](https://gavinwiener.medium.com/how-to-schedule-a-python-script-cron-job-dea6cbf69f4e)
## How to execute the script ?
`python3 app.py --path`
### Command line arguments :
* **path** - *directory path you want to clean*