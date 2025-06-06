# 🧠 Business Process to Mermaid Flowchart Generator

This Streamlit app allows you to convert **natural language discussions** (such as conversations between a Business Analyst and a client) into **Mermaid flowcharts** using OpenAI's GPT models.

## ✨ Features

- 📝 Paste a business requirement discussion or transcript
- ➕ Optionally add a follow-up prompt or clarification
- 📊 Automatically generates Mermaid diagram syntax
- 🎨 Renders the Mermaid diagram live in the browser
- 🔁 Regenerate with new prompts without losing context

---

## 🚀 Getting Started

### 1. Clone the Repository

git clone https://github.com/your-username/mermaid-agent-app.git
cd mermaid-agent-app

### 2. Install Dependencies

pip install -r requirements.txt


### 3. Set OpenAI API Key
Create a .env file in the root directory with your OpenAI key:

OPENAI_API_KEY=your-openai-api-key-here


### 4. Run the App

streamlit run app.py


Then open the URL shown in your terminal (usually http://localhost:8501




### Example input

Priya (BA): Can you describe how appointments are currently booked?

Dr. Sharma: Right now, all appointments are booked manually by phone or walk-in...

Priya: Would you like to send notifications to patients?

Dr. Sharma: Yes, via SMS or email, especially for confirmations or delays...


### Follow-up Prompt (optional):

Add a decision node for if the doctor is unavailable.
