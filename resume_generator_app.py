import streamlit as st
import requests
from streamlit.components.v1 import html

# ---------- Streamlit App UI ----------
st.set_page_config(page_title="Styled Resume Generator", page_icon="📝", layout="wide")

st.title("🧑‍💻 AI Resume Generator — Professional HTML Format")
st.markdown("Fill in your resume details below 👇")

# ---------- User Input Form ----------
with st.form("user_input_form"):
    st.subheader("👤 Personal Information")
    name = st.text_input("Full Name", placeholder="e.g., Alankrita Upadhyay")
    phone = st.text_input("Phone Number", placeholder="e.g., +91-9876543210")
    email = st.text_input("Email Address", placeholder="e.g., alankrita@example.com")
    linkedin = st.text_input("LinkedIn URL", placeholder="e.g., https://linkedin.com/in/yourname")
    portfolio = st.text_input("Portfolio URL", placeholder="Optional")
    address = st.text_input("Address", placeholder="e.g., Bengaluru, India")

    st.subheader("🎓 Education & 💼 Experience")
    education = st.text_area("Education", placeholder="B.Tech in Computer Science from ABC University, Graduated 2023\nM.S. in Data Science from XYZ Institute, 2025")
    experience = st.text_area("Experience", placeholder="Software Developer at XYZ Corp (2022–2024)\n- Developed Python APIs to handle user authentication, increasing security by 20%.\n- Optimized SQL queries, reducing database load by 15%.")

    st.subheader("🛠️ Skills")
    skills = st.text_area("Technical & Soft Skills", placeholder="Programming: Python, Java, JavaScript\nWeb Technologies: React, Node.js, HTML, CSS\nDatabases: SQL, MongoDB\nTools: Git, Docker, AWS\nSoft Skills: Communication, Problem-solving, Teamwork")

    st.subheader("📄 Job Description (Used to tailor resume)")
    job_description = st.text_area("Job Description", placeholder="We're hiring a software developer skilled in Python, Java, databases, and cloud platforms. Experience with agile methodologies is a plus.")

    submitted = st.form_submit_button("Generate Styled Resume")

# ---------- Resume Generation ----------
if submitted:
    required_fields = [name, phone, email, experience, skills, education, job_description]
    if not all(field.strip() for field in required_fields):
        st.warning("⚠️ Please fill in all required fields.")
    else:
        with st.spinner("Generating resume using Gemini..."):
            API_KEY = " " # Added the API key in my README File
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

            headers = {
                "Content-Type": "application/json"
            }

            # Enhanced prompt for better styling, specifically adding color to headings
            prompt = f"""
You are a professional resume builder. Your task is to generate a modern, clean, and visually appealing **two-column HTML resume with inline CSS**.

Here is the user's information:
Name: {name}
Phone: {phone}
Email: {email}
LinkedIn: {linkedin}
Portfolio: {portfolio}
Address: {address}
Education: {education}
Experience: {experience}
Skills: {skills}
Job Description: {job_description}

⚠️ STRICT INSTRUCTIONS for HTML and CSS generation:
- The entire output MUST be a complete and valid HTML document, including `<!DOCTYPE html>`, `<html>`, `<head>`, and `<body>` tags.
- Use **inline CSS only**. Do NOT use `<style>` tags or external stylesheets.
- The layout must be a clean **two-column design**.
    - **Left Column (approx 30% width):**
        - Prominently display Full Name at the top, styled as a main heading.
        - Below the name, list Contact Information (Phone, Email, LinkedIn, Portfolio - if provided, and Address).
        - Use icons (emojis or simple text symbols) next to contact details for a modern look.
        - Ensure good spacing and readability.
    - **Right Column (approx 70% width):**
        - Start with an "About Me" section (summary). Craft this summary to be concise and impactful, highlighting key skills and experience relevant to the provided Job Description.
        - Follow with "Experience" section. For each experience entry, include Company, Role, Location, and Dates. Use clear bullet points for responsibilities and quantifiable achievements, tailoring them to the Job Description.
        - Next, "Education" section. List degrees, institutions, and graduation years.
        - Finally, "Skills" section. Categorize skills (e.g., Programming Languages, Tools, Frameworks, Soft Skills) for better readability.
- **Styling Guidelines:**
    - Use a clean, professional sans-serif font (e.g., Arial, Helvetica, Lato, Roboto - ensure it's a common web-safe font).
    - Use a subtle color palette: main text dark grey/black.
    - **All section headings (e.g., "About Me", "Experience", "Education", "Skills") must have a distinct color, like a professional blue (#0056b3) or a deep green (#28a745) to highlight them.**
    - Ensure adequate padding and margins for readability.
    - Headings should be clear and distinct, bolded, and properly sized.
    - Bullet points for experience should be well-formatted.
    - No place holders like "(Your Name)", "(Insert here)", or "(Add Skill)". Use only the provided input.
    - Return ONLY clean HTML. No markdown, no explanations, no code blocks (```html), just the raw HTML.
"""

            payload = {
                "contents": [
                    {
                        "role": "user",
                        "parts": [{"text": prompt}]
                    }
                ]
            }

            try:
                response = requests.post(url, headers=headers, json=payload)
                response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)
                result = response.json()

                # Access the 'text' key from the first 'part' of the first 'candidate'
                html_content = result['candidates'][0]['content']['parts'][0]['text']

                st.success("✅ Resume generated successfully!")
                st.markdown("---")
                st.markdown("### 📄 Your Styled Resume:")
                html(html_content, height=1000, scrolling=True)

            except requests.exceptions.RequestException as req_err:
                st.error("❌ Request error. Check your API key or connection.")
                st.text(f"Error: {str(req_err)}")
                if response is not None:
                    st.text(f"Response status: {response.status_code}")
                    st.text(f"Response body: {response.text}")
            except (KeyError, IndexError):
                st.error("❌ Unexpected API response format. Please check your input or model access.")
                if response is not None:
                    st.code(response.text)
                else:
                    st.error("No response received from the API.")
