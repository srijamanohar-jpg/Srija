import streamlit as st

# Data for the app
content = {
    "Class 5": ["The Earth", "Continents & Oceans", "Early Life", "Governance"],
    "Class 6": ["Reading Maps", "Globe: A Model of Earth", "Harappan Civilization", "Emergence of Kingdoms"],
    "Class 7": ["The Universe", "The Mughal Empire", "Delhi Sultanate", "State Government"]
}

st.title("📚 TG Social Studies Portal")
st.sidebar.header("Navigation")

# User Selection
grade = st.sidebar.selectbox("Choose your Class:", list(content.keys()))

st.header(f"Topics for {grade}")
for topic in content[grade]:
    st.write(f"- {topic}")

# Simple Quiz Section
st.divider()
st.subheader("Quick Check")
answer = st.radio("Which of these is the model of the Earth?", ["Map", "Globe", "Compass"])
if st.button("Submit"):
    if answer == "Globe":
        st.success("Correct! 🌟")
    else:
        st.error("Try again!")
