import streamlit as st
import openai

# Ensure you have set the API key as an environment variable or in Streamlit's >
openai.api_key = st.secrets["api_key"]

def query_model(prompt, model_name):
    response = openai.Completion.create(
        model=model_name,
        prompt=prompt,
        max_tokens=50,
        temperature=0.7
    )
    return response.choices[0].text.strip()

def main():
    st.title("GPT-3.5 Turbo Model Interface")

    user_input = st.text_area("Enter your text here", "")

    if st.button("Submit"):
        if user_input:
            with st.spinner('Generating response...'):
                response = query_model(user_input, "your-model-name")
                st.write(response)
        else:
            st.error("Please enter some text to process.")

if __name__ == "__main__":
    main()
