# Multilingual LLM Evaluation: MMLU in Low-Resource Languages

## Overview

This repository contains evaluation code for testing large language model (LLM) performance across multiple languages using translated MMLU benchmark questions. The project specifically focuses on comparing model performance between English and lower-resource languages (Latvian and Giriama).

## Project Details

- **Dataset**: 112 randomly selected questions from the MMLU benchmark
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

- Limited sample size (112 questions)
- Focus on specific language pairs
- Experimental nature of translations in low-resource languages

## Notes
USed AISI Inspect framework, and base code for MMLU evals:
https://github.com/UKGovernmentBEIS/inspect_evals/blob/main/src/inspect_evals/mmlu/mmlu.py 

If you use or adapt this code for your research, please reach out to the author regarding proper attribution and citation details.

Earlier version and shorter of the paper whic did not include Giriama aviable here:
https://github.com/akanepajs/capabilities_lv_giriama/blob/main/Benchmarking%20Frontier%20LLM%20Understanding%20in%20Latvian.pdf

Please cite the earlier version as:

```bibtex
@article{kanepajs2024benchmarking,
  title={Benchmarking Frontier LLM Understanding in Latvian},
  author={Kanepajs, Arturs},
  year={2024}
}
```
