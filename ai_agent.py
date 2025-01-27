# Step 1: Api keys for groq and tavily
import os
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_openai import ChatOpenAI
from langchain_core.messages.ai import AIMessage
from langgraph.prebuilt import create_react_agent
GROQ_API_KEY = os.environ.get('GROQ_API_KEY')
TAVILY_API_KEY = os.environ.get('TAVILY_API_KEY')
OPEANAI_API_KEY = os.environ.get('OPENAI_API_KEY')

# Step 2: Create a function to get response from AI agent
def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    if provider == "Groq":
        llm = ChatGroq(model=llm_id)
    elif provider == "OpenAI":
        llm = ChatOpenAI(model=llm_id)
    search_tool = TavilySearchResults(max_results=3)
    tools = [search_tool] if allow_search else []
    agent = create_react_agent(model=llm, tools=tools, state_modifier=system_prompt)
    state={"messages": query}
    message = agent.invoke(state).get("messages")
    ai_message = [messages.content for messages in message if isinstance(messages, AIMessage)]
    print(ai_message[-1])
    return ai_message[-1]