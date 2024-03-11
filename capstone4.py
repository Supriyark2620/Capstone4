import streamlit as st
import boto3
import os

# Function to upload file to S3 bucket
def upload_to_s3(file_path, bucket_name, object_name):
    s3 = boto3.client('s3')
    try:
        response = s3.upload_file(file_path, bucket_name, object_name)
        st.success("File uploaded successfully to S3 bucket!")
    except Exception as e:
        st.error(f"Error uploading file to S3: {e}")

def main():
    st.title("File Uploader to S3 Bucket")
    
    # File upload section
    uploaded_file = st.file_uploader("Choose a file to upload")
    
    if uploaded_file is not None:
        file_name = uploaded_file.name
        st.write(f"Selected file: {file_name}")
        
        # Temporary file path to save the uploaded file
        temp_file_path = f"./{file_name}"
        
        # Save the uploaded file to a temporary location
        with open(temp_file_path, "wb") as f:
            f.write(uploaded_file.getvalue())
        
        # S3 bucket and object name
        bucket_name = st.text_input("Enter S3 Bucket Name")
        object_name = st.text_input("Enter Object Name (Key)")
        
        if st.button("Upload to S3"):
            if bucket_name and object_name:
                upload_to_s3(temp_file_path, bucket_name, object_name)
            else:
                st.warning("Please provide both S3 Bucket Name and Object Name")

if __name__ == "__main__":
    main()
