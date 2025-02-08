# Multilingual LLM Evaluation: MMLU in Low-Resource Languages

## Overview

This repository contains evaluation code for testing large language model (LLM) performance across multiple languages using translated MMLU benchmark questions. The project specifically focuses on comparing model performance between English and lower-resource languages (Latvian and Giriama).

## Project Details

- **Dataset**: 500 randomly selected questions from the MMLU benchmark
- **Languages**:
  - English (original)
  - Latvian (machine-translated)
  - Latvian (machine-translated + human-edited)
  - Giriama
- **Primary Goal**: Assess and compare LLM performance across languages with varying levels of resources
- **Research Focus**: Understanding capability gaps between high-resource (English) and lower-resource languages

## Research Status

This is an academic research project with results currently under peer review. The evaluation code is publicly available, but the final results and detailed findings are being withheld pending publication. For research-related inquiries or result discussions, please contact the author.

## Limitations

- Limited sample size (500 questions)
- Focus on specific language pairs
- Experimental nature of translations in low-resource languages

## Notes
USed AISI Inspect framework, and base code for MMLU evals:
https://github.com/UKGovernmentBEIS/inspect_evals/blob/main/src/inspect_evals/mmlu/mmlu.py 

Run e.g. as follows:

```
import os
from google.colab import userdata
!pip install inspect-ai
os.environ['ANTHROPIC_API_KEY'] = userdata.get('ANTHROPIC_API_KEY')
os.environ['GOOGLE_API_KEY'] = userdata.get('GOOGLE_API_KEY')
os.environ['OPENAI_API_KEY'] = userdata.get('OPENAI_API_KEY')
os.environ['MISTRAL_API_KEY'] = userdata.get('MISTRAL_API_KEY')
os.environ['TOGETHER_API_KEY'] = userdata.get('TOGETHER_API_KEY')

%cd /content
os.environ['LANGUAGE'] = 'latvian'
!inspect eval mmlu.py@mmlu_0_shot --model together/deepseek-ai/DeepSeek-R1 --log-dir ./DeepSeek-R1 -T cot=false
```
