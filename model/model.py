# Import relevant functionality
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langgraph.checkpoint.memory import MemorySaver

# Create the model and memory
load_dotenv()

model = init_chat_model(
    model=os.environ.get("Model"),
    base_url=os.environ.get("OPENAI_API_BASE"),
    api_key=os.environ.get("OPENAI_API_KEY"),model_provider='openai'
    )

memory = MemorySaver()