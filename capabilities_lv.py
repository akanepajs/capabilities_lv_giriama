from google.colab import userdata
import os

# Install
!pip install inspect-ai
!pip install git+https://github.com/UKGovernmentBEIS/inspect_evals
!pip install anthropic
!pip install --upgrade google-generativeai

# Set the API key
os.environ['ANTHROPIC_API_KEY'] = userdata.get('ANTHROPIC_API_KEY')
os.environ['GOOGLE_API_KEY'] = userdata.get('GOOGLE_API_KEY')

# Run the inspect command
#!inspect eval mmlu_lv.py --model anthropic/claude-3-haiku-20240307 --limit 50
#!inspect eval mmlu_lv.py --model anthropic/claude-3-5-sonnet-20240620	--limit 50
!inspect eval mmlu_lv.py --model google/gemini-1.5-flash-002	--limit 50
!inspect eval mmlu_lv.py --model google/gemini-1.5-pro-002 --limit 50
