# Oklahoma Career Skills Matcher

A rule-based Streamlit prototype that compares skills you enter with example
skill lists for selected industry categories.

**This is an independent portfolio project.** It is **not affiliated with or
endorsed by** the Oklahoma Employment Security Commission (OESC) or the U.S.
Bureau of Labor Statistics (BLS). It uses example skill lists and does not
retrieve live labor-market data.

The app demonstrates Streamlit development and simple matching logic. It is
not a hiring tool, a job-readiness assessment, or career advice.

## Architecture

```text
Skills entered by the user
    |
    v
Split at commas, semicolons, or new lines
    |
    v
Normalize: lowercase, trim extra spaces, remove duplicates
    |
    v
Compare exact skill names with the selected example skill list
    |
    v
Display matched skills, skills to explore, and example certifications
```

The app calls no external service, uses no AI model, and saves no entries.

## Main capabilities

- Accepts skills separated by commas, semicolons, or new lines.
- Ignores capitalization, extra spaces, and duplicate entries.
- Compares entries with four example industry skill lists.
- Shows matched skills and skills to explore.
- Displays the percentage of example skills matched, with a clear caveat.
- Lists example certifications to research.
- Warns users not to enter sensitive personal information or a real résumé.

## Technology stack

| Component | Purpose |
|---|---|
| Python | Application logic and skill parsing |
| Streamlit | Browser interface |
| Python `re` module | Splitting skill entries |
| Python dictionaries | Example skills and certifications |

## Project structure

```text
oklahoma-career-skills-matcher/
|-- app.py                   Streamlit application and matching logic
|-- requirements.txt         Python package list
|-- results-screenshot.png   Screenshot shown in this README
|-- .gitignore               Files Git should not track
`-- README.md                Project documentation
```

## Requirements

- Windows with PowerShell.
- Python 3.12 recommended.
- Packages listed in `requirements.txt`.
- A web browser.
- Internet access to download packages.
- No API key or external service is needed to run the app.

## Environment setup

From the project folder on your computer:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r .\requirements.txt
```

Check the installed dependencies:

```powershell
.\.venv\Scripts\python.exe -m pip check
```

## Run the app

```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py --server.address 127.0.0.1
```

Open the local address shown in PowerShell. Keep PowerShell open while using
the app. Press Ctrl+C in PowerShell to stop it.

## How to use it

1. Enter skills separated by commas, semicolons, or new lines.
2. Choose an industry category.
3. Select **Compare My Skills**.
4. Review the matched skills, skills to explore, and certifications to research.

Use sample skills only.

## How matching works

1. The text is split at commas, semicolons, and new lines.
2. Each entry is converted to lowercase, extra spaces are removed, and
   duplicate entries are ignored.
3. Each example skill in the selected category is checked for an exact match.
4. The percentage equals the matched example skills divided by the number of
   example skills in that category. Each category has five example skills, so
   each match adds 20 percentage points.
5. Matched skills, skills to explore, and the category's example certifications
   are displayed.

## Industry categories

| Category | Example skills | Example certifications to research |
|---|---|---|
| Healthcare Support | communication, patient care, CPR, EMR, scheduling | Certified Nursing Assistant (CNA); Basic Life Support (BLS) certification |
| Logistics & Supply Chain | inventory, Excel, shipping, forklift, safety | Certified Logistics Associate (CLA); forklift operator certification |
| Data Analytics & IT | Excel, SQL, Tableau, Python, data entry | Google Data Analytics Certificate; Tableau certification |
| Advanced Manufacturing | safety, blueprints, quality control, machining, math | OSHA 10-Hour General Industry training |

In the Healthcare category, **BLS** means Basic Life Support. It does not refer
to the Bureau of Labor Statistics.

The skill lists are short, generic examples chosen for demonstration. They are
not verified job requirements for any employer or region.

## Example result

Enter this text:

```text
excel, sql, tableau, python
```

Then choose **Data Analytics & IT** and select **Compare My Skills**.

Expected display:

- Example skill-list overlap: **80%**
- Matched skills: Excel, Sql, Tableau, Python
- Skills to explore: Data Entry
- Certifications to research: Google Data Analytics Certificate; Tableau certification

The app title-cases skill names for display, so "SQL" appears as "Sql."

## Screenshot

<img width="721" height="833" alt="Screenshot 2026-11-08 074221" src="https://github.com/user-attachments/assets/ca4ca4fb-814e-4128-91a7-5ce1d629cd9e" />


Results for the sample skills `excel, sql, tableau, python` in the Data
Analytics & IT category. The example uses invented sample skills only.

## Testing

This prototype does not include automated tests yet. Its matching logic is
simple and can be checked manually with the example above.

## Current limitations

- The app is rule-based. It uses no AI model, machine learning, or live
  labor-market data.
- Matching is exact. "Microsoft Excel" does not match "excel," and "data-entry"
  does not match "data entry."
- Spaces alone do not separate skills. Use commas, semicolons, or new lines.
- A pasted résumé paragraph will rarely match, because only exact skill names
  count.
- The title refers to Oklahoma, but the skill lists are generic examples, not
  Oklahoma labor-market data.
- The percentage reflects overlap with five example skills only. It is not a
  hiring, eligibility, or job-readiness score.
- Certifications are examples. Verify requirements, costs, and availability
  with official sources.
- Automatic title-casing displays some abbreviations imperfectly, such as
  "Sql," "Cpr," and "Emr."

## Privacy and security

- Use sample skills only. Do not enter your full name, contact details,
  employer information, or a real résumé.
- The app does not save entries to a file or database.
- If the app is published online, the hosting provider may keep its own logs.
  Avoid personal information in any public demonstration.
- Running with `--server.address 127.0.0.1` keeps the app on your own computer.

## Demonstration outline

1. Show the independent-project notice.
2. Enter `excel, sql, tableau, python`.
3. Choose **Data Analytics & IT**.
4. Select **Compare My Skills**.
5. Point out the 80% example overlap, the skills to explore, and the
   certification examples.
6. Explain the limits: sample data, exact matching, and no hiring decision.
