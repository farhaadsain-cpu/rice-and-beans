import streamlit as st

def main():
    st.set_page_config(
        page_title="Sustainability Dashboard (Pilot)",
        page_icon="🌱",
        layout="wide",
    )
    st.title("Sustainability Dashboard (Pilot)")
    st.write("Use the sidebar to navigate to different sections.")

if __name__ == "__main__":
    main()
