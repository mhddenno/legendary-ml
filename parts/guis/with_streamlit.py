import streamlit as st

class InputERROR(Exception):
    def __init__(self, title, message):
        self.title = title
        self.message = message
        super().__init__(self.message)

def upload() -> None:
    file = st.file_uploader("Upload your file here")
    process_input("upload", file)

def free_text() -> None:
    text = st.text_area("Write your text here")
    process_input("text", text)

def url() -> None:
    url = st.text_input("Write your URL here")
    process_input("URL", url)

def process_input(type: str, input: str) -> None:
    st.button(f"Inject the -{type}- input to the model")
    output(input)

def output(output: str) -> None:
    st.subheader('Summarization')
    st.subheader('Study plan')
    st.subheader('Feeling about the input')
    st.write(output)

def main() -> None:
    st.title("Your Secretary is here to help you!")
    st.balloons()

    selected_box = st.selectbox("How do you want to give your input", ["Upload", "Free Text", "URL"])
    
    if selected_box == "Upload":
        upload()
    elif selected_box == "URL":
        url()
    elif selected_box == "Free Text":
        free_text()
    else:
        raise InputERROR("Invalid input", "You can only choose from the given options Upload, Url or Free text")


if __name__ == "__main__":
    main()