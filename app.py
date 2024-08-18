### openAI api 코드 ###
import openai
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv('OPENAI_API_KEY')

def chatAI(msg): 
    chatAnswer = openai.ChatCompletion.create( 
        model="gpt-3.5-turbo", 
        messages=[{"role":"system","content":"answer in detail and kindly like an elementary school teacher. you only answer in Korean"}, 
                    {"role":"user", "content": msg}] )
    result = chatAnswer.choices[0].message.content

    return result


### 플라스크 코드 ###
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def indexChat():
    # 기본 index 페이지 
    print("하이롱")
    return render_template("index.html")

@app.route('/result', methods=['POST','GET'])
def resultChat():
    # msg_input(POST방식으로 데이터 전송)
    msg_input = request.form["msg_input"]
    
    # 질문 완성 및 그림 리스트 뽑기
    result = chatAI(msg_input)

    print("질문 : ", msg_input)
    print("결과 : ", result)


    return render_template("result.html", result = result)

if __name__ == '__main__':
    app.run('0.0.0.0',port=5000, debug=False)