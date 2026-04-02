## Data Management 1 (4-Week Teaching Repository)

Welcome to **Data Management 1**, a beginner-friendly teaching repository focused on how to manage data responsibly in academic and professional settings. The course emphasizes the practical meaning of **FAIR principles**, the role of **DOIs and repositories**, and the foundations of **metadata** (including **Dublin Core**, **DataCite**, and **schema.org**).

### Repository purpose

This repository helps students and instructors:
- understand why data management matters,
- apply FAIR principles in an evidence-based way,
- interpret how DOIs and repositories support persistent access and citation,
- and practice parsing and comparing metadata standards locally with Python.

### Target audience

This repository is designed for:
- University students in **data management / data science** with basic Python familiarity
- Instructors who want a structured, reproducible teaching setup for Week 1

### Current scope

- **Week 1 is fully implemented**
- **Weeks 2–4 are scaffolded only** (placeholders with TODO notes)

### What you will learn (Week 1)

By the end of Week 1, students should be able to:
- Explain why data management matters and identify common data challenges
- Interpret and apply the **FAIR** principles (Findable, Accessible, Interoperable, Reusable)
- Understand what **metadata** is, why it matters, and the difference between metadata types
- Compare **Dublin Core**, **DataCite**, and **schema.org** in practical terms
- Access and parse metadata examples using Python (locally, without internet access)
- Connect metadata quality to **FAIR Findability and Reusability**

### Week 1 overview

- **Day 1 (Foundations and FAIR):** Data management basics up to FAIR principles, ending with an in-class FAIR assessment activity.
- **Day 2 (Metadata and Practice):** A metadata-focused day with multiple parsing notebooks and a structured in-class + homework exercise.

### Repository contents (quick tree)

Key folders:
- `docs/` — teaching materials and exercises
- `data/` — sample datasets and example metadata files
- `notebooks/` — Week 1 Jupyter notebooks
- `src/` — lightweight Python helper scripts imported by notebooks
- `slides_support/` — ready-to-use lecture support snippets
- Week structure:
  - `docs/week1/` — fully implemented Day 1 and Day 2 materials + exercises + rubrics
  - `docs/week2/`, `docs/week3/`, `docs/week4/` — TODO-only placeholders for later expansion

Full top-level tree (overview):

```text
data-management-1/
├── README.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── environment.yml
├── docs/
│   ├── course_overview.md
│   ├── teaching_plan_4_weeks.md
│   ├── assessment_notes.md
│   ├── week1/   (Day 1 + Day 2 fully implemented)
│   ├── week2/   (TODO placeholder)
│   ├── week3/   (TODO placeholder)
│   └── week4/   (TODO placeholder)
├── data/
│   ├── raw/         (sample CSVs)
│   ├── metadata/   (Dublin Core, DataCite, schema.org examples)
│   └── repository_examples/
├── notebooks/
│   └── week1/      (offline teaching notebooks)
├── src/            (parsers + validators)
└── slides_support/ (Week 1 lecture support snippets)
```

### Installation

#### Option A: `pip` (recommended for beginners)

```bash
cd "data-management-1"
python -m pip install -r requirements.txt
```

#### Option B: Conda (optional)

```bash
cd "data-management-1"
conda env create -f environment.yml
conda activate data-management-1
```

### How to run notebooks

From the repository root (`data-management-1/`):

```bash
jupyter notebook
```

Then open the notebooks under `notebooks/week1/`.

Notes:
- Notebooks are written to use **relative paths** to `data/`
- The notebooks are intended to run **offline** (no live API calls required)

### How to use the sample metadata files

Example metadata files are stored in:
- `data/metadata/`

They describe the same dataset (**“2025 Global Climate Data”**) in three formats:
- Dublin Core XML (`climate_dataset_dublin_core.xml`)
- DataCite XML (`climate_dataset_datacite.xml`)
- schema.org JSON-LD (`climate_dataset_schemaorg.jsonld`)

The Week 1 notebooks show how to:
- parse these files with Python
- convert them into Python dictionaries / tables
- compare metadata coverage across standards
- perform lightweight “teaching demo” completeness checks

### Teaching philosophy

This course repository prioritizes:
- **Practical understanding over theory**
- **Small, reproducible examples**
- **Clear learning objectives**
- **Student inspection and iteration**

### Future expansion

In Weeks 2–4, you will extend the teaching repository with additional real-world activities such as:
- data stewardship workflows
- more advanced metadata modeling and validation
- dataset documentation and licensing scenarios
- more FAIR assessment practice

For now, Weeks 2–4 contain only placeholders so you can add your own content later.

---

## Notes for instructors and students: recommended workflow

Instructor workflow:
- Assign Day 1 reading/handouts and run the Day 1 notebooks only as needed
- Use the classroom exercises in `docs/week1/` to guide discussion
- Use the helper scripts in `src/` to keep parsing logic consistent across notebooks

Student workflow:
- Read the relevant `docs/week1/` handouts
- Run notebooks top-to-bottom for the day
- Complete exercises using provided templates and sample metadata files

