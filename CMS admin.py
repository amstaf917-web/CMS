import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import cv2
from pyzbar.pyzbar import decode
import time

st.title("🎓 CLASS MENEGMENT SYSTEM")
# --- Sidebar & Developer Credits ---
with st.sidebar:
    st.title("System Info")
    st.markdown("---")
    st.write("**Developer:**")
    st.success("✨ ABDULLAH MAQSOOD")
    st.info("Role: Lead Developer / Data Scientist")
    st.markdown("---")
    st.write("v1.0.0 - F2025 Release")

    # TAKING PASS INPUT
u_id = st.text_input("Enter your id: " , icon="🆔")
u_password = st.text_input("Enter your password: ",type="password" , icon="🔑")


if u_id == "admin" and u_password == "admin123" :
    st.success("🎊 successfully loged in")


    # DATA LOADING
    data1 = pd.read_csv("CAG.csv")
    data2 = pd.read_csv("DS.csv")
    data3 = pd.read_csv("FE.csv")
    data4 = pd.read_csv("ICT.csv")
    data5 = pd.read_csv("PF.csv")
    data6 = pd.read_csv("roll no  sheet.csv")
    ict_df = pd.DataFrame(data4)
    fe_df = pd.DataFrame(data3)
    ds_df = pd.DataFrame(data2)
    cag_df = pd.DataFrame(data1)
    pf_df = pd.DataFrame(data5)
    roll_df = pd.DataFrame(data6)

#---------------------------------------------------------------------------------
    # CAG GRAPH
    def cag_graph(name):
        # student = "F25M-BSDS-044"
        chart_colors = ["#EDB2B2","#EDBB82","#9DEA85","#6EACED","#F08AE6",]
        result = cag_df[cag_df["Student Name"]==name]
        if result.empty:
            st.warning("no data found")
        else:
                data = [
                        result["Q1 (10)"].iloc[0],
                        result["Q2 (10)"].iloc[0],
                        result["Asgn (10)"].iloc[0],
                        result["Mid (30)"].iloc[0],
                        result["Form (50)"].iloc[0]]
                labels = ["Quiz 1" , "Quiz 2" , "Formative" , "Mids" , "Final"]
                
                fig, ax = plt.subplots()
                ax.pie(data, labels=labels, colors=chart_colors, autopct='%1.1f%%')

                student_name = result["Student Name"].iloc[0]
                ax.set_title(f"{student_name}'s CAG Performance Graph")

                st.pyplot(fig)
# -----------------------------------------------------------------------------------------------
    # ICT GRAPH
    def ict_graph(name):
        # student = "Abdullah Maqsood"
        chart_colors = ["#EDB2B2","#EDBB82","#9DEA85","#6EACED","#6EEDD6"]
        result = ict_df[ict_df["Student Name"] == name]

        if result.empty:
            st.warning("no data found")
        else:
            data = [
                result["Quiz 1"].iloc[0],
                result["Quiz 2"].iloc[0],
                result["Assignment "].iloc[0],
                result["MidTerm Test"].iloc[0],
                result["Final"].iloc[0]
            ]

            # Matching labels to the 4 data points above
            labels = ["Quizzes 1", "Quizzes 2","Formative" , "Midterm", "Final"]

            fig, ax = plt.subplots()
            ax.pie(data, labels=labels, colors=chart_colors, autopct='%1.1f%%')

            student_name = result["Student Name"].iloc[0]
            ax.set_title(f"{student_name}'s ICT Performance Graph")

            st.pyplot(fig)
# ------------------------------------------------------------------------------------------------
    # PF GRAPH
    def pf_graph(name):
        # student = "Abdullah Maqsood"
        chart_colors = ["#EDB2B2","#EDBB82","#9DEA85","#6EACED","#6EEDD6"]
        result = pf_df[pf_df["Student Name"] == name]

        if result.empty:
            st.warning("no data found")
        else:
            data = [
                result["Unnamed: 3"].iloc[0],
                result["Formative Assesment(50 %)"].iloc[0],
                result["Unnamed: 4"].iloc[0],
                result["Formative Assesment(50 %)"].iloc[0],
                result["Unnamed: 7"].iloc[0]
            ]

        # Matching labels to the 4 data points above
            labels = ["Quiz 1", "Quiz 2","Formative" , "Midterm", "Final"]

            plt.pie(data, labels=labels, colors=chart_colors, autopct='%1.1f%%')

            fig, ax = plt.subplots()
            ax.pie(data, labels=labels, colors=chart_colors, autopct='%1.1f%%')

            student_name = result["Student Name"].iloc[0]
            ax.set_title(f"{student_name}'s PF Performance Graph")

            st.pyplot(fig)
# ------------------------------------------------------------------------------------------
    # FE GRAPH
    def fe_graph(name):
        # student = "Abdullah Maqsood"
        chart_colors = ["#EDB2B2","#EDBB82","#9DEA85","#6EACED","#6EEDD6"]
        result = fe_df[fe_df["Student Name"] == name]

        if result.empty:
            st.warning("no data found")
        else:
            data = [
                result["Unnamed: 5"].iloc[0],
                result["Summative Assesment(50 %)"].iloc[0],
                result["Unnamed: 6"].iloc[0],
                result["Formative Assesment(50 %)"].iloc[0],
                result["Unnamed: 9"].iloc[0]
            ]
    
            # Matching labels to the 4 data points above
            labels = ["Quiz 1", "Quiz 2","Formative" , "Midterm", "Final"]

            fig, ax = plt.subplots()
            ax.pie(data, labels=labels, colors=chart_colors, autopct='%1.1f%%')

            student_name = result["Student Name"].iloc[0]
            ax.set_title(f"{student_name}'s FE Performance Graph")
            st.pyplot(fig)

# DEFINING FUNCTIONS
    def taking_input_rollno():
        roll_no = st.selectbox("slect ypur roll no",roll_df["Roll #"])
        result = roll_df[roll_df["Roll #"] == roll_no]
        if result.empty:
            st.warning("no data found")
        else:
            name = result["Name"].iloc[0]
            return name
#------------------------------------------------------------------------------------------
    def taking_input_subject():
        subject = st.selectbox("Select your subject",["CAG","DS","FE","ICT","PF"])
        return subject
    def taking_input_name():
        name = st.selectbox("Select your name: " , roll_df["Name"])
        return name
    
#------------------------------------------------------------------------------------------
    def selecting_graph(name , subject):
        if subject == "CAG":
            cag_graph(name)
        elif subject == "FE":
            fe_graph(name)
        elif subject == "ICT":
            ict_graph(name)
        elif subject == "PF":
            pf_graph(name)

#------------------------------------------------------------------------------------------
    def scanning_student_card():
        col_left, col_right = st.columns([1, 1.2])

        with col_left:
            st.subheader("📷 Live Scanner")
            scan_btn = st.button("🚀 Start Scanning", use_container_width=True)
            stop_btn = st.button("🛑 Stop Camera", use_container_width=True)

            FRAME_WINDOW = st.image([])

        if 'scanned_id' not in st.session_state:
            st.session_state['scanned_id'] = None

        if scan_btn:
            st.session_state['scanned_id'] = None
            st.success("Camera is openning. This may take a moment.", icon="✅")
            cam = cv2.VideoCapture(0)
        # OPTIMIZATION: Low res makes camera open much faster
            cam.set(cv2.CAP_PROP_FRAME_WIDTH, 400)
            cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)

            while True:
                success, frame = cam.read()
                if not success or stop_btn:
                    break

                for barcode in decode(frame):
                    st.session_state['scanned_id'] = barcode.data.decode("utf-8").strip()

                    (x, y, w, h) = barcode.rect
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 6)
                    break

                FRAME_WINDOW.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

                if st.session_state['scanned_id']:
                    time.sleep(0.5)
                    break
            
            cam.release()
            st.rerun()

        with col_right:
            st.subheader("📄 Student Profile")
    
            if st.session_state['scanned_id']:
                search_id = st.session_state['scanned_id']
                result = roll_df[roll_df["Roll #"] == search_id]

                if not result.empty:
                    st.balloons()
                    st.success(f"Record Found for: {search_id}")
                    result = roll_df[roll_df["Roll #"] == search_id]
                    return result["Name"].iloc[0]

#------------------------------------------------------------------------------------------
    st.subheader("Fetch numbers by:")
    fetching_method = st.radio("Slect your choice",["By name" , "By roll no" ,"by scanning student card"])
#------------------------------------------------------------------------------------------
if fetching_method == "By name":
    name = taking_input_name()
    if name:
        st.success(f"{name} is selected", icon="✅")
    subject = taking_input_subject()
    if subject:
        st.success(f"{subject} is selected", icon="✅")
    selecting_graph(name , subject)

#------------------------------------------------------------------------------------------
elif fetching_method == "By roll no":
    name = taking_input_rollno()
    if name:
        st.success(f"{name} is selected" , icon = "✅")
    subject = taking_input_subject()
    if subject:
        st.success(f"{subject} is selected", icon="✅")
    if name and subject:
        selecting_graph(name , subject)

#------------------------------------------------------------------------------------------
elif fetching_method == "by scanning student card":
    scanned_id = scanning_student_card()
    if scanned_id:
        st.success(f"Scanned ID: {scanned_id}", icon="✅")
   
    subject = taking_input_subject()
    if subject:
        st.success(f"{subject} is selected", icon="✅")
    if scanned_id and subject:
        selecting_graph(scanned_id , subject)
# ------------------------------------------------------------------------------------------
# MY NAME FOOTER
st.markdown(f'<div class="dev-footer">Developed by ABDULLAH MAQSOOD</div>', unsafe_allow_html=True)