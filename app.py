import streamlit as st
from dotenv import load_dotenv
from utils import *

def main():
    load_dotenv()

    st.set_page_config(page_title="Invoice Extraction Bot")
    st.title("Invoice Extraction Bot...💁 ")
    st.subheader("I can help you in extracting invoice data")

    pdf = st.file_uploader("Upload Invoices Here, Only PDF Files Allowed",type=['pdf'],accept_multiple_files=True)

    submit = st.button("Extract Data")

    if submit:
        with st.spinner('Wait for it...'):
            df = create_docs(pdf)
            st.write(df)

            data_as_csv = df.to_csv(index=False).encode("utf-8")

            st.download_button("Download Data as CSV",data_as_csv,"benchmark-tool.csv",'text/csv',key="download-tools-csv")

        st.success("Hope I was able to save your time❤️")    

if __name__ == '__main__':
    main()        