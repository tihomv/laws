import requests
import os


def download_ipc():
    file_name = "ipc.pdf"
    path = os.getcwd()
    REMOVE_DIR = str(path.split('\\')[-1])
    RESOURCE_DIR = str(path)
    RESOURCE_DIR = RESOURCE_DIR.replace(REMOVE_DIR, '')
    RESOURCE_ROOT = os.path.join(RESOURCE_DIR, 'resource')
    RESOURCE_ROOT = os.path.join(RESOURCE_ROOT, file_name)
    url = 'https://legislative.gov.in/sites/default/files/A1860-45.pdf'
    response = requests.get(url)
    with open(RESOURCE_ROOT, 'wb') as f:
        f.write(response.content)
    return RESOURCE_ROOT
