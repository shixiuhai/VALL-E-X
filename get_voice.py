import requests

url = 'http://104.225.236.140:8000/textToVoice'  # 修改为您的API接口URL

params = {
    'text': """一旦您的应用在调试模式下运行，您可以使用调试界面中的工具栏来控制代码的执行，查看变量的值，单步执行代码等""",
    'voice': 'zh-CN-YunxiNeural',  # 修改为您需要的语音模型
    'rate': '+0%',
    'volume': '+0%'
}

response = requests.post(url, json=params)

if response.status_code == 200:
    with open('edge1.wav', 'wb') as f:
        f.write(response.content)
    print("Audio file saved as 'wav'")
else:
    print("Error:", response.text)