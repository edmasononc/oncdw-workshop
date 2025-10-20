import streamlit as st
import os
from onc import ONC
import pandas as pd

st.title("Oceans 3.0 Open API Playground")
st.metric("Web Services", 2, 1)

token = os.getenv("ONC_TOKEN")
onc = ONC(token)

st.header(":blue[Discovery Services]")
with st.sidebar:
    st.markdown("[Discovery Services](#discovery-services)")
    st.markdown("[Real-time Services](#real-time-services)")

st.subheader(":green[Return locations]")
# col1, col2 = st.columns(2)
col1, col2 = st.tabs(["Discovery", "Real-time"])

st.markdown(":blue-badge[GET] `/locations`")
with col1:
    st.header(":blue[Discovery Services]")

location_code = st.text_input("locationCode", placeholder="FGPD")
st.subheader(":green[Return locations]")

if st.button("Run", key="location_button"):
    param = {"locationCode": location_code}
    location_info = onc.getLocations(param)
    st.json(location_info)
    st.markdown(":blue-badge[GET] `/locations`")

st.divider()
location_code = st.text_input("locationCode", placeholder="FGPD")

st.header(":blue[Real-time Services]")
if st.button("Run", key="location_button"):
        param = {"locationCode": location_code}
        location_info = onc.getLocations(param)
        st.json(location_info)

st.subheader(":green[Return archivefiles]")
with col2:
    st.header(":blue[Real-time Services]")

st.markdown(":blue-badge[GET] `/archivefile`")
st.subheader(":green[Return archivefiles]")

device_code = st.text_input("deviceCode", value="BPR_BC")
last_days = st.number_input("last days", value=4)
st.markdown(":blue-badge[GET] `/archivefile`")

if st.button("Run", key="archivefile_button"):
    param = {
        "deviceCode": device_code,
        "dateFrom": f"-P{last_days}D",
        "returnOptions": "all",
    }
    archivefile = onc.getArchivefile(param)
    df = pd.DataFrame(archivefile["files"])
    df["dateFrom"]=pd.to_datetime(df["dateFrom"])
    st.line_chart(df,x="dateFrom",y="uncompressedFileSize")
    device_code = st.text_input("deviceCode", value="BPR_BC")
    last_days = st.number_input("last days", value=4)

    if st.button("Run", key="archivefile_button"):
        param = {
            "deviceCode": device_code,
            "dateFrom": f"-P{last_days}D",
            "returnOptions": "all",
        }
        archivefile = onc.getArchivefile(param)
        df = pd.DataFrame(archivefile["files"])
        df["dateFrom"] = pd.to_datetime(df["dateFrom"])
        st.line_chart(df, x="dateFrom", y="uncompressedFileSize")


#with st.sidebar: # Sidebar content 
#    st.title("Oceans 3.0 Open API Playground") # Sidebar title
#    st.write("This is a simple Streamlit app to interact with the Oceans 3.0 Open API.") # Sidebar description
#    st.write("Enter your parameters and click 'Run' to see the results.") # Sidebar instructions