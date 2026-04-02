# Day 1: Foundations of Data Management and FAIR

## Learning objectives

By the end of Day 1, students should be able to:
1. Explain what **data management** means and why it matters.
2. Identify common data challenges in real projects (storage, documentation, access, and reuse).
3. Describe the benefits of good data management in plain language.
4. Distinguish **structured**, **semi-structured**, and **unstructured** data at an introductory level.
5. Provide a basic introduction to **OLTP vs OLAP** and the typical purpose of each.
6. Explain the **FAIR principles**: **Findable**, **Accessible**, **Interoperable**, and **Reusable**.
7. Prepare a short FAIR-oriented assessment summary for a public dataset.

## Timing (single session blocks)

Suggested total: ~3 hours (adjust as needed).

1. Welcome and course framing (10 min)
2. Why data management matters (25 min)
3. Data management basics and common challenges (20 min)
4. Data types and example use-cases (25 min)
5. OLTP vs OLAP, basic comparison (20 min)
6. Data sensitivity and protection (15 min)
7. FAIR principles (60 min)
   - Findable (15)
   - Accessible (15)
   - Interoperable (15)
   - Reusable (15)
8. In-class FAIR practical (55 min)
9. Wrap-up recap (10 min)

## Short lecture outline

### 1) Why data management matters (simple explanation)
Data management is the set of practices that ensure data can be understood, shared, and reused over time. Without good data management, valuable information can become hard to find, hard to access, difficult to combine with other datasets, or even unusable due to missing context.

### 2) Definition and core benefits
Data management includes:
- documenting data (what it is, how it was created, and how to interpret it),
- storing data securely and sustainably,
- enabling access for the intended audience,
- supporting reuse by others (including through identifiers and metadata).

Core benefits include:
- reduced duplication of effort,
- faster onboarding of new team members,
- improved reproducibility,
- higher scientific and operational impact.

### 3) Common data challenges
Typical challenges include:
- “We have the file, but nobody knows what it means.”
- “We can access it now, but not later.”
- “We cannot combine datasets because formats and definitions differ.”
- “We share data, but we miss key documentation (metadata).”

### 4) OLTP vs OLAP (intro level)
Use a simple mental model:
- **OLTP (Online Transaction Processing):** supports frequent updates (e.g., inserting new records). Priorities: fast writes and consistency.
- **OLAP (Online Analytical Processing):** supports analysis and reporting over time. Priorities: fast reads, aggregations, and analytics.

Intro example:
- A university database that stores new enrollment transactions is closer to OLTP.
- A dashboard that aggregates enrollment trends by year is closer to OLAP.

### 5) Types of data
- **Structured:** fixed schema (e.g., a table of measurements with named columns).
- **Semi-structured:** flexible structure with tags or key-value fields (e.g., JSON, XML).
- **Unstructured:** no fixed schema (e.g., text, images, audio). Usually requires additional processing to extract meaning.

### 6) Data sensitivity and protection (basic level)
Not all data can be treated the same way. Some datasets contain personal data or confidential information. Basic protection concepts:
- limit access based on legitimate need,
- follow licensing and ethical guidance,
- store securely,
- document sensitivity and any restrictions clearly.

### 7) FAIR principles (end of lecture focus)
FAIR means that data should be managed in ways that make it:

**Findable**
- Has a persistent identifier (e.g., a DOI).
- Includes searchable metadata.

**Accessible**
- The data can be retrieved using a standardized protocol.
- Even if access is restricted, metadata should remain accessible.

**Interoperable**
- Uses standards (e.g., common formats and vocabularies).
- Links to other resources.

**Reusable**
- Clear licensing and provenance.
- Sufficient documentation to allow others to reuse the data correctly.

## Simple examples (short, student-friendly)
1. Findable example: A dataset with a DOI and a searchable metadata record in a repository.
2. Accessible example: A dataset where the data files can be downloaded via a standard mechanism, and access terms are clearly described.
3. Interoperable example: A dataset using a documented data format and consistent units.
4. Reusable example: A dataset that includes a license and explains how variables were measured.

## Key terms
- **Data management:** practices for storing, documenting, securing, and sharing data for future use.
- **Metadata:** information about data (e.g., what a dataset contains and how to interpret it).
- **DOI / persistent identifier:** a long-lasting identifier used to locate digital resources.
- **FAIR:** Findable, Accessible, Interoperable, Reusable.
- **OLTP / OLAP:** two contrasting database purposes (transactions vs analysis).
- **Sensitivity / protection:** rules and safeguards for confidential or personal data.

## Mini discussion questions
1. What goes wrong when a dataset has no clear documentation?
2. In your experience, what is usually missing: the data file itself, or the context needed to interpret it?
3. Which FAIR principle do you think is hardest to achieve, and why?
4. Does “accessible” mean “open to everyone”? What could “restricted access” still mean?

## Recap (end-of-day summary)
Data management helps ensure that data remains understandable and usable over time. The FAIR principles provide a practical checklist: make data **Findable**, **Accessible**, **Interoperable**, and **Reusable**. On Day 1, we focus on understanding FAIR; Day 2 will connect FAIR to metadata in detail.

