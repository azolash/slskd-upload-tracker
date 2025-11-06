# SLSKD UPLOAD TRACKER

## Description

This is a simple python script that tracks uploads per user in seperate txt files.
Each user is assigned a txt file named after them. 
The files are updated regularly after each complete download.
The script will document time of upload, filename and size in Megabytes.
A total of uploaded megabytes so far is calculated at the end. 

## Example

example.txt

```txt
Upload History for example

2025-11-01 23:34:51: Song 1 (Original Mix).mp3 - 11.4 MB
2025-11-02 00:17:02: Song 2 (Extended Mix).mp3 - 12.43 MB
2025-11-02 00:18:53: Song 3 (Remix).mp3 - 15.73 MB

=========================
Last check: 2025-11-02 00:18:53, Total megabytes transferred so far: 39.56 MB
```

## Requirements:
- slskd-upload-tracker.py
- Latest version of Python
- Integration in the slskd.yml file.

## Usage
Download slskd-upload-tracker.py and copy it to %localappdata%/slskd/scripts
The script will start automatically with slskd if the integration is correct and python is isntalled. 
The output folder is configured to be %localappdata%/slskd-upload-tracker but you can change it in the code if you want. 
To make sure the script is working check the folder for new txt files.

## Integration

locate your slskd.yml file, usually in %localappdata%/slskd
copy this piece of code to the perspective area of "integration".
Make sure the indentation stays the same or slskd won't start.
An example of slskd.yml is available to see how integration should look like.

slskd.yml

```yaml
  integration:
    scripts:
      upload_tracker:
        on:
          - UploadFileComplete
        run:
          command: 'python %localappdata%\slskd\scripts\slskd-upload-tracker.py'
```

## License
MIT

## Acknowledgement 
Thanks to slskd and its developers for creating this great software. 
