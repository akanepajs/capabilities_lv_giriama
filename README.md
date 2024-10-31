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

## Usage

The main evaluation script can be executed via:
```bash
python capabilities_lv_giriama.py
```

## Research Status

This is an academic research project with results currently under peer review. The evaluation code is publicly available, but the final results and detailed findings are being withheld pending publication. For research-related inquiries or result discussions, please contact the author.

## Contact

**Author**: Arturs Kanepajs  
**Email**: akanepajs@gmail.com  
**Date**: October 2024

## Limitations

- Limited sample size (112 questions)
- Focus on specific language pairs
- Experimental nature of translations in low-resource languages

## Notes

If you use or adapt this code for your research, please reach out to the author regarding proper attribution and citation details.

Earlier version and shorter of the paper whic did not include Giriama aviable here:
Please cite as:

@article{kanepajs2024benchmarking,
  title={Benchmarking Frontier LLM Understanding in Latvian},
  author={Kanepajs, Arturs},
  year={2024}
}



