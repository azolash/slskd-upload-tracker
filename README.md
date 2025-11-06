## Description

This is a simple python script that tracks uploads per user in seperate txt files. The files are updated regularly after each complete download.
Only the file name and its size in Megabytes is documented. And a total of uploaded megabytes so far is calculated at the end. 

## Example

leecher.txt

Upload History for leecher

2025-11-06 04:17:50: Artist - Song (Extended Mix).flac - 39.96 MB

=========================

Last check: 2025-11-06 04:17:50, Total megabytes transferred so far: 39.96 MB

## Requirements:
- Latest version of Python
- Integration in the slskd.yml file.

## Integration

locate your slskd.yml file, usually in %localappdata%/slskd
copy this piece of code to the perspective area of "integration".
Make sure the indentation stays the same or slskd won't start.

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

## Usage
Download the py file and copy it to %localappdata%/slskd/scripts
The script will start automatically with slskd if the integration is correct and python is isntalled. 
It will record data on uploads to users.
The output folder is configured to be %localappdata%/slskd-upload-tracker but you can change it in the code if you want. 
To make sure the script is working check the folder for new txt files.

## License
MIT

## Acknowledgement 
Thanks to slskd and its developers for creating this great software. 
