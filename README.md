# **FinAgent: A Hybrid Financial AI Agent**

FinAgent is a lightweight financial AI agent that leverages OpenAI's GPT-4 and the Alpha Vantage API to provide intelligent, real-time responses to financial queries. By combining conversational AI with external APIs, FinAgent demonstrates the power and flexibility of hybrid agents in modern application development.

---

## **Features**
- **Conversational AI**: Uses OpenAI GPT-4 to understand and process user queries.
- **Real-Time Financial Data**: Integrates with the Alpha Vantage API to fetch up-to-date stock and financial information.
- **Hybrid Workflow**: Combines language understanding and API integration for intelligent, data-driven insights.

---

## **Medium Article**
Read a walkthrough of this project on Medium: [The Hybrid AI Agent: Integrating ChatGPT with External API](https://medium.com/@liorboord/the-hybrid-ai-agent-integrating-chatgpt-with-external-api-cbd11a165b0e)


---

## **Setup Instructions**

### **Prerequisites**
- Python 3.7+
- Alpha Vantage API Key (Get one from [Alpha Vantage](https://www.alphavantage.co/))
- OpenAI API Key (Sign up at [OpenAI](https://platform.openai.com/signup/))

### **Installation**
Clone the repository:
```bash
   git clone https://github.com/your-username/finagent.git
   cd finagent
```   


Install the required dependencies:

```bash
pip install -r requirements.txt
```

Set up your API keys in the config.py file:
```python
OPENAI_API_KEY = "your_openai_api_key"
ALPHAV_API_KEY = "your_alpha_vantage_api_key"
```
### **Usage**
```bash
python agent.py
```
