!pip install huggingface_hub
from huggingface_hub import HfApi, login
import os

# Login first using the login function
token = os.getenv('HUGGING_FACE_TOKEN')
login(token=token)  # Use the separate login function

# Then create the API instance
api = HfApi()

# Create a new dataset repository
repo_name = "mmlux-research"  # you can change this name
try:
    api.create_repo(
        repo_id=f"akanepajs/{repo_name}",
        repo_type="dataset",
        private=False  # Set to True if you want it private initially
    )
    print(f"Created repository: akanepajs/{repo_name}")
except Exception as e:
    print(f"Repository might already exist or there was an error: {e}")

# Upload the files
download_dir = "downloaded_files"  # adjust if your files are in a different directory
for file in os.listdir(download_dir):
    if file.endswith('.jsonl'):
        print(f"Uploading {file}...")
        try:
            api.upload_file(
                path_or_fileobj=f"{download_dir}/{file}",
                path_in_repo=file,
                repo_id=f"akanepajs/{repo_name}",
                repo_type="dataset",
                token=token  # Add token here explicitly
            )
            print(f"Successfully uploaded {file}")
        except Exception as e:
            print(f"Error uploading {file}: {e}")

print("\nUpload complete! Your dataset should be available at:")
print(f"https://huggingface.co/datasets/akanepajs/{repo_name}")
