import streamlit as st
from LandingPage import landing_page
from PageOne import page_one
from PageTwo import page_two
from PageThree import page_three
from PageFour import page_four


# Menu Sidebar wird definiert. Der Standartwert ist wird auf LandingPage gesetzt
# st.sidebar.title("TITEL SIDEBAR")
# menu = st.sidebar.radio(
#     "SUBTITEL SIDEBAR",
#     ["Landing Page",
#      "Seite 1",
#      "Seite 2",
#      "Seite 3",
#      "Seite 4"],
#     index=0             # Definition des Standartwertes (LandingPage)
# )

pages = ["Landing Page", "Page One", "Page Two", "Page Three", "Page Four"]

if "current_page" not in st.session_state:
    st.session_state["current_page"] = "Home"

# Sidebar mit einfachen Textlinks
st.sidebar.title("Navigation")
for page in pages:
    # Aktive Seite hervorheben
    if page == st.session_state["current_page"]:
        st.sidebar.markdown(f"**> {page}**")
    else:
        if st.sidebar.markdown(f"[{page}](#{page})", unsafe_allow_html=True):
            st.session_state["current_page"] = page

if st.session_state["current_page"] == "Home":
    st.markdown("### Willkommen auf der Startseite!")
elif st.session_state["current_page"] == "Add Pickups":
    st.markdown("### Pickup hinzufügen")
elif st.session_state["current_page"] == "View Pickups":
    st.markdown("### Pickup-Übersicht")

# Page Routing basierend auf Sidebar Auswahl
# if menu == "Landing Page":
#     landing_page()
# elif menu == "Seite 1":
#     page_one()
# elif menu == "Seite 2":
#     page_two()
# elif menu == "Seite 3":
#     page_three()
# elif menu == "Seite 4":
#     page_four()