# In-Class Exercise (Day 2, Part A): Improve a Dublin Core Record

## Objective

Students will:
- inspect the provided **climate dataset** CSV and metadata examples,
- interpret examples of **Dublin Core**, **DataCite**, and **schema.org**,
- complete or improve a partial **Dublin Core** record for the dataset.

## Estimated time

35–45 minutes

## Starter materials

Provided in the repository:
- Dataset CSV: `data/raw/climate_sample.csv`
- Metadata examples:
  - `data/metadata/climate_dataset_dublin_core.xml` (complete example)
  - `data/metadata/climate_dataset_datacite.xml`
  - `data/metadata/climate_dataset_schemaorg.jsonld`

Partial template to improve:
- `docs/week1/exercise_day2_metadata_partA_inclass.md` (template included below)

## Step-by-step instructions

1. Inspect the dataset CSV briefly (focus on columns and meaning).
2. Read the complete Dublin Core example (look for `dc:title`, `dc:creator`, `dcterms:description`, `dc:identifier`, etc.).
3. Use the DataCite and schema.org examples as “hints” for what information should appear in the Dublin Core record.
4. Fill in missing fields in the partial Dublin Core template.
5. Answer the short questions about your choices.

## Expected short answers (guided)

For the completed Dublin Core record, provide short answers:
1. What did you use as the dataset title and why?
2. What did you put into `dc:creator` and where did you get that information from?
3. Which identifier did you use (and what does it represent)?
4. What is one change you made to improve reusability (documentation/description/licensing)?

## Partial Dublin Core template (fill in the blanks)

Replace blanks (`___`) with correct values consistent with the dataset metadata examples.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<metadata
  xmlns:dc="http://purl.org/dc/elements/1.1/"
  xmlns:dcterms="http://purl.org/dc/terms/">

  <dc:title>___</dc:title>

  <dc:creator>___</dc:creator>

  <dc:publisher>___</dc:publisher>

  <dc:identifier>___</dc:identifier>

  <dcterms:description>
    ___
  </dcterms:description>

  <dc:subject>___</dc:subject>

  <dc:date>___</dc:date>
</metadata>
```

## Extension question (one optional extra)

If Dublin Core is “simple description,” what extra information would DataCite add for DOI-based citation, and how would that help Findability or Reusability?

