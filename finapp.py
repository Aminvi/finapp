import os
from phi.assistant import Assistant
from phi.llm.groq import Groq




groq_api_key = "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"

  
def ai(prompt, totalBudget, totalIncome, totalSpend):

    assistant = Assistant(
    llm=Groq(model="llama3-70b-8192", api_key=groq_api_key, max_tokens=6000),
    description=f"Based on the following financial data: - Total Budget: {totalBudget} USD - Expenses: {totalSpend} USD - Incomes: {totalIncome} USD Provide detailed financial advice in 2 sentence to help the user manage their finances more effectively.",
    # debug_mode=True,
    )
    
    response = assistant.run(prompt, stream=False)
    return response