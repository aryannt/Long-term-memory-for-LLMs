# Long-term Memory for LLMs

## Overview

This project provides a backend service that enables long-term memory for Large Language Models (LLMs) using vector storage. It allows users to store, retrieve, and delete memories associated with their interactions, leveraging OpenAI's GPT-4 Turbo and AWS S3 for vector storage.

## Technologies Used and Rationale

### Python & Flask
- **Why Used:** Python is widely adopted for AI and backend development due to its simplicity and rich ecosystem. Flask is a lightweight web framework ideal for building REST APIs quickly.
- **Impact:** Rapid development, easy integration with AI libraries, and strong community support.
- **Comparison:** Flask is more lightweight and flexible than Django for small APIs, and Python offers more AI/ML libraries than languages like Java or Go.

### LangChain
- **Why Used:** LangChain provides abstractions for working with LLMs and vector stores, making it easier to build memory and retrieval systems.
- **Impact:** Simplifies integration with LLMs and vector databases, reducing boilerplate and improving maintainability.
- **Comparison:** LangChain is more specialized for LLM workflows than general-purpose libraries, and supports multiple backends.

### OpenAI API (GPT-4 Turbo)
- **Why Used:** GPT-4 Turbo offers state-of-the-art language understanding and generation, crucial for extracting and responding to user memories.
- **Impact:** High-quality responses, robust fact extraction, and reliable context handling.
- **Comparison:** OpenAI models outperform many open-source alternatives in accuracy and reliability, and GPT-4 Turbo is more cost-effective and faster than previous models.

### AWS S3 (Vector Store)
- **Why Used:** S3 provides scalable, durable, and cost-effective storage for vector embeddings, with easy integration into cloud workflows.
- **Impact:** S3 Vectors is purpose-built for storing and querying large vector datasets, making it ideal for AI agents and semantic search. It significantly reduces the cost of vector operations, supports sub-second query performance, and allows you to scale to billions of vectors with the same reliability and elasticity as standard S3. This enables applications to efficiently organize, search, and maintain vector indexes at scale, improving both the memory and context capabilities of AI systems.
- **Comparison:** S3 offers greater scalability, durability, and cost optimization compared to local storage or smaller cloud providers, and integrates seamlessly with other AWS services.

## Architecture

- **Backend:** Python (Flask), LangChain, OpenAI API, AWS S3
- **Frontend:** (Currently empty; add details when implemented)

### Main Components

- [`backend/app.py`](backend/app.py): Flask API endpoints for messaging and memory management.
- [`backend/memory_agent.py`](backend/memory_agent.py): Handles extraction, storage, retrieval, and deletion of user memories.
- [`backend/vector_store.py`](backend/vector_store.py): Configures the vector store using AWS S3 and OpenAI embeddings.
- [`backend/requirements.txt`](backend/requirements.txt): Lists Python dependencies.

## Setup

### Prerequisites

- Python 3.8+
- AWS account (for S3)
- OpenAI API key

### Installation

1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd Long-term-memory-for-LLMs/backend
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables in a `.env` file:
   ```
   OPENAI_API_KEY=your_openai_api_key
   AWS_S3_BUCKET=your_s3_bucket_name
   AWS_REGION=your_aws_region
   AWS_ACCESS_KEY_ID=your_aws_access_key_id
   AWS_SECRET_ACCESS_KEY=your_aws_secret_access_key
   ```

## Usage

### Running the Backend

Start the Flask server:
```bash
python app.py
```

### API Endpoints

- `POST /message`
  - Request: `{ "userId": "<user_id>", "message": "<user_message>" }`
  - Response: `{ "reply": "<llm_response>" }`
  - Stores relevant facts from the message and retrieves related memories.

- `POST /forget`
  - Request: `{ "userId": "<user_id>", "message": "<forget_message>" }`
  - Response: `{ "reply": "<llm_response>" }`
  - Deletes specified memories for the user.

## Code Structure

- `MemoryAgent`: Main class for memory operations.
- `vector_store`: AWS S3-based vector store for memory storage.
- Uses LangChain for LLM and vector operations.