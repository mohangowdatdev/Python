import speedtest
print("Please Wait for a moment")
s = speedtest.Speedtest()
s.get_best_server()
s.download()
s.upload()
res = s.results.dict()
print("Download : ", res["download"])
print("Upload : ", res["upload"])
