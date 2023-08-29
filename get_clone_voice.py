import requests

url = 'http://127.0.0.1:7000/textToVoice'  # 修改为您的API接口URL

params = {
    'text': "体验超凡的口腔清洁与舒适，我们自豪地推出全新的维尔牌高级抗菌电动牙刷。以先进的抗菌技术为基础，配备高效振动清洁，能轻松去除牙菌斑、污渍和食物残渣。多重清洁模式，智能提醒功能，以及持久续航，为您的口腔健康保驾护航。时尚外观和舒适握持设计，让您享受每一次刷牙的愉悦体验。选择维尔，迎接健康与自信的笑容！",
    'promptName': "dbd206bf-2ddb-40f3-962c-879ea05d656c"
}

response = requests.post(url, json=params)

if response.status_code == 200:
    with open('voice_clone.wav', 'wb') as f:
        f.write(response.content)
    print("Audio file saved as 'wav'")
else:
    print("Error:", response.text)