#!/bin/sh

TODAY=`date +"%Y%m%d"`
YESTERDAY=`date -d "1 day ago" +"%Y%m%d"`
OLDBACKUP=`date -d "2 days ago" +"%Y%m%d"`

# Set the path to rsync on the remote server so it runs with sudo.
RSYNC="/usr/bin/rsync"

# Set the folderpath on the QNAP
# Dont't forget to mkdir $SHAREPATH
SHAREPATH="/mnt/homecloud/Champ/hc_backup"
 
# This is a list of files to ignore from backups.
# Dont't forget to touch $EXCLUDES
# EXCLUDES="$SHAREPATH/servername.excludes"

#LOG file
# Dont't forget to touch $LOG
LOG="$SHAREPATH/BACKUP_success.log"
 
# Source and Destination
SOURCE="devendrarath@172.16.16.199:/Users/devendrarath/Documents/"

DESTINATION="$SHAREPATH/mini2020"

rsync -avrh --no-perms --no-group --no-owner --info=progress2 $SOURCE $DESTINATION

# Writes a log of successful updates
echo "BACKUP success-$TODAY" >> $LOG

# Clean exit
exit 0