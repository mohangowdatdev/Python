from speedtest import Speedtest
st=Speedtest()
print("download: ", st.download())
print("upload :", st.upload())
st.get_servers([])
print("ping :", st.results.ping)