import streamlit as st
from src.screens.home_screen import home_screen
from src.screens.student_screen import student_screen
from src.screens.teacher_screen import teacher_screen

def main():
    if 'login_type' not in st.session_state:
        st.session_state['login_type'] = None

    match st.session_state['login_type']:
        case 'teacher':
            teacher_screen()
        case 'student':
            student_screen()    

        case None:
            home_screen()
main()    


















#  st.header("Title")
#     st.text_input("Enter name")
#     col1 , col2 = st.columns(2,gap="medium")
#     with col1:
#         if st.button("Display",type="primary",width="stretch"):
#             print("Hii Me!")
#     with col2:
#         if st.button("Display",type="secondary",width="stretch"):
#             print("Hii Me2!")

#     st.markdown(""" 

#  """,unsafe_allow_html=True)  # allows us to write html code    