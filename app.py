import streamlit as st 
import google.generativeai as genai 
import google.ai.generativelanguage as glm 
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.environ.get("GOOGLE_API_KEY")
genai.configure(api_key=API_KEY)

st.image("adidas.jpg", width=200)
st.write("")

def main():
    st.title("Databricks Job Failure Analysis")
    prompt_template = """
    Analyze the provided text for insights into potential Databricks job failure causes and suggest solutions.

    **Text:**

    {provided_text}

    **Additional Information:**

    * (Describe any relevant job configuration details here, if available)
    * (Mention cluster type, size, etc., if applicable)
    * (If there were previous failures, mention any insights from them)

    **Desired Output:**

    * Summarize the identified cause(s) of the job failure (based on the provided text).
    * Provide at least two potential solutions to address the identified causes.
    * If possible, suggest additional troubleshooting steps for further investigation.
    * If provided text is not relevant to log please display to user to message e.g. "Please provide valid log details" 
    """
    text_input = st.text_area("Paste or type the relevant text related to the Databricks job failure (logs, error messages, etc.)", height=100)
    additional_info = st.text_area("Provide any additional information about the job (optional):", height=50)
    model = genai.GenerativeModel("gemini-pro")

    if st.button("Analyze", use_container_width=True):
        provided_text = text_input
        #prompt = prompt_template.format(provided_text=provided_text)
        prompt = prompt_template.format(provided_text=provided_text, additional_info=additional_info)
        response = model.generate_content(prompt)

        st.write("")
        st.header(":blue[Analysis Result]")
        st.write("")

        st.markdown(response.text)


if __name__ == "__main__":
    main()
