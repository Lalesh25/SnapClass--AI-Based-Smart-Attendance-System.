import streamlit as st
from src.screens.home_screen import home_screen
from src.screens.student_screen import student_screen
from src.screens.teacher_screen import teacher_screen
from src.components.dialog_auto_enroll import auto_enroll_dialog


def main():
    st.set_page_config(
        page_title = 'SnapClass - Making Attendance faster using AI!',
        page_icon = "https://i.bb.co/YTYFn5qV/logo.png"
    )
    if 'login_type' not in st.session_state:
        st.session_state['login_type'] = None

    match st.session_state['login_type']:
        case 'teacher':
            teacher_screen()
        case 'student':
            student_screen()    

        case None:
            home_screen()


    join_code = st.query_params.get('join-code')
    if join_code:
        if st.session_state.login_type != 'student':
            st.session_state.login_type = 'student'
            st.rerun()
        if st.session_state.get('is_logged_in') and st.session_state.get('user_role') == 'student':
            auto_enroll_dialog(join_code)
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