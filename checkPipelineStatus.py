import streamlit as st
import boto3

# Connect to AWS Step Functions
stepfunctions_client = boto3.client('stepfunctions')

# Function to retrieve execution details
def get_execution_details(execution_arn):
    response = stepfunctions_client.describe_execution(executionArn=execution_arn)
    return response

# Streamlit UI
st.title('Pipeline Execution Details')

execution_arn = st.text_input('Enter Pipeline Execution ARN:')
if st.button('Get Execution Details'):
    execution_details = get_execution_details(execution_arn)
    # Display relevant details
    st.write('Execution Status:', execution_details['status'])
    st.write('Execution Output:', execution_details.get('output', 'No output available'))
