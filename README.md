## Description

This is a simple python script that tracks uploads per user in seperate txt files. The files are updated regularly after each complete download.
Only the file name and its size in Megabytes is documented. And a total of uploaded megabytes so far is calculated at the end. 

You need the latest version of python to run the script and to integrate it in slskd using the slskd.yml file.

## Example

leecher.txt

Upload History for leecher

2025-11-06 04:17:50: Artist - Song (Extended Mix).flac - 39.96 MB

=========================
Last check: 2025-11-06 04:17:50, Total megabytes transferred so far: 39.96 MB

## Integration

you need to change the slskd.yml file to integrate the script.
Make sure to remove all the relative # and that the identation stays the same.
And to change the path to where the script is located on your pc.

slskd.yml

  integration:
    scripts:
      upload_tracker:
        on:
          - UploadFileComplete
        run:
          command: 'python C:\path\to\script\upload-tracker.py'


## Usage

The script will start automatically with slskd and record data on uploads to users.
The output folder is configured to be C:\upload-tracker but you can change it in the code if you want. 

## License
MIT

## Acknowledgement 
Thanks to slskd and its developers for creating this great software. 
