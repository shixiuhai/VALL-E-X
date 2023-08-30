import requests

url = 'http://124.222.114.154:7500/textToVoice'  # 修改为您的API接口URL

params = {
    'text': "体验超凡的口腔清洁与舒适",
    'promptName': "3fabef64-7986-434e-ae3b-ff36c424a8ae"
}

response = requests.post(url, json=params)

if response.status_code == 200:
    with open('voice_clone.wav', 'wb') as f:
        f.write(response.content)
    print("Audio file saved as 'wav'")
else:
    print("Error:", response.text)