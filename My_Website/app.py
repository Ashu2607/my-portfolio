# -*- coding: utf-8 -*-
import streamlit as st
from PIL import Image, ImageDraw
import os

def make_circular(image_path):
    """Function to make an image circular"""
    img = Image.open(image_path).convert("RGBA")
    size = min(img.size)

    # Create a circular mask
    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)

    # Apply mask and crop
    circular_img = Image.new("RGBA", (size, size))
    circular_img.paste(img.resize((size, size)), (0, 0), mask)

    return circular_img

# Portfolio Title (Centered)
st.markdown("""
    <style>
        @media (max-width: 640px) {
            .portfolio-title {
                padding-left: 4px !important;
            }
        }
    </style>

    <h1 class="portfolio-title" style="padding-left: 140px; font-size: 36px; font-weight: bold;">My Portfolio</h1>
""", unsafe_allow_html=True)

# Profile Section
image_path = "circular_profile.png"  

if os.path.exists(image_path):
    circular_image = make_circular(image_path)

    # Save the circular image temporarily
    circular_image_path = "circular_profile.png"
    circular_image.save(circular_image_path)

    # ✅ Use `st.image()` for better compatibility
    col1, col2, col3 = st.columns([0.5, 1, 1])
    
    with col1:
        st.write("  ")  # Empty space for centering
    with col2:
        st.image(image_path, width=150)  # Image appears centered
        
        # 🔥 FIXED INDENTATION ERROR HERE 🔥
        st.markdown("""
        <style>
            .container {
                display: flex;
                flex-direction: column;
                align-items: flex-start;
            }
            .name {
                display: inline-block;
                margin-bottom: -5px; /* Adjust spacing */
            }
            .subtitle {
                display: inline-block;
                margin-top: -20px; /* Pull closer */
            }
        </style>
        <div class="container" style="width: 450px;">
       <h2 class="name" style="text-align: left;">Ashutosh Singh</h2>
        <p class="subtitle" style="text-align: left; font-size: 18px; color: #bbbbbb; font-style: italic;">
        BTech Student @ IIT Guwahati | Competitive Programmer | Data Science Enthusiast
       </p>
        </div>

        """, unsafe_allow_html=True)  # ✅ Correct indentation here!
        
    with col3:
        st.write("")  # Empty space for centering

else:
    st.error("⚠️ Profile image NOT found! Check the filename or path.")

# Styled Section Headers with Borders
def section_title(title, icon):
    st.markdown(f"""
    <div style="border: 2px solid #444; padding: 10px; border-radius: 10px; margin-bottom: 20px; background-color: #222;">
        <h2 style="color: white; font-weight: bold;">{icon} {title}</h2>
    </div>
    """, unsafe_allow_html=True)

# Sections with Borders
section_title("About Me", "💡")
st.info("""
Hello fellas! 👋

I’m Ashutosh Singh, a BTech student in Chemical Engineering at IIT Guwahati, with a strong passion for Software Development and Competitive Programming 🚀. I love solving complex problems, optimizing algorithms, and exploring new tech stacks.

Beyond coding, I enjoy traveling to new places ✈️, binge-watching Dragon Ball Z ⚡, and brainstorming creative ideas. As a core team member of Alcheringa, IIT Guwahati’s annual cultural festival, I actively contribute to organizing and managing large-scale events.

Always excited to learn, innovate, and take on new challenges! Let’s build something amazing. 💡🔥
""")

section_title("Projects", "🚀")

st.markdown("""
### 📌 **Credit Card Behavior Prediction Score**
- **Predictive Modeling for Credit Behavior:** Developed a machine learning model to predict credit card usage behavior using real-world financial data, enhancing risk assessment and customer profiling.  
- **Feature Engineering & Model Explainability:** Applied embedding, LIME, SHAP, and feature selection to interpret key factors influencing credit behavior, ensuring transparency in decision-making.  
- **Machine Learning Implementation:** Implemented Random Forest and Logistic Regression models to classify credit card users, optimizing performance through hyperparameter tuning and evaluation metrics.  
- 🔗 **[GitHub Repository](https://github.com/Ashu2607/CreditCard-score)**

 ### 📌 **Predicting Completion of Clinical Trials**  
- **Clinical Trial Data Analysis:** Analyzed clinical trial data from Novartis, focusing on study status, sponsor details, interventions, outcomes, and study design.  
- **Data Cleaning & Visualization:** Used heatmaps for missing values and performed Exploratory Data Analysis (EDA) with Pandas, Seaborn, and Matplotlib to understand data distribution and relationships.  
- **Modeling & Insights:** Applied various machine learning techniques, including embeddings, LIME, SHAP, Named Entity Linking (NLM), Random Forest, and Logistic Regression, to extract insights and improve predictive accuracy.  
- 🔗 **[GitHub Repository](https://github.com/Ashu2607/Novartis)** 

""", unsafe_allow_html=True)

section_title("Skills", "🛠")
st.markdown("""
- **Programming:** C/C++, Python, JavaScript, Dart  
- **Data Science:** NumPy, Pandas, Scikit-learn, TensorFlow, Keras  
- **Machine Learning:** Regression, Classification, Clustering, XGBoost  
- **Web Development:** HTML, CSS, React.js, Node.js  
- **App Development:** Flutter  
- **Databases:** MySQL, MongoDB  
- **Tools & Others:** Git, MATLAB, Figma  
""", unsafe_allow_html=True)


import streamlit as st

# --- Blog Section Title ---
section_title("Blog", "✍️")

st.markdown("### 📝 Latest Articles")

