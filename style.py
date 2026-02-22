def get_page_style():
    return """
    <style>

    .stApp {
        background-color: #F4F6F9;
        font-family: 'Inter', sans-serif;
    }

    .block-container {
        background: white;
        padding: 2.5rem;
        border-radius: 16px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.05);
    }

    section[data-testid="stSidebar"] {
        background-color: #111827;
    }

    section[data-testid="stSidebar"] * {
        color: white;
    }

    h1 {
        font-weight: 700;
        margin-bottom: 1.5rem;
    }

    .stButton > button {
        background: linear-gradient(135deg, #111827, #2563EB);
        color: white;
        border-radius: 12px;
        padding: 14px;
        font-weight: 600;
        border: none;
    }

    .stButton > button:hover {
        opacity: 0.9;
    }

    .stTextInput > div > input,
    .stTextArea > div > textarea {
        border-radius: 10px;
        border: 1px solid #E5E7EB;
        padding: 10px;
    }

    ::placeholder {
        color: #9CA3AF !important;
        font-style: italic !important;
        opacity: 1;
    }

    </style>
    """