from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
import io

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
for model in genai.list_models():
    print(model.name, model.supported_generation_methods)

model = genai.GenerativeModel("models/gemini-2.5-flash")
def get_gemini_response(input,image,prompt):
    response=model.generate_content([input,image[0],prompt])
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # e.g. image/png, image/jpeg
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")


st.set_page_config(page_title="MultiLanguage Invoice Extractor")
st.header("MultiLanguage Invoice Extractor")
input = st.text_input("Input: ", key="input")
uploaded_file = st.file_uploader("Upload an image of the invoice", type=["png", "jpg", "jpeg"])

image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image.",use_column_width=True)

submit=st.button("Submit")

input_prompt="""
you are an expert in understanding invoice .
we will upoad an image as the invoice and you will have to answer
 any questions based on the uploaded invoice image"""

## if submit button is clicked
if submit:
    image_data=input_image_details(uploaded_file)
    response=get_gemini_response(input_prompt,image_data,input)
    st.subheader("Here is your response")
    st.write(response)