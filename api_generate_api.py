from flask import Flask, request, jsonify
import openai
from flask_cors import CORS

# Configure OpenAI client
openai.api_base = "https://api.aieat.or.th/v1"
openai.api_key = "dummy"

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    # data = request.json
        # Get the 'data' parameter from the URL
    text = request.args.get('data', '')
    prompt = f"<|im_start|>system\nคุณคือผู้ช่วยตอบคำถามที่ฉลาดและซื่อสัตย์ และลงท้ายประโยคด้วยคำว่า ค่ะเปโกะ<|im_end|>\n<|im_start|>user\n{text}<|im_end|>\n<|im_start|>assistant\n"
    try:
        response = openai.Completion.create(
            model=".",  # Specify model name
            prompt=prompt,
            max_tokens=512,
            temperature=0.7,
            top_p=0.8,
            top_k=40,
        )
        return jsonify({"response": response.choices[0].text.strip()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)
