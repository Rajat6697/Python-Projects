import speedtest

test= speedtest.Speedtest()

print("------------Getting server List---------")
test.get_servers() # Get list of servers

print("------------Choosing Best Server--------")
best= test.get_best_server() # Choose best server
#---------------------------------------------------
#print(best)
# Output: {'url': 'http://speedtest.ultranet.co.in:8080/speedtest/upload.php', 'lat': '28.5700', 'lon': '77.3200', 'name': 'Noida', 'country': 'India', 'cc': 'IN', 'sponsor': 'Ultranet', 'id': '13173', 'host': 'speedtest.ultranet.co.in:8080', 'd': 5.125776079050784, 'latency': 17.936}
#--------------------------------------------------

print(f"Found: host {best['host']} located in {best['country']}")

print("------------Performing download test-----------------")
download_result= test.download() /1024 /1024

print("------------Preforming Upload test--------------------")
upload_result= test.upload() /1024 /1024

print("------------Checking Ping----------------------")
ping_result= test.results.ping

print(f"Download Speed: {download_result:.2f} Mbits/Sec")
print(f"Upload Speed: {upload_result:.2f} Mbits/Sec")
print(f"Ping: {int(ping_result)} ms")