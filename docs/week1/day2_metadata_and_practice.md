# Day 2: Metadata and Practice

## Learning objectives

By the end of Day 2, students should be able to:
1. Recall what **metadata** is and distinguish it from the data itself.
2. Explain why metadata matters for **Findability** and **Reusability** in FAIR.
3. Identify three broad **types of metadata**: descriptive, structural, and administrative.
4. Recognize the purpose of three common metadata standards:
   - **Dublin Core**
   - **DataCite**
   - **schema.org**
5. Interpret practical examples of Dublin Core, DataCite, and schema.org metadata.
6. Use Python to inspect and lightly validate metadata records (teaching demo).

## Lecture flow (suggested)

1. Quick recap of FAIR (10 min)
2. Transition: why FAIR needs metadata (15 min)
3. What is metadata? Intuitive explanation (20 min)
4. Types of metadata (15 min)
5. Metadata standards overview (30 min)
   - Dublin Core (descriptive, simple)
   - DataCite (citation + DOI-driven)
   - schema.org (web discovery + JSON-LD)
6. Comparison and interpretation of example records (25 min)
7. Wrap-up + linking back to FAIR (10 min)
8. Practical notebooks + in-class exercise (the remainder of the session)

## Intuitive explanation of metadata

If the dataset is the “what”, then metadata is the “about”:
- What does the dataset contain?
- Who created it?
- How should it be understood (units, fields, context)?
- Under what terms may it be reused?
- How can someone reliably cite and locate it?

Without metadata, even a well-designed dataset can become difficult to reuse because future users cannot interpret it.

## Real-world examples (short)

- Descriptive metadata: a title, keywords, an abstract/summary.
- Structural metadata: “there are columns `year`, `country`, and measurement columns”.
- Administrative metadata: licensing, version number, contact information, access conditions.

## Dublin Core vs DataCite vs schema.org (comparison)

| Standard | Typical purpose | Common fields you will see | Designed for |
|---|---|---|---|
| Dublin Core | Simple descriptive description | `title`, `creator`, `description`, `publisher`, `subject` | Broad resource description |
| DataCite | Citation metadata for DOIs | `identifier`, `creators`, `title`, `publisher`, `publicationYear`, `resourceType`, `description` | DOIs and scholarly citation |
| schema.org (JSON-LD) | Web discovery metadata | `@type`, `name`, `description`, `creator`, `identifier`, `keywords`, `distribution` | Search/discovery on the web |

## Practical interpretation of each (what to look for)

- **Dublin Core:** quick “human-readable” overview of what the dataset is.
- **DataCite:** citation details that support Findability and Reusability through DOI-based identification.
- **schema.org:** discovery cues and structured fields that help search engines and portals.

## Timing blocks (guideline)

Day 2 can be structured as:
- 10 min recap + discussion
- 45 min lecture + examples
- 60–90 min notebook practice (Dublin Core, DataCite, schema.org parsing)
- 30–45 min in-class exercise (metadata interpretation + improving a partial record)
- Remaining time: reflection and transition to homework

## Recap

Metadata is not “extra”; it is the mechanism that makes FAIR work in practice. On Day 2 you learned:
- what metadata is,
- the three major metadata types,
- and how different standards (Dublin Core, DataCite, schema.org) support FAIR Findability and Reusability in different ways.

