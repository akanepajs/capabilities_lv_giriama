import os
import zipfile
import tarfile
import shutil
from tqdm import tqdm
import glob

def format_size(size_bytes):
    """Convert bytes to human readable format"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} GB"

def create_archive(source_dir, archive_name=None, archive_type='zip'):
    """
    Create an archive of all CSV files in the source directory
    
    Parameters:
    - source_dir: Directory containing CSV files
    - archive_name: Name for the archive file (optional)
    - archive_type: 'zip' or 'tar.gz'
    """
    # Get list of all CSV files
    csv_files = glob.glob(os.path.join(source_dir, "*.csv"))
    
    if not csv_files:
        print(f"No CSV files found in {source_dir}")
        return
    
    total_size = sum(os.path.getsize(f) for f in csv_files)
    print(f"Found {len(csv_files)} CSV files")
    print(f"Total uncompressed size: {format_size(total_size)}")
    
    # Default archive name if none provided
    if archive_name is None:
        archive_name = f"csv_archive_{len(csv_files)}_files"
    
    if archive_type == 'zip':
        archive_path = f"{archive_name}.zip"
        print(f"\nCreating ZIP archive: {archive_path}")
        
        with zipfile.ZipFile(archive_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file in tqdm(csv_files, desc="Adding files to ZIP"):
                # Add file to zip with just its basename to avoid directory structure
                zipf.write(file, os.path.basename(file))
                
    elif archive_type == 'tar.gz':
        archive_path = f"{archive_name}.tar.gz"
        print(f"\nCreating TAR.GZ archive: {archive_path}")
        
        with tarfile.open(archive_path, "w:gz") as tar:
            for file in tqdm(csv_files, desc="Adding files to TAR.GZ"):
                # Add file to tar with just its basename to avoid directory structure
                tar.add(file, arcname=os.path.basename(file))
    
    # Get compressed size
    compressed_size = os.path.getsize(archive_path)
    compression_ratio = (1 - compressed_size / total_size) * 100
    
    print(f"\nArchive created successfully!")
    print(f"Archive size: {format_size(compressed_size)}")
    print(f"Compression ratio: {compression_ratio:.1f}%")
    print(f"Archive saved as: {os.path.abspath(archive_path)}")

if __name__ == "__main__":
    # Configuration
    source_directory = "downloaded_files"  # Directory containing your CSV files
    archive_name = "mmlu_dataset"          # Name for the archive (without extension)
    
    # Create both ZIP and TAR.GZ archives (you can comment out one if you prefer)
    create_archive(source_directory, archive_name, 'zip')
    create_archive(source_directory, archive_name, 'tar.gz')
