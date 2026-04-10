# Week 3 – Day 1: Tableau Prep Practice Questions

## 1. Short introduction

**Tableau Prep** lets you build a **visual, step-by-step** data-cleaning workflow: you see the data change after each operation, similar to the logic you practiced in Python (profiling, fixing, validating).

This sheet connects **Chapter 3: Data cleaning** ideas to a **low-code** environment. The goal is not memorizing every button—it is to **think** like an analyst: *What is wrong? What rule fixes it? How do I check the result?*

**Dataset to use (same idea as the Week 3 Day 1 notebook):**  
Import `../../data/week3/week3_messy_data.csv` from this notebook folder (or `data/week3/week3_messy_data.csv` from the repository root). Retail-style **orders**: `order_id`, `customer_id`, `order_date`, `city`, `category`, `quantity`, `order_amount`, `shipping_days`, `department`, `line_total`. If that file is not on your machine yet, run `01_in_class_data_cleaning_fundamentals.ipynb` once to generate it, or ask your instructor for the CSV.

---

## 2. Suggested practical questions

Work through the questions **in order** (easier → slightly more advanced).

**1. Data inspection — missing and messy fields**  
In the Profile pane, which columns show nulls or empty values? Which text columns show inconsistent formatting or spelling (e.g. city, category, department)?

*Instructor note:* Students should name columns and give examples. *Why it matters:* You fix only what you can see. *Expected:* e.g. gaps in `quantity`, `shipping_days`, or `line_total`; messy `city` / `category` / `department`.

**2. Data inspection — duplicates and suspicious values**  
Are there duplicate **rows**? Which **numeric** fields look suspicious (negative amounts, one value far from the rest, odd dates)?

*Instructor note:* Links to `duplicated()` and outlier thinking in Python. *Expected:* At least one duplicate pair; call out `order_amount` and/or invalid `order_date` patterns.

**3. Missing data — strategy**  
For each column with missing values, decide: **drop row**, **fill**, or **keep null and flag**. Briefly justify each choice.

*Instructor note:* Stress trade-offs (bias vs information loss). *Expected:* e.g. fill `quantity` with median or 1; fill `shipping_days` with median; impute `category` with mode only if agreed; consider flagging “was missing.”

**4. Missing data — how to fill**  
If you fill missing `quantity`, would you use **mean**, **median**, **mode**, or a **fixed value**? Why?

*Instructor note:* Same lesson as the notebook (median resists outliers). *Expected:* One choice + one sentence of reasoning.

**5. Duplicates**  
Detect and remove **exact** duplicate rows. Record **row count before** and **after**. Should every duplicate always be deleted automatically—why or why not?

*Instructor note:* Two numbers required; second part tests judgment (legitimate repeat orders). *Expected:* Before/after counts; one risk example.

**6. Standardization — cities and labels**  
Find labels that mean the same place (e.g. **NYC**, **New York**, **new york**). Describe your **rule** to standardize (trim, case, replacement map).

*Instructor note:* Logic before clicks. *Expected:* One canonical form + ordered steps.

**7. Standardization — dates and text**  
Put all valid `order_date` values into **one** readable format. What do you do with **unparseable** dates? Then trim spaces and normalize case for **`category`** or **`department`** and note how **distinct values** changed.

*Instructor note:* Mirrors ISO dates and string cleanup in Python. *Expected:* Date policy stated; fewer distinct categories after cleanup.

**8. Outliers**  
Which `order_amount` values look like **outliers**? How did you **see** them in Prep (profile, sort, filter)? For one outlier: keep, remove, replace, or escalate—and why?

*Instructor note:* Visual inspection ≈ boxplot logic. *Expected:* No single “right” answer; must show reasoning.

**9. Transformation — binning**  
Create a **binned** field from `order_amount` (e.g. Low / Medium / High). What cutoffs did you use?

*Instructor note:* Connects to `pd.cut`. *Expected:* Explicit thresholds or quantiles + labels.

**10. Transformation — calculated field**  
Create a simple new field, e.g. **spend per unit** = `order_amount` / `quantity`, with a safe rule for **zero or null quantity**.

*Instructor note:* Same as feature generation in the notebook. *Expected:* Formula in words + null/zero handling.

**11. Transformation vs Python**  
Which numeric columns might still need **scaling** later in **Python** for ML, even if you do not scale in Prep?

*Instructor note:* Different scales → distance-based models. *Expected:* e.g. `order_amount`, `quantity`, `shipping_days`, `line_total`.

**12. Validation and export**  
List **three checks** that prove the data is cleaner than at the start. What do you verify **before exporting** the final file?

*Instructor note:* “Assert” mindset. *Expected:* e.g. fewer nulls, no full-row duplicates, cleaner cities/dates; export checklist (row count, spot-check rows).

---

## 3. Instructor notes / expected thinking (summary)

| Theme | What students should practice |
|--------|-------------------------------|
| Inspection | Evidence first (Profile); name columns and examples. |
| Missing data | Per-column strategy; know cost of drop vs fill. |
| Duplicates | Count before/after; question blind auto-delete. |
| Standardization | One label per entity; one date format; document bad dates. |
| Outliers | Visual discovery; domain judgment. |
| Transformation | Bins and ratios mirror Python. |
| Validation | Repeatable checks before output. |

---

## 4. Final reflection

1. Which cleaning problem was **easiest to detect** in Tableau Prep, and why?

2. Which problem still required **human judgment** (no single button was enough)?

3. When would you prefer **Tableau Prep**, and when would you prefer **Python**?

---

## Suggested Tableau Prep workflow

1. **Input** — Connect to `week3_messy_data.csv`.  
2. **Inspect** — Profile all columns; note nulls, types, and distributions.  
3. **Clean missing values** — Per column: remove, fill, or flag.  
4. **Remove duplicates** — Exact duplicates first; record row counts.  
5. **Standardize fields** — Trim, case, parse dates, map labels (cities, departments).  
6. **Validate** — Re-check nulls, distinct values, and a sample of rows.  
7. **Output** — Export cleaned data (or publish per course instructions).
