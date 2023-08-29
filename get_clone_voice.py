import requests

url = 'http://127.0.0.1:7000/textToVoice'  # 修改为您的API接口URL

params = {
    'text': "凡本网注明来源。中国经济网或来源,经济日报，你好今天几月几日，我要好好学习，天津的跳水大爷们，突然引发了大量的关注，中国新闻周刊了解到，天津大爷们的跳水方式颇具特色，伴随着天津跳水大爷短视频的爆火，也有的质疑大爷们跳水的合规性与安全性，并对其能否良性发展表示担忧。",
    'promptName': "626c908d-9ea2-48be-b8d8-f57af4d5753a"
}

response = requests.post(url, json=params)

if response.status_code == 200:
    with open('voice_clone.wav', 'wb') as f:
        f.write(response.content)
    print("Audio file saved as 'wav'")
else:
    print("Error:", response.text)