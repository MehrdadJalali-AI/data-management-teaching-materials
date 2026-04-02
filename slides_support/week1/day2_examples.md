# Week 1 Day 2: Ready-to-use Metadata Examples

## One “bad metadata” example (illustrative)

Common problems:
- missing `title` (only a filename is used),
- `creator` is blank or contains an institutional page instead of a person/group,
- `identifier` is a temporary download URL rather than a persistent identifier,
- `description` is a vague sentence (“data for research”) with no context.

## One “improved metadata” example (illustrative)

Improvements:
- uses a clear, human-readable title,
- includes creator(s) names,
- includes a persistent identifier (e.g., DOI),
- provides a short description of what the dataset contains and what each variable means.

## Comparison-ready note

For a teaching dataset, the three standards often map like this:
- `title` -> Dublin Core `dc:title`, DataCite `titles/title`, schema.org `name`
- `creator` -> Dublin Core `dc:creator`, DataCite `creators/creator/name`, schema.org `creator`
- DOI/identifier -> Dublin Core `dc:identifier`, DataCite `identifier`, schema.org `identifier`
- abstract/description -> Dublin Core `dcterms:description`, DataCite `descriptions/description`, schema.org `description`

