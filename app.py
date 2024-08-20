from flask import Flask, request, jsonify
import os
from phi.assistant import Assistant
from phi.llm.groq import Groq
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

groq_api_key = "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"

def ai(prompt):
    print(prompt)
    assistant = Assistant(
        llm=Groq(model="llama3-70b-8192", api_key=groq_api_key, max_tokens=6000),
        description="You are an AI assistant that specialises in giving financial advice based on the user's provided spending. Provide detailed financial advice in 2 sentences to help the user manage their finances more effectively."
    )
    response = assistant.run(prompt, stream=False)
    return response

@app.route('/ai', methods=['POST'])
def ai_endpoint():
    # For demonstration purposes, using hardcoded values
    data = request.json
    totalBudget = data.get('totalBudget')
    totalIncome = data.get('totalIncome')
    totalSpend = data.get('totalSpend')
    print(totalBudget)
    prompt = f"The following financial data: - Total Budget: {totalBudget} Naira - Expenses: {totalSpend} Naira - Incomes: {totalIncome} Naira. Provide detailed financial advice in 2 sentences to help the user manage their finances more effectively."

    result = ai(prompt)
    print(result)
    return jsonify({"response": result})

if __name__ == '__main__':
    app.run(debug=True)
