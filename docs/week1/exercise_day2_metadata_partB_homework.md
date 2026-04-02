# Homework (Day 2, Part B): Create Metadata for a Dataset of Your Choice

## Objective

Each student selects a public dataset of their choice and creates:
- **one DataCite XML** metadata file, and
- **one schema.org JSON-LD** metadata file with `@type` set to `Dataset`.

The goal is not to produce a perfect metadata record, but to practice selecting fields that support FAIR **Findability** and **Reusability**.

## Deliverables

Submit two files:
1. DataCite XML file (example: `datacite_metadata_mydata.xml`)
2. schema.org JSON-LD file (example: `schemaorg_metadata_mydata.jsonld`)

## Submission instructions

Upload your files (as text) to your course platform.

Include any short field explanations in a `README` text file, if your instructor requests it.

## Naming convention

Use:
- `datacite_metadata_<studentname>_<datasetname>.xml`
- `schemaorg_metadata_<studentname>_<datasetname>.jsonld`

Use lowercase letters and replace spaces with underscores in `<datasetname>`.

## Evaluation criteria (simple rubric)

1. **Correctness (structure):** XML and JSON-LD are syntactically valid.
2. **Completeness (core fields):** includes required teaching fields (title, creator, identifier, description).
3. **Clarity (meaning):** field values match what the dataset actually contains.
4. **FAIR connection:** you used the fields to improve Findability and/or Reusability.

## Suggested workflow (beginner-friendly)

1. Find a public dataset and locate its persistent identifier (preferably a DOI).
2. Copy key details:
   - title,
   - creators,
   - publisher (or repository),
   - publication year,
   - resource type (e.g., Dataset),
   - short description/abstract,
   - license/access terms if available.
3. Create the DataCite XML:
   - ensure you include `identifier`, `creators`, `title`, `publisher`, `publicationYear`, `resourceType`, `description`.
4. Create the schema.org JSON-LD:
   - set `@type` to `Dataset`,
   - include `name`, `description`, `creator`, `publisher`, `identifier` (or URL), and `keywords` if possible.
5. Do a quick “teaching demo” check:
   - Does your record include the key fields listed above?

## Common mistakes to avoid

- Using a temporary URL instead of a persistent identifier (if a DOI exists).
- Confusing metadata fields with actual data values.
- Copying the wrong title/creator (e.g., a paper title instead of dataset title).
- Leaving `description` empty or meaningless.

