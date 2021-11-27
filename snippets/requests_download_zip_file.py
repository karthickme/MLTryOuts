# importing the requests module
import requests
url = "https://academic.udayton.edu/kissock/http/Weather/gsod95-current/allsites.zip"
print('Downloading started')

# Downloading the file by sending the request to the URL
req = requests.get(url)

# Split URL to get the file name
filename = url.split('/')[-1]

# Writing the file to the local file system
with open(filename, 'wb') as output_file:
    output_file.write(req.content)
print('Downloading Completed')
