
import requests


# The CSR content you want to send
csr_file = open("CSR.csr", "rb")
csr_content=csr_file.read()
print(csr_content)


# URL of the API endpoint
url = "http://129.82.44.147:10200/sign-csr?sid=your_id"

# Sending the Get request with csr_content as form data
response = requests.get(url, data={'csr_content': csr_content}, verify=False)


# Check if the request was successful
if response.status_code == 200:
    # Extract the desired filename from the Content-Disposition header
    content_disposition = response.headers.get('Content-Disposition')
    filename = "cert.pem"  # default name if extraction fails
    if content_disposition:
        fname_pos = content_disposition.find('filename=')
        if fname_pos != -1:
            filename = content_disposition[fname_pos + 9:].strip()

    # Save the PEM file
    with open(filename, 'wb') as file:
        file.write(response.content)



    print(f"File saved as {filename}")

 

else:
    print(f"Error with status code: {response.status_code}")
    print(response.text)


