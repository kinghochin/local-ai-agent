# 🍷 Wine Descriptor Offline API Demo

A lightweight FastAPI demo showcasing an **offline** Hugging Face model (`google/flan-t5-small`) to generate wine flavor descriptions and food pairings.

## Full Tutorial on Medium
Learn how this demo was built, with detailed explanations of prompt design, API setup, and deployment:

[Run a LLM Locally as a REST API: Gain Full Control and Enhanced Security](https://medium.com/@it.works/run-a-llm-locally-as-a-rest-api-gain-full-control-and-enhanced-security-44a1c47870fa?sk=6ae642080ec60030fdbc7c53e28e4c6f)

---

## Features

- Offline LLM inference using the `transformers` library  
- FastAPI server with interactive Swagger UI documentation  
- Returns structured JSON including wine flavors, finish, and suggested food pairings  
- No internet or OpenAI API key required — runs completely offline  

---

## Running Locally

1. **Clone the repo and install dependencies:**

   ```bash
   git clone https://github.com/kinghochin/local-ai-agent.git
   cd local-ai-agent
   pip install -r requirements.txt

2. **Run the FastAPI server:

   ```bash
   Copy
   Edit
   uvicorn main:app --reload

3. **Test the API in your browser:

   ```bash
   Open http://localhost:8000/docs for Swagger UI to try out the /generate endpoint interactively.

---




