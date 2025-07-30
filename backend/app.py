from flask import Flask, request, jsonify
from memory_agent import MemoryAgent
from dotenv import load_dotenv
import os
from langchain.chat_models import ChatOpenAI

load_dotenv()

app = Flask(__name__)

llm = ChatOpenAI(model="gpt-4-turbo", openai_api_key=os.getenv('OPENAI_API_KEY'))

@app.route('/message', methods=['POST'])
def message():
    data = request.json
    user_id = data['userId']
    message = data['message']

    memory_agent = MemoryAgent(user_id)

    fact = memory_agent.extract_fact(message)
    if fact:
        memory_agent.store_memory(fact)

    relevant_memories = memory_agent.retrieve_memory(message)

    context = "\n".join(relevant_memories)
    prompt = f'''
    User message: "{message}"
    Relevant memories:
    {context if context else 'None'}

    Respond to the user's message using relevant memories.
    '''
    response = llm.predict(prompt)

    return jsonify({"reply": response})

@app.route('/forget', methods=['POST'])
def forget():
    data = request.json
    user_id = data['userId']
    message = data['message']

    memory_agent = MemoryAgent(user_id)

    deletion_prompt = f'''
    Identify the keyword or fact the user wants to forget from this message, else return 'none':

    "{message}"
    '''
    keyword = llm.predict(deletion_prompt).strip()

    if keyword.lower() != "none":
        memory_agent.delete_memory(keyword)
        return jsonify({"deleted": True, "keyword": keyword})
    else:
        return jsonify({"deleted": False})

if __name__ == '__main__':
    app.run(debug=True)
