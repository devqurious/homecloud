#!/bin/sh

# Set the path to rsync on the remote server so it runs with sudo.
RSYNC="/usr/bin/rsync"

#Todays date in ISO-8601 format:
TODAY=$(date +"%Y-%m-%d %H:%M:%S")

#LOG file
LOG="/Users/devendrarath/backup_log.txt"
 
# Source and Destination
S1="/Users/devendrarath/Documents"
S2="/Users/devendrarath/Desktop"
S3="/Users/devendrarath/Pictures/PhotosLibrary.photoslibrary/originals/"

DESTINATION="root@172.16.16.16:/data"

echo "Starting-$TODAY" >> $LOG

#rsync -avrh --no-perms --no-group --no-owner $SOURCE $DESTINATION
rsync -avrzR --chmod=a+rx --exclude=.DS_Store -e 'ssh -p 30037' $S1 $S2 $S3 $DESTINATION

# Writes a log of successful updates
echo "BACKUP success-$TODAY" >> $LOG

# Clean exit
exit 0
