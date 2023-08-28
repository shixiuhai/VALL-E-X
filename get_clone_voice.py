import requests

url = 'http://127.0.0.1:7000/textToVoice'  # 修改为您的API接口URL

params = {
    'text': """这件商品的价格一百元""",
    'promptName': "33f52a9f-4841-4693-a285-0af4dc889bc4"
}

response = requests.post(url, json=params)

if response.status_code == 200:
    with open('voice_clone.wav', 'wb') as f:
        f.write(response.content)
    print("Audio file saved as 'wav'")
else:
    print("Error:", response.text)