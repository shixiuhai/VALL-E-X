from flask import Flask, request, jsonify,make_response,Response
from utils.prompt_making import make_prompt
import uuid
import tempfile
from utils.generation import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
import os
# https://plachtaa.github.io/ # 网页demo
preload_models()


app = Flask(__name__)

def text_to_voice(text:str, promptName:str):
    try:
        audio_array = generate_audio(text, prompt=promptName)
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_file:
            # save audio to disk
            write_wav(temp_file.name, SAMPLE_RATE, audio_array)
            with open(temp_file.name, 'rb') as audio_file:
                audio_data = audio_file.read()

            # os.remove(temp_file.name)  # 清除临时文件

            return Response(audio_data, content_type='audio/mpeg')
    
    except Exception as e:
        return make_response(jsonify({"error": "An error occurred: " + str(e),"code":500}), 500)

def generate_prompt(audio_prompt_path:str, transcript:str):
    try:
        promptName=str(uuid.uuid4())
        make_prompt(name=promptName, audio_prompt_path=audio_prompt_path,
        transcript=transcript)
        # os.remove(audio_prompt_path)
        return make_response(jsonify({"promptName":promptName,"code":200}),200)
    except Exception as e:
        return make_response(jsonify({"error": "An error occurred: " + str(e),"code":500}), 500)


@app.route('/generatePrompt', methods=['POST'])
def voice_generate_prompt():
    file = request.files['file']
    promptText = request.form.get('promptText')
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_file:
        file.save(temp_file)
        return generate_prompt(temp_file.name,promptText)
    
@app.route('/textToVoice', methods=['POST'])
def voice_text_to_voice():
    data = request.get_json()
    text = data.get("text")
    promptName = data.get("promptName")
    return text_to_voice(text,promptName)
    
    

if __name__ == "__main__":
    
    app.run(host='0.0.0.0',port=7000,threaded=1)