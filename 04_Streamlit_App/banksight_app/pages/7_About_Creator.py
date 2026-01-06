import streamlit as st
from PIL import Image

st.title("👩‍💻 About Creator")

# Load profile image
image = Image.open("images/profile.jpg")
st.image(image, width=200)

st.markdown("""
### 👤 Name
**Rudra Barman**

### 🎓 Role
Aspiring Data Analyst | Banking & Financial Analytics

### 🛠️ Skills & Expertise
- Python (Pandas, NumPy)
- SQL (PostgreSQL)
- Data Cleaning & Analysis
- Streamlit Dashboard Development
- Banking Analytics & Fraud Detection

### 📌 Project Highlights
- End-to-end data cleaning & SQL modeling  
- 15+ analytical SQL queries  
- Real-time CRUD & banking simulation  
- Interactive Streamlit dashboard  

### 📫 Contact
- 📧 Email: **rudrabarman7090@gmail.com**  
- 💼 LinkedIn: https://linkedin.com/in/rudra-barman-196613271  
- 🐙 GitHub: https://github.com/Rudra-Barman
""")
