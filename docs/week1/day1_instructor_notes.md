# Day 1 Instructor Notes

## Teaching notes (plain-language approach)

When students are new to data management, keep explanations short and concrete:
- Start with the idea that data has a “life after the lab”: future users need context.
- Use “file + meaning” as a repeated phrase: the goal is not only the file, but what the file means.

## Where to pause for discussion

Suggested pause points:
1. After “Common data challenges”: ask students to name one dataset or project where context was missing.
2. After “OLTP vs OLAP”: ask whether their course experiences feel more like OLTP (transaction-focused) or OLAP (analysis-focused).
3. During FAIR: after each principle, ask for a one-sentence example from daily life (e.g., “Findable means you can locate it again.”).

## Common misunderstandings

1. **“FAIR means open access only.”**
   - Clarify: “Accessible” can include restricted access; the key point is that access conditions and metadata remain usable.
2. **“Interoperable means using the same file type only.”**
   - Clarify: it also includes shared semantics (meaning), formats, and vocabularies.
3. **“Reusable only matters for licensing.”**
   - Clarify: reusability also depends on documentation and provenance.

## How to explain FAIR in simple language

Use this short pattern for each principle:
- **Findable:** can the right person discover it?
- **Accessible:** can it be retrieved under stated conditions?
- **Interoperable:** can it be understood and combined with other data?
- **Reusable:** can someone use it correctly (license + documentation)?

Then connect to metadata as a bridge:
- “FAIR is achieved through many practices; metadata is one of the main tools that makes FAIR work.”

## Optional live questions (fast checks)

1. If a dataset has no DOI, is it automatically not Findable?
2. If a dataset is behind a permission request, is it still “Accessible”?
3. If a dataset has a downloadable file but no explanation of units, which FAIR principle is weakened?

