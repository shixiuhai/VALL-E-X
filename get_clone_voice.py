import requests

url = 'http://127.0.0.1:7000/textToVoice'  # 修改为您的API接口URL

params = {
    'text': """支持声音克隆！你可以使用任何人，角色，甚至是你自己的声音，来制作一个音频提示。在你使用该音频提示时，VALL-E X 将会使用与其相似的声音来合成文本。""",
    'promptName': "33f52a9f-4841-4693-a285-0af4dc889bc4"
}

response = requests.post(url, json=params)

if response.status_code == 200:
    with open('voice_clone.wav', 'wb') as f:
        f.write(response.content)
    print("Audio file saved as 'wav'")
else:
    print("Error:", response.text)