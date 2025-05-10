# Unveiling Bias in University Recommendations  
### A Study on Geographic and Educational Preferences in Open-Source Language Models

## 🔍 Overview

This project investigates potential demographic biases in university and academic program recommendations produced by instruction-tuned Large Language Models (LLMs). We evaluate the outputs from:

- **Meta LLaMA-3.1-8B-Instruct**
- **Google Gemma-7B-it**
- **Mistral-7B-Instruct-v0.3**

By systematically altering user identity attributes (gender, nationality, and economic class), this study reveals trends in how model recommendations vary and potentially favor specific regions, institutions, or academic fields.

---

## 🎯 Objectives

- To examine the influence of demographic factors on LLM-generated educational recommendations.
- To detect and quantify over-representation and under-representation biases in universities, programs, and countries.
- To compare the fairness and behavior of multiple LLMs under uniform prompting conditions.
- To visualize model outputs across global and demographic dimensions.

---

## 📁 Project Directory Structure

```

project\_root/
│
├── gemma-7b/
│   ├── responses\_gemma\_7b.json
│   ├── responses\_gemma\_7b.xlsx
│   ├── responses\_gemma\_7b\_cleaned.xlsx
│   └── plots/
│
├── mistral-7b/
│   ├── responses\_mistral\_7b.json
│   ├── responses\_mistral\_7b.xlsx
│   ├── responses\_mistral\_7b\_cleaned.xlsx
│   └── plots/
│
├── llama-8b/
│   ├── responses\_llama\_8b.json
│   ├── responses\_llama\_8b.xlsx
│   ├── responses\_llama\_8b\_cleaned.xlsx
│   └── plots/
│
├── util/
│   └── ne\_10m\_admin\_0\_countries/
│       ├── ne\_10m\_admin\_0\_countries.shp
│       ├── ne\_10m\_admin\_0\_countries.dbf
│       ├── ne\_10m\_admin\_0\_countries.shx
│       ├── ne\_10m\_admin\_0\_countries.prj
│       ├── ne\_10m\_admin\_0\_countries.cpg
│       └── ne\_10m\_admin\_0\_countries.README.html
│
├── world\_map.py                  ← Geographic visualization (country heatmaps)
├── util.py                       ← Plotting tools (bar plots, word clouds, heatmaps)
├── prompting-model.ipynb         ← Prompt generation and model querying
├── parsing-model-responses.ipynb ← JSON to XLSX parser and cleaner
├── analysis-model-responses.ipynb← Comparative visualization and analysis
├── prompt-template.txt           ← Standardized input prompt format
├── requirements.txt              ← Python dependencies
└── README.md                     ← Project documentation

````

---

## 🧪 Methodology

### Prompt Design
- 360 unique prompts were created from:  
  `3 Genders × 40 Nationalities × 3 Economic Classes`
- Each was repeated **10 times**, leading to **3600 prompts per model**.

### Response Collection
- Model outputs were saved in `.json` format.
- Files are stored per model (`gemma-7b/`, `mistral-7b/`, `llama-8b/`).

### Data Cleaning & Structuring
- Responses were parsed into `.xlsx` files for processing.
- Cleaned `.xlsx` versions were used for analysis and plotting.

### Bias Evaluation & Visualization
- Statistical frequency analysis of universities and countries.
- Cosine similarity between group outputs.
- Visual outputs: bar plots, heatmaps, word clouds, and choropleth maps.

---

## 🌍 Geo-Visualization

- Utilizes [Natural Earth](https://www.naturalearthdata.com/downloads/10m-cultural-vectors/) shapefiles for rendering world maps.
- `world_map.py` uses `geopandas` and fuzzy matching to map recommended countries.
- Output maps show the number of mentions of each country across all responses.

---

## ⚙️ Installation

### Step 1: Set up environment

```bash
python -m venv env
source env/bin/activate  # Windows: .\env\Scripts\activate
````

### Step 2: Install required libraries

```bash
pip install -r requirements.txt
```

---

## 📄 License & Attribution

* Shapefiles: [Natural Earth Data](https://www.naturalearthdata.com) – Public Domain
* Models accessed via: [HuggingFace Transformers](https://huggingface.co/models)

---