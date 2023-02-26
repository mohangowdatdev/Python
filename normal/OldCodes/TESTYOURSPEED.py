# Python program to test WIFI/DATA Speed.
# First you must install speedtest module
# pip install speedtest-cli

import speedtest

st = speedtest.Speedtest()
st.get_best_server()
option = int(input('''What speed do you want to test: 
1) Download Speed 
2) Upload Speed 
3) Ping 
4) All the three
Your Choice: '''))
print("Please Wait for a moment")


if option == 1:
	d = st.download()
	d = d/1000000
	print("Download : ",d)
elif option == 2:
	u = st.upload()
	u = u/1000000
	print("Upload : ",u)

elif option == 3:
	servernames =[]
	st.get_servers(servernames)
	p = st.results.ping
	print("Ping : ",p)
elif option == 4:
	d = st.download()
	d = d / 1000000
	print("Download : ", d)
	u = st.upload()
	u = u/1000000
	print("Upload : ", u)
	servernames =[]
	st.get_servers(servernames)
	p = st.results.ping
	print("Ping : ",p)
else:
	print("Please enter the correct choice !")
