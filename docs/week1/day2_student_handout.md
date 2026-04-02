# Day 2 Student Handout (Metadata and Practice)

## Concise definitions

**Metadata** is information that describes data. It helps others understand, find, and reuse datasets.

**FAIR connection (simple):**
- Metadata supports **Findability** (what it is + identifiers).
- Metadata supports **Reusability** (how to interpret it + usage rules).

## Types of metadata

1. **Descriptive metadata**: what the dataset is about (title, description, keywords).
2. **Structural metadata**: how the dataset is organized (e.g., columns, file structure).
3. **Administrative metadata**: access and management details (license, version, contacts).

## Short examples

### Dublin Core (XML fragments)

```xml
<dc:title>2025 Global Climate Data</dc:title>
<dc:creator>Global Climate Data Team</dc:creator>
<dc:identifier>10.1234/gcd-2025</dc:identifier>
<dcterms:description>Fictional annual climate summaries for two countries...</dcterms:description>
```

### DataCite (XML fragments)

```xml
<identifier identifierType="DOI">10.1234/gcd-2025</identifier>
<creators>
  <creator><creatorName>Global Climate Data Team</creatorName></creator>
</creators>
<titles><title>2025 Global Climate Data</title></titles>
<publicationYear>2025</publicationYear>
```

### schema.org (JSON-LD fragments)

```json
{
  "@type": "Dataset",
  "name": "2025 Global Climate Data",
  "identifier": "10.1234/gcd-2025"
}
```

### Dublin Core (example fields)
- `title`, `creator`, `publisher`, `description`, `subject`, `identifier`

### DataCite (example fields)
- `identifier` (often a DOI), `creators`, `title`, `publisher`, `publicationYear`, `resourceType`, `description`

### schema.org (JSON-LD) (example fields)
- `@type` (e.g., `Dataset`), `name`, `description`, `creator`, `publisher`, `identifier`, `keywords`

## A mini comparison table

| Standard | Typical focus | Example field emphasis |
|---|---|---|
| Dublin Core | general resource description | `title`, `creator`, `description` |
| DataCite | citations and DOI-based citation | `identifier`, `creators`, `publicationYear` |
| schema.org | discovery on the web | `@type`, `name`, `keywords`, `distribution` |

## Review questions (5)

1. Give one sentence: what is metadata?
2. Which metadata type would you use to explain who should have access to the dataset?
3. Which standard is most directly tied to DOI citation metadata?
4. Why might schema.org metadata be useful even when the dataset is also in a repository?
5. Think of one FAIR principle that metadata directly supports. Explain how.