# --- Credit Card Default Risk Scoring Project ---
st.markdown("### 📉 Credit Card Default Risk Scoring – ML Project")

with st.expander("📌 Problem Statement"):
    st.write("""
    Banks face significant losses due to credit card defaults. The goal was to develop a **Behavioral Score Model** to predict the probability of default and assist in risk management.
    """)

with st.expander("⚠️ Challenges"):
    st.markdown("""
    - **Imbalanced Data**: Defaults were rare, making it harder for models to learn patterns.  
    - **Diverse Feature Types**: Included **transaction history, credit bureau records, and loan inquiries**.  
    - **Model Generalization**: Ensuring consistent performance on unseen validation data.
    """)

with st.expander("🛠 Approach"):
    st.markdown("""
    - **Preprocessed data**: Handled missing values, performed encoding, and applied scaling.  
    - **Feature Selection**: Used **correlation analysis** and **domain knowledge**.  
    - **Trained ML Models**: **Logistic Regression, Random Forest, and XGBoost**.  
    - **Evaluation Metrics**: Emphasized **ROC-AUC** and **precision-recall curves** for accuracy.
    """)

with st.expander("🚀 Outcome"):
    st.markdown("""
    - Successfully **predicted default probabilities** for validation accounts.  
    - Ready for **integration into Bank A’s risk framework** to improve credit assessment.
    """)


# --- Clinical Trials Completion Prediction Project ---
st.markdown("### 🧪 Clinical Trials Completion Prediction – Novartis Hackathon")

with st.expander("📌 Problem Statement"):
    st.write("""
    Many clinical trials fail before completion. The objective was to **predict whether a clinical trial would successfully complete**, aiding pharma companies in optimizing resource allocation.
    """)

with st.expander("⚠️ Challenges"):
    st.markdown("""
    - **Severely Imbalanced Classes**: Very few trials were marked as 'Withdrawn'.  
    - **Complex Categorical Variables**: Multiple attributes like **intervention types, sponsors, and study duration**.  
    - **Model Interpretability**: Required clear insights for non-technical stakeholders.
    """)

with st.expander("🛠 Approach"):
    st.markdown("""
    - **Data Cleaning & Feature Engineering**: Extracted insights from **study duration, sponsor credibility, and intervention types**.  
    - **Applied ML Models**: **Logistic Regression, Random Forest, and XGBoost** for robust predictions.  
    - **Addressed Class Imbalance**: Used **SMOTE (Synthetic Minority Over-sampling Technique)**.  
    - **Improved Interpretability**: Leveraged **SHAP values** for clear feature importance analysis.
    """)

with st.expander("📊 Key Insights"):
    st.markdown("""
    - **Pharma-sponsored trials** had significantly **higher success rates**.  
    - **Drug-based interventions** performed **better than behavioral studies** in trial completion.  
    - Provided actionable insights to **optimize funding allocation in clinical research**.
    """)





section_title("Achievements", "🏆")
st.markdown("""
### 🚀 Notable Achievements  

- 🧠 **Semifinalist in Novartis NEST Hackathon 2024**  
   Selected among top teams for innovative ML-based healthcare solutions in a national-level competition organized by Novartis.

- 💻 **Flutter App Developer at IITG Student Web Committee**  
   Built production-level apps including a weather app and eMart shopping app, awarded certification by the Student Web Committee.

- 🧠 **Competitive Programming Excellence**  
   Strong problem-solving and DSA skills, with hands-on experience in solving 500+ problems on platforms like LeetCode and Codeforces.

- 🗣️ **Literary Secretary – Brahmaputra Hostel**  
   Organized literary events and led communication initiatives, demonstrating strong leadership and team-building skills.

- 🥇 **Gold Medal in Hockey (Spardha 2024)**  
   Represented Brahmaputra Hostel and clinched the top spot in IIT Guwahati’s inter-hostel championship.

- 📘 **Qualified JEE Advanced 2022**  
   Secured **AIR 5646**, placing in the top 1% of over 160,000 candidates in India’s most competitive engineering entrance exam.

- 🧮 **Pre-Regional Mathematics Olympiad (PRMO) Qualifier**  
   Cleared the first round of India’s prestigious Olympiad program focused on advanced mathematics.
""")




st.subheader("📬 Contact Me")

st.markdown("""
<div style="display: flex; gap: 10px; flex-wrap: wrap; align-items: center; margin-top: 10px;">
    <a href="mailto:ashutosh.snh@iitg.ac.in" target="_blank">
        <img src="https://img.shields.io/badge/📧%20Email-D14836?style=flat&logo=gmail&logoColor=white" alt="Email">
    </a>
    <a href="https://www.linkedin.com/in/ashutosh-singh-6609491b6" target="_blank">
        <img src="https://img.shields.io/badge/🔗%20LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white" alt="LinkedIn">
    </a>
    <a href="https://github.com/Ashu2607" target="_blank">
        <img src="https://img.shields.io/badge/💻%20GitHub-181717?style=flat&logo=github&logoColor=white" alt="GitHub">
    </a>
    <a href="https://www.instagram.com/_ashusng_05/" target="_blank">
        <img src="https://img.shields.io/badge/📸%20Instagram-E4405F?style=flat&logo=instagram&logoColor=white" alt="Instagram">
    </a>
    <a href="tel:+918955952607">
        <img src="https://img.shields.io/badge/📞%20Call-25D366?style=flat&logo=whatsapp&logoColor=white" alt="Call">
    </a>
</div>
""", unsafe_allow_html=True)
