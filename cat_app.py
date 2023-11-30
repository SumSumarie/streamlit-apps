import streamlit as st
import requests

####code to config the page
st.set_page_config(
    page_title="Cat App",
    page_icon=":Cat:"
)

st.header("WELCOME TO MY :cat: APP", divider='rainbow')
####


def get_content():
    """Access the API and get the image URL"""
    contents=requests.get('https://cataas.com//cat')
    return contents.content

def place_cat_image():
    cat_image = get_content()
    st.image(cat_image,width=200)


st.button("Click here",
          help="Click to get a cat image",
          on_click=place_cat_image)

#test=get_content()






