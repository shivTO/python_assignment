
import streamlit as st
import os
import requests
from dotenv import load_dotenv
import streamlit_google_oauth as oauth
header=st.container()
login=st.container()
register=st.container()
get=st.container()
post=st.container()


with header:
    st.title("Python assignment")



load_dotenv()
client_id = os.environ["GOOGLE_CLIENT_ID"]
client_secret = os.environ["GOOGLE_CLIENT_SECRET"]
redirect_uri = os.environ["GOOGLE_REDIRECT_URI"]


# with login:
#     login_info = oauth.login(
#         client_id=client_id,
#         client_secret=client_secret,
#         redirect_uri="redirect_uri",
#         login_button_text="Continue with Google",
#         logout_button_text="Logout",
#     )
#     print(login_info)
#     if login_info:
#         user_id, user_email = login_info
#         st.subheader(f"Welcome {user_email}")
#     else:
#         st.subheader("Please login")
url="http://127.0.0.1:8000/api"
with get:
    if st.button("Getting the data",disabled=False):
        res=requests.get(url=url)
        st.subheader(res.text)
with post:
    pl=st.text_input(label="Add petal length")
    pw=st.text_input(label="Add petal width")
    sl=st.text_input(label="Add sepal length")
    sw=st.text_input(label="Add sepal width")
    cl=st.text_input(label="Add class")
    obj={'pl':pl,'sl':sl,'pw':pw,'sw':sw,'cl':cl}
    if pl and pw and sl and sw and cl:
        if st.button("Posting the data",disabled=False):
            res=requests.post(url,obj)
            st.subheader(res.text)
            
