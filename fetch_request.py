import requests

async def download(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(f'data/{filename}', 'wb') as f:
            f.write(response.content)
    else:
        print("Error: ", response.status_code)