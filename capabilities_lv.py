from google.colab import userdata
import os

# Install
#!pip install inspect-ai
#!pip install git+https://github.com/UKGovernmentBEIS/inspect_evals
#!pip install openai
#!pip install anthropic
#!pip install --upgrade google-generativeai


# Set the API key
os.environ['ANTHROPIC_API_KEY'] = userdata.get('ANTHROPIC_API_KEY')
os.environ['GOOGLE_API_KEY'] = userdata.get('GOOGLE_API_KEY')
os.environ['OPENAI_API_KEY'] = userdata.get('OPENAI_API_KEY')

#models
# https://inspect.ai-safety-institute.org.uk/
# https://docs.anthropic.com/en/docs/about-claude/models 
# https://ai.google.dev/gemini-api/docs/models/gemini 

# Run the inspect command
#!inspect eval mmlu_lv.py --model openai/o1-mini-2024-09-12		--limit 50
#!inspect eval mmlu_lv.py --model openai/o1-preview-2024-09-12 --limit 50
#!inspect eval mmlu_lv.py --model anthropic/claude-3-haiku-20240307 --limit 50
#!inspect eval mmlu_lv.py --model anthropic/claude-3-5-sonnet-20240620	--limit 50
#!inspect eval mmlu_lv.py --model google/gemini-1.5-flash-002	--limit 50
#!inspect eval mmlu_lv.py --model google/gemini-1.5-pro-002 --limit 50
#!inspect eval mmlu_lv.py --model openai/gpt-4o-mini-2024-07-18	--limit 50
#!inspect eval mmlu_lv.py --model openai/gpt-4o-2024-08-06	--limit 50
!inspect eval mmlu_lv.py --model openai/gpt-4o-realtime-preview-2024-10-01	--limit 50
