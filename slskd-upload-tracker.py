import json
import os
from datetime import datetime
import sys
import re
from pathlib import Path

def get_filename_only(filepath):
    """Extract just the filename from a full path"""
    return os.path.basename(filepath)

def process_upload(data, tracker_dir):
    username = data['transfer']['username']
    megabytes = round(data['transfer']['bytesTransferred'] / (1024 * 1024), 2)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = get_filename_only(data['transfer'].get('filename', 'unknown_file'))
    
    user_file = os.path.join(tracker_dir, f"{username}.txt")
    
    log_entry = f"{timestamp}: {filename} - {megabytes} MB"
    
    if os.path.exists(user_file):
        with open(user_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        lines = content.split('\n')
        
        header = lines[0] if lines else f"Upload History for {username}"
        
        upload_entries = []
        in_entries_section = False
        found_separator = False
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            if line == header:
                continue
                
            if '=========================' in line:
                found_separator = True
                break
                
            if not found_separator:
                upload_entries.append(line)
        
        upload_entries.append(log_entry)
        
        total_mb = 0.0
        for entry in upload_entries:
            try:
                match = re.search(r'(\d+\.?\d*)\s*MB$', entry, re.IGNORECASE)
                if match:
                    total_mb += float(match.group(1))
            except (ValueError, AttributeError) as e:
                print(f"Warning: Could not parse MB from entry: {entry} - {e}")
                continue
        
        total_mb = round(total_mb, 2)
        
        with open(user_file, 'w', encoding='utf-8') as f:
            header_text = f"Upload History for {username}"
            f.write(f"{header_text}\n\n")
            
            for entry in upload_entries:
                f.write(entry + '\n')
            
            f.write("\n=========================\n")
            f.write(f"Last check: {timestamp}, Total megabytes transferred so far: {total_mb} MB\n")
    else:
        with open(user_file, 'w', encoding='utf-8') as f:
            header_text = f"Upload History for {username}"
            f.write(f"{header_text}\n\n")
            f.write(log_entry + '\n')
            f.write("\n=========================\n")
            f.write(f"Last check: {timestamp}, Total megabytes transferred so far: {megabytes} MB\n")
    
    print(f"Logged {megabytes} MB to {username} - {filename}")

def main():
    if os.name == 'nt':
        tracker_dir = Path(os.environ['LOCALAPPDATA']) / "slskd" / "upload-tracker"
    else:
        tracker_dir = Path.home() / ".local" / "share" / "slskd" / "upload-tracker"
    
    tracker_dir.mkdir(parents=True, exist_ok=True)
    
    json_data = os.environ.get('SLSKD_SCRIPT_DATA')
    
    if not json_data:
        print("No SLSKD_SCRIPT_DATA environment variable found")
        return
    
    try:
        data = json.loads(json_data)
        process_upload(data, tracker_dir)
    except Exception as e:
        print(f"Error processing upload data: {e}")

if __name__ == "__main__":

    main()

