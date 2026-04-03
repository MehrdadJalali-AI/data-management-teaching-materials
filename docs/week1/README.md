# Week 1 notebooks — Data Management 1

This folder contains **Jupyter notebooks** for **Week 1** of *Data Management 1*: **FAIR principles** (Day 1) and **metadata** (Day 2), using the teaching dataset **“2025 Global Climate Data”** and files under `../../data/`.

---

## Suggested order

| Order | Notebook | Session |
|------:|----------|---------|
| 1 | `01_day1_fair_demo.ipynb` | Day 1 |
| 2 | `02_day2_intro_to_metadata.ipynb` | Day 2 |
| 3 | `03_day2_dublin_core_parsing.ipynb` | Day 2 |
| 4 | `04_day2_datacite_parsing.ipynb` | Day 2 |
| 5 | `05_day2_schemaorg_processing_refined.ipynb` | Day 2 |
| 6 | `06_day2_compare_metadata_standards.ipynb` | Day 2 |
| 7 | `07_day2_mini_metadata_validation.ipynb` | Day 2 |

Run notebooks **top to bottom** unless your instructor says otherwise.

---

## What each notebook does

### Day 1

**`01_day1_fair_demo.ipynb`** — *FAIR principles analysis of a sample dataset*  
Step-by-step classroom demo: inspect a dataset and its metadata, run basic quality checks, apply a simple FAIR review framework (**Findable**, **Accessible**, **Interoperable**, **Reusable**), score and summarize by principle, and discuss weaknesses and improvements.  
Aim: understand FAIR **in practice**, not a formal production evaluator.

### Day 2

**`02_day2_intro_to_metadata.ipynb`** — *Introduction to metadata*  
Introduces **metadata** vs **data**, the three types (**descriptive**, **structural**, **administrative**), links to **Findability** and **Reusability**, and ties a small CSV to its description. Classroom-oriented, short steps.

**`03_day2_dublin_core_parsing.ipynb`** — *Dublin Core parsing, step by step*  
Locates and reads Dublin Core XML, explains **namespaces** and **local names**, builds small helpers, extracts main fields, turns them into a table, interprets them, connects to **FAIR**, and discusses weaknesses.

**`04_day2_datacite_parsing.ipynb`** — *Parsing DataCite metadata step by step*  
Shows what a **DataCite** XML record looks like, identifies key dataset fields, parses XML incrementally in Python, builds a clean table, and relates the record to **FAIR**.

**`05_day2_schemaorg_processing_refined.ipynb`** — *Processing schema.org metadata step by step*  
Loads **JSON-LD**, finds the **Dataset** record, inspects important **schema.org** fields, builds a parser, tabulates results, highlights **FAIR**-relevant fields, checks completeness, and suggests discussion points.

**`06_day2_compare_metadata_standards.ipynb`** — *Comparing Dublin Core, DataCite, and schema.org*  
Uses the same teaching dataset in three formats: preview files, parse each with lightweight helpers, build a **shared comparison table**, interpret coverage, discuss **FAIR**, limitations, and class questions.

**`07_day2_mini_metadata_validation.ipynb`** — *Mini metadata validation (teaching demo)*  
**Not** a formal validator: defines files, previews raw metadata, parses three records, focuses on important fields, runs a **simple checklist**, computes a **completeness score**, surfaces missing fields, interprets from a **FAIR** angle, and supports classroom discussion.

---

## Dependencies

- **Python 3** with **pandas** and **Jupyter** (see repository root `requirements.txt`).
- Standard library: e.g. `pathlib`, `json`, `xml.etree.ElementTree`, `urllib` (as used inside notebooks).

---

## Data files

Notebooks expect teaching files under the repo’s **`data/`** tree, for example:

- `data/raw/climate_sample.csv`
- `data/metadata/climate_dataset_dublin_core.xml`
- `data/metadata/climate_dataset_datacite.xml`
- `data/metadata/climate_dataset_schemaorg.jsonld`

Paths inside notebooks are written for running from this **`notebooks/week1/`** location (or equivalent working directory). If a path fails, open the notebook and check the **“Step 1”** or path-definition cells.

---

## Google Colab and GitHub

Notebooks **`02` through `07`** begin with a **bootstrap** code cell that downloads missing files from a **raw GitHub** base when local copies are absent (configure `GITHUB_RAW_BASE` in that cell to match your fork or course repo).

**`01_day1_fair_demo.ipynb`** does **not** include that bootstrap in the current version; for Colab, upload the needed CSV/metadata files or clone the full repository and set working directory paths accordingly.

---

## For instructors

- **Day 1:** start with `01_day1_fair_demo.ipynb` and the matching materials in `docs/week1/`.  
- **Day 2:** use `02` → `07` in order for a coherent arc: concepts → three standards → comparison → lightweight validation.  
- Slides and handouts: `../../slides_support/week1/` and `../../docs/week1/`.

---

## For students

1. Install dependencies from the repository root.  
2. Open Jupyter from the repo (or use Colab with bootstrap where available).  
3. Open notebooks in the order above and **Run All** or run cell by cell as directed in class.

If anything fails on file paths, confirm you are in the correct folder and that `data/raw` and `data/metadata` exist (or run the bootstrap cell first for notebooks that provide it).
