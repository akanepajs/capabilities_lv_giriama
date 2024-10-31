import os
import requests
import time
from tqdm import tqdm

def format_size(size_bytes):
    """Convert bytes to human readable format"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} GB"

def get_all_files():
    """Get complete file list using HuggingFace API"""
    print("Fetching complete file list using API...")
    
    api_url = "https://huggingface.co/api/datasets/openGPT-X/mmlux/tree/main"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        
        files_data = response.json()
        jsonl_files = [
            file['path'] 
            for file in files_data 
            if file['type'] == 'file' 
            and file['path'].endswith('.jsonl')
        ]
        
        return jsonl_files
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching file list: {e}")
        return []

def download_files(base_file_url, output_dir='downloaded_files', max_retries=3, delay_between_retries=5):
    """Download files from HuggingFace datasets with retry mechanism"""
    os.makedirs(output_dir, exist_ok=True)
    session = requests.Session()
    
    files = get_all_files()
    
    if not files:
        print("No files found! Check the repository URL and permissions.")
        return
    
    print(f"\nFound {len(files)} files to download:")
    for f in files:
        print(f"- {f}")
    
    print(f"\nPreparing to download {len(files)} files. Continue? (y/n)")
    if input().lower() != 'y':
        print("Download cancelled.")
        return
    
    total_size = 0
    successful_downloads = 0
    failed_downloads = []
    
    for file_path in tqdm(files, desc="Downloading files"):
        file_url = base_file_url + file_path
        output_path = os.path.join(output_dir, os.path.basename(file_path))
        
        if os.path.exists(output_path):
            file_size = os.path.getsize(output_path)
            print(f"\nSkipping {file_path} - already exists ({format_size(file_size)})")
            total_size += file_size
            successful_downloads += 1
            continue
            
        for attempt in range(max_retries):
            try:
                response = session.get(file_url, stream=True)
                response.raise_for_status()
                
                # Save the file directly
                with open(output_path, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
                
                file_size = os.path.getsize(output_path)
                total_size += file_size
                successful_downloads += 1
                
                print(f"\nSaved {output_path}")
                print(f"File size: {format_size(file_size)}")
                
                time.sleep(1)  # Small delay between files
                break
                
            except requests.exceptions.RequestException as e:
                if attempt < max_retries - 1:
                    print(f"\nRetry {attempt + 1}/{max_retries} for {file_path} after error: {e}")
                    time.sleep(delay_between_retries)
                else:
                    print(f"\nFailed to download {file_path} after {max_retries} attempts: {e}")
                    failed_downloads.append(file_path)
            except Exception as e:
                print(f"\nUnexpected error processing {file_path}: {e}")
                failed_downloads.append(file_path)
                break
    
    print(f"\nDownload complete!")
    print(f"Successfully downloaded: {successful_downloads}/{len(files)} files")
    print(f"Total size on disk: {format_size(total_size)}")
    
    if failed_downloads:
        print("\nFailed downloads:")
        for failed in failed_downloads:
            print(f"- {failed}")

if __name__ == "__main__":
    base_file_url = 'https://huggingface.co/datasets/openGPT-X/mmlux/resolve/main/'
    download_files(base_file_url)
