#from google.colab import drive
#drive.mount('/content/drive')

from google.colab import userdata
import os

# Install
#!pip install inspect-ai
#!pip install git+https://github.com/UKGovernmentBEIS/inspect_evals
#!pip install openai
#!pip install anthropic
#!pip install --upgrade google-generativeai
#!pip install mistralai


# Set the API key
os.environ['ANTHROPIC_API_KEY'] = userdata.get('ANTHROPIC_API_KEY')
os.environ['GOOGLE_API_KEY'] = userdata.get('GOOGLE_API_KEY')
os.environ['OPENAI_API_KEY'] = userdata.get('OPENAI_API_KEY')
os.environ['TOGETHER_API_KEY'] = userdata.get('TOGETHER_API_KEY')
os.environ['MISTRAL_API_KEY'] = userdata.get('MISTRAL_API_KEY')

#models
# https://inspect.ai-safety-institute.org.uk/
# https://docs.anthropic.com/en/docs/about-claude/models 
# https://ai.google.dev/gemini-api/docs/models/gemini 
# https://docs.mistral.ai/getting-started/models/models_overview/
# https://api.together.ai/models 


# Run the inspect command

# English

#!inspect eval mmlu.py --model openai/gpt-4o-2024-08-06	--limit 1000
#!inspect eval mmlu.py --model anthropic/claude-3-5-sonnet-20240620	--limit 1000
#!inspect eval mmlu.py --model google/gemini-1.5-pro-002 --limit 1000
#!inspect eval mmlu.py --model together/meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo --limit 1000
#!inspect eval mmlu.py --model mistral/mistral-large-latest --limit 1000
# for o1-preview only temperature=1 allowed
# !inspect eval mmlu_temperature1.py --model openai/o1-preview-2024-09-12 --limit 1000
#!inspect eval mmlu.py --model together/meta-llama/Llama-3.2-90B-Vision-Instruct-Turbo --limit 1000

# Latvian

#!inspect eval mmlu_lv.py --model openai/gpt-4o-2024-08-06	--limit 1000
#!inspect eval mmlu_lv.py --model anthropic/claude-3-5-sonnet-20240620	--limit 1000
#!inspect eval mmlu_lv.py --model google/gemini-1.5-pro-002 --limit 1000
#!inspect eval mmlu_lv.py --model together/meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo --limit 1000
#!inspect eval mmlu_lv.py --model mistral/mistral-large-latest --limit 1000
# for o1-preview only temperature=1 allowed
#!inspect eval mmlu_lv_temperature1.py --model openai/o1-preview-2024-09-12 --limit 1000

# Latvian redacted

#!inspect eval mmlu_lv_redacted.py  --model openai/gpt-4o-2024-08-06	--limit 1000
#!inspect eval mmlu_lv_redacted.py --model anthropic/claude-3-5-sonnet-20240620	--limit 1000
#!inspect eval mmlu_lv_redacted.py  --model google/gemini-1.5-pro-002 --limit 1000
#!inspect eval mmlu_lv_redacted.py  --model together/meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo --limit 1000
#!inspect eval mmlu_lv_redacted.py  --model mistral/mistral-large-latest --limit 1000
# for o1-preview only temperature=1 allowed
#!inspect eval mmlu_lv_redacted_temperature1.py --model openai/o1-preview-2024-09-12 --limit 1000


# Latvian redacted, temperature = 1
#!inspect eval mmlu_lv_redacted_temperature1.py  --model openai/gpt-4o-2024-08-06	--limit 1000
#!inspect eval mmlu_lv_redacted_temperature1.py --model anthropic/claude-3-5-sonnet-20240620	--limit 1000
#!inspect eval mmlu_lv_redacted_temperature1.py  --model google/gemini-1.5-pro-002 --limit 1000
#!inspect eval mmlu_lv_redacted_temperature1.py  --model together/meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo --limit 1000
#!inspect eval mmlu_lv_redacted_temperature1.py  --model mistral/mistral-large-latest --limit 1000



# Other models

#!inspect eval mmlu_lv.py --model openai/o1-mini-2024-09-12		--limit 50
#!inspect eval mmlu_lv.py --model anthropic/claude-3-haiku-20240307 --limit 50
#!inspect eval mmlu_lv.py --model google/gemini-1.5-flash-002	--limit 50
#!inspect eval mmlu_lv.py --model openai/gpt-4o-mini-2024-07-18	--limit 50
#!inspect eval mmlu_lv.py --model openai/gpt-4o-realtime-preview-2024-10-01	--limit 50
