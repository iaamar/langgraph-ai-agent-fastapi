# Setup pydantic model (schema validation)
from model import AIRequestState
from fastapi import FastAPI
from ai_agent import get_response_from_ai_agent

app = FastAPI(title="LangGraph AI Agent")
MODEL_NAME = ["llama-3-70b-8192", "deepseek-r1-distill-llama-70b", "llama-3.3-70b-versatile", "gpt-40-mini"]
# Decorator to create an endpoint
@app.post("/chat_agent")

# Function to handle the endpoint with type hinting
async def chat_agent(request: AIRequestState):
    """
    This endpoint is used to create an AI agent and invoke it with the given messages
    """
    # Create AI agent
    if request.model_name not in MODEL_NAME:
        return {"error": "Model not supported"}
    response = get_response_from_ai_agent(llm_id=request.model_name, query=request.messages, allow_search=request.allow_search, system_prompt=request.system_prompt, provider=request.model_provider)
    return response

# Run the FastAPI app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)