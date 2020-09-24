REM This script converts from mkv to mp4 container
REM Just drag and drop the mkv file onto this batch file
ffmpeg -i %1 -c copy -map 0 %1.mp4