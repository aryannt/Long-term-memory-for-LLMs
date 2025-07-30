from langchain.chat_models import ChatOpenAI
from vector_store import vector_store
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4-turbo", openai_api_key=os.getenv('OPENAI_API_KEY'))

class MemoryAgent:
    def __init__(self, user_id):
        self.user_id = user_id

    def extract_fact(self, message):
        prompt = f'''
        Extract a concise memory from this user message or return "none":

        "{message}"
        '''
        response = llm.predict(prompt)
        return None if response.strip().lower() == "none" else response.strip()

    def store_memory(self, fact):
        metadata = {"user_id": self.user_id}
        vector_store.add_texts([fact], metadatas=[metadata])

    def retrieve_memory(self, query, k=3):
        docs = vector_store.similarity_search(query, k=k, filter={"user_id": self.user_id})
        return [doc.page_content for doc in docs]

    def delete_memory(self, keyword):
        docs = vector_store.similarity_search(keyword, k=5, filter={"user_id": self.user_id})
        for doc in docs:
            if keyword.lower() in doc.page_content.lower():
                vector_store.delete(ids=[doc.metadata['id']])
