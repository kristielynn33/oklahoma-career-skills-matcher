# Oklahoma Career Skills Matcher

A Streamlit prototype that compares user-entered skills with predefined
skill lists for selected Oklahoma industry categories.

This is a rule-based demonstration. Its match score is based on exact
keyword overlap; it is not an AI assessment, a hiring prediction, or a
substitute for professional career guidance.

## How it works

1. Enter a name and a comma-separated list of skills.
2. Choose an industry category.
3. Select **Analyze My Career Match**.
4. Review the displayed matches, missing skills, and suggested
   certification.

The prototype contains four predefined categories:

- Healthcare Support
- Logistics & Supply Chain
- Data Analytics & IT
- Advanced Manufacturing

## Technology

- Python
- Streamlit
- Predefined Python dictionaries and lists

## Run locally

Requires Python and Streamlit. From the project folder, install Streamlit:

```powershell
python -m pip install streamlit
```

Then run the application, replacing `APP_FILENAME.py` with the actual
Python filename in this repository:

```powershell
python -m streamlit run APP_FILENAME.py
```

Streamlit will display a local browser address.

## Data and limitations

- Industry requirements, certification suggestions, and growth figures
  are hard-coded in the prototype.
- The application does not currently retrieve live BLS data.
- The displayed growth figures are illustrative and have not been
  verified or linked to a source in this repository.
- The percentage is a simple comparison with the selected predefined
  skill list. It is not a validated measure of job readiness.
- The current matching method expects comma-separated skills; a pasted
  résumé paragraph may not match correctly.
- Certification suggestions should be independently researched before
  making education or career decisions.
- This prototype should not be used as an employment-screening decision
  tool.

## Privacy

For demonstrations, use invented names and sample skills. Do not enter
sensitive personal information or a real résumé unless you understand the
hosting and data-handling arrangements.

## Possible improvements

- Replace illustrative growth figures with verified, dated sources.
- Improve skill matching and prevent duplicate inputs from inflating scores.
- Remove unsupported claims about automated BLS-agent data.
- Add tests for matching logic.
- Document input handling before deploying a public version.
