---
task_categories:
- text-classification
- text-generation
- question-answering
language:
- en
tags:
- medical
pretty_name: Gut-Health-DPO
size_categories:
- n<1K
---
# Gut Health DPO Dataset

## Overview

This dataset contains 200 carefully curated examples for Direct Preference Optimization (DPO) training in the domain of gut health and digestive wellness. Each example consists of a user prompt, a "chosen" response (preferred), and a "rejected" response (less preferred), designed to train AI models to provide high-quality, medically responsible advice on digestive health topics.

## Dataset Structure

The dataset is provided in CSV format with three columns:
- `prompt`: User questions about gut health, digestion, and related symptoms
- `chosen`: High-quality responses that demonstrate preferred answering style
- `rejected`: Lower-quality responses that show less preferred approaches

## Topics Covered

The dataset spans a wide range of gut health topics including:
- Acid reflux and GERD
- Food intolerances and sensitivities
- Probiotics and prebiotics
- Dietary fiber management
- Menstrual cycle and digestive health
- Exercise and digestion
- Stress and gut health
- Pediatric digestive issues
- Post-surgical digestive care
- Chronic conditions (IBS, IBD, Crohn's disease)

## Key Characteristics

### Preferred Responses ("chosen"):
- Empathetic and conversational tone
- Evidence-based information
- Clear recommendations to consult healthcare providers
- Balanced discussion of benefits and limitations
- Practical, actionable advice
- Appropriate disclaimers for medical information

### Less Preferred Responses ("rejected"):
- Overly clinical or impersonal tone
- Making definitive medical claims without disclaimers
- Providing treatment recommendations without medical consultation advice
- Overly simplistic or potentially misleading information

## Intended Use

This dataset is designed for:
- Training and fine-tuning LLMs for healthcare and wellness applications
- Improving AI responses in digestive health domains
- Research in medical AI safety and preference optimization
- Developing responsible AI for health-related queries

## Important Considerations

⚠️ **Medical Disclaimer**: This dataset contains health-related information for training purposes only. The responses should not be considered medical advice. Always consult qualified healthcare professionals for medical concerns.

## Citation

If you use this dataset in your research or applications, please acknowledge its use appropriately.

## Dataset Details

- **Number of examples**: 200
- **Format**: CSV
- **Language**: English
- **Domain**: Healthcare / Gut Health / Digestive Wellness