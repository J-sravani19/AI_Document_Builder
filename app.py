import streamlit as st
from generators.resume_generator import generate_resume
from generators.coverletter_generator import generate_cover_letter
from generators.portfolio_generator import generate_portfolio
from style import get_page_style

st.set_page_config(page_title="AI Document Builder", layout="wide")
st.markdown(get_page_style(), unsafe_allow_html=True)

st.sidebar.title("AI Document Builder")

section = st.sidebar.radio(
    "Select Document Type",
    ["Resume", "Cover Letter", "Portfolio"]
)

st.title(section)

if "generated_files" not in st.session_state:
    st.session_state.generated_files = None


# ================= RESUME =================
if section == "Resume":

    name = st.text_input("Full Name", placeholder="John Doe")
    phone = st.text_input("Phone", placeholder="+91 9876543210")
    linkedin = st.text_input("LinkedIn URL", placeholder="https://linkedin.com/in/johndoe")
    github = st.text_input("GitHub URL", placeholder="https://github.com/johndoe")

    profile_type = st.selectbox(
        "Profile Type",
        ["Fresher", "Experienced Professional"]
    )

    template = st.selectbox(
        "Select Template",
        ["Classic", "Modern", "Professional"]
    )

    skills = st.text_area("Skills", placeholder="Python, SQL, Power BI")
    projects = st.text_area("Projects", placeholder="AI Resume Builder - Built using Streamlit and Gemini API")
    certifications = st.text_area("Certifications", placeholder="Google Data Analytics Certificate")
    role = st.text_input("Target Role", placeholder="Data Analyst")
    job_description = st.text_area("Job Description", placeholder="Paste job description here (optional)")

    if st.button("Generate Resume", use_container_width=True):

        if not name or not skills or not projects or not role:
            st.error("Please fill all required fields.")
        else:
            with st.spinner("Generating your resume..."):
                files = generate_resume(
                    name,
                    phone,
                    linkedin,
                    github,
                    skills,
                    projects,
                    role,
                    job_description,
                    profile_type,
                    certifications,
                    template
                )

            st.session_state.generated_files = files
            st.success("Resume generated successfully!")


# ================= COVER LETTER =================
elif section == "Cover Letter":

    name = st.text_input("Full Name", placeholder="John Doe")
    phone = st.text_input("Phone", placeholder="+91 9876543210")
    linkedin = st.text_input("LinkedIn URL", placeholder="https://linkedin.com/in/johndoe")

    profile_type = st.selectbox(
        "Profile Type",
        ["Fresher", "Experienced Professional"]
    )

    template = st.selectbox(
        "Select Template",
        ["Classic", "Modern", "Professional"]
    )

    skills = st.text_area("Skills", placeholder="Python, SQL, Machine Learning")
    role = st.text_input("Target Role", placeholder="Data Analyst")
    company = st.text_input("Company Name", placeholder="Google")
    education = st.text_area(
        "Education",
        placeholder="Bachelor of Technology in Computer Science | XYZ University | 2023 | CGPA: 8.5/10"
    )

    if st.button("Generate Cover Letter", use_container_width=True):

        if not name or not skills or not role or not company:
            st.error("Please fill all required fields.")
        else:
            with st.spinner("Generating your cover letter..."):
                files = generate_cover_letter(
                    name,
                    phone,
                    linkedin,
                    skills,
                    role,
                    company,
                    education,
                    profile_type,
                    template
                )

            st.session_state.generated_files = files
            st.success("Cover letter generated successfully!")


# ================= PORTFOLIO =================
elif section == "Portfolio":

    name = st.text_input("Full Name", placeholder="John Doe")
    phone = st.text_input("Phone", placeholder="+91 9876543210")
    linkedin = st.text_input("LinkedIn URL", placeholder="https://linkedin.com/in/johndoe")
    github = st.text_input("GitHub URL", placeholder="https://github.com/johndoe")

    profile_type = st.selectbox(
        "Profile Type",
        ["Fresher", "Experienced Professional"]
    )

    template = st.selectbox(
        "Select Template",
        ["Classic", "Modern", "Professional"]
    )

    skills = st.text_area("Skills", placeholder="Python, SQL, Power BI")
    projects = st.text_area("Projects", placeholder="Data Dashboard Project | E-commerce Analytics")
    certifications = st.text_area("Certifications", placeholder="AWS Cloud Practitioner")
    achievements = st.text_area("Achievements", placeholder="Winner - Hackathon 2024")

    if st.button("Generate Portfolio", use_container_width=True):

        if not name or not skills or not projects:
            st.error("Please fill required fields.")
        else:
            with st.spinner("Generating your portfolio..."):
                files = generate_portfolio(
                    name,
                    phone,
                    linkedin,
                    github,
                    skills,
                    projects,
                    certifications,
                    achievements,
                    profile_type,
                    template
                )

            st.session_state.generated_files = files
            st.success("Portfolio generated successfully!")


# ================= DOWNLOAD SECTION =================
if st.session_state.generated_files:

    st.markdown("---")
    st.subheader("Download Your Document")

    docx_file, pdf_file = st.session_state.generated_files

    col1, col2 = st.columns(2)

    with col1:
        with open(docx_file, "rb") as f:
            st.download_button(
                "Download DOCX",
                f,
                file_name=docx_file,
                use_container_width=True
            )

    with col2:
        with open(pdf_file, "rb") as f:
            st.download_button(
                "Download PDF",
                f,
                file_name=pdf_file,
                use_container_width=True
            )

    st.info("If AI quota is exceeded, an ATS template version is automatically generated.")