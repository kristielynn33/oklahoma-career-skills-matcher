import re

import streamlit as st


st.set_page_config(
    page_title="Oklahoma Career Skills Matcher",
    page_icon="🎯",
    layout="centered",
)

st.title("🎯 Oklahoma Career Skills Matcher")

st.caption(
    "Independent portfolio prototype. Not affiliated with or endorsed "
    "by the Oklahoma Employment Security Commission (OESC) or the "
    "U.S. Bureau of Labor Statistics (BLS)."
)

st.write(
    "Compare your skills with example skill lists for selected "
    "industry categories."
)

st.warning(
    "For demonstrations, use sample skills. Do not enter sensitive "
    "personal information or a real résumé."
)

st.markdown("---")

# Example skill lists for demonstration purposes.
# These are not official or validated job requirements.
INDUSTRY_PROFILES = {
    "Healthcare Support": {
        "skills": [
            "communication",
            "patient care",
            "cpr",
            "emr",
            "scheduling",
        ],
        "certifications": [
            "Certified Nursing Assistant (CNA)",
            "Basic Life Support (BLS) certification",
        ],
    },
    "Logistics & Supply Chain": {
        "skills": [
            "inventory",
            "excel",
            "shipping",
            "forklift",
            "safety",
        ],
        "certifications": [
            "Certified Logistics Associate (CLA)",
            "Forklift operator certification",
        ],
    },
    "Data Analytics & IT": {
        "skills": [
            "excel",
            "sql",
            "tableau",
            "python",
            "data entry",
        ],
        "certifications": [
            "Google Data Analytics Certificate",
            "Tableau certification",
        ],
    },
    "Advanced Manufacturing": {
        "skills": [
            "safety",
            "blueprints",
            "quality control",
            "machining",
            "math",
        ],
        "certifications": [
            "OSHA 10-Hour General Industry training",
        ],
    },
}


def parse_skills(text: str) -> set[str]:
    """Split skills on commas, semicolons, or new lines; remove duplicates."""

    parts = re.split(r"[,;\n]+", text.lower())

    return {
        " ".join(part.split())
        for part in parts
        if part.strip()
    }


def compare_skills(
    user_skills: set[str],
    example_skills: list[str],
) -> tuple[list[str], list[str], int]:
    """Return matched skills, missing skills, and an overlap percentage."""

    matched = [
        skill for skill in example_skills
        if skill in user_skills
    ]

    missing = [
        skill for skill in example_skills
        if skill not in user_skills
    ]

    score = round(len(matched) / len(example_skills) * 100)

    return matched, missing, score


st.subheader("📋 Step 1: Enter Your Skills")

skills_text = st.text_area(
    "List skills separated by commas or new lines",
    placeholder="Example: customer service, excel, data entry, communication",
    max_chars=2000,
)

st.subheader("📈 Step 2: Choose an Industry Category")

industry = st.selectbox(
    "Industry category",
    list(INDUSTRY_PROFILES),
)

st.markdown("---")

if st.button("🚀 Compare My Skills"):
    user_skills = parse_skills(skills_text)

    if not user_skills:
        st.error("Please enter at least one skill.")

    else:
        profile = INDUSTRY_PROFILES[industry]

        matched, missing, score = compare_skills(
            user_skills,
            profile["skills"],
        )

        st.subheader(f"📊 Results for {industry}")

        st.metric(
            label="Example skill-list overlap",
            value=f"{score}%",
        )

        st.progress(score / 100)

        st.caption(
            "This percentage only shows how many example skills matched "
            "exactly. It is not a hiring prediction, a job-readiness "
            "score, or professional career advice."
        )

        column_1, column_2 = st.columns(2)

        with column_1:
            st.success("✅ Matched skills")

            if matched:
                for skill in matched:
                    st.write(f"- {skill.title()}")
            else:
                st.write("*No exact matches found.*")

        with column_2:
            st.warning("🔍 Skills to explore")

            if missing:
                for skill in missing:
                    st.write(f"- {skill.title()}")
            else:
                st.write("*All example skills matched.*")

        st.markdown("---")
        st.subheader("💡 Certifications to Research")

        for certification in profile["certifications"]:
            st.write(f"- {certification}")

        st.info(
            "These are examples only. Verify requirements, costs, and "
            "local employer demand with official sources before making "
            "education or career decisions."
        )

st.divider()

st.caption(
    "Skill lists are illustrative examples. This prototype does not "
    "retrieve live labor-market data."
)
