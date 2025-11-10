# pip install -qU "langchain[anthropic]" to call the model

import os
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model


model = init_chat_model(
        model="deepseek-v3",
        base_url="https://api.lkeap.cloud.tencent.com/v1",
        api_key="sk-pPa4s9UEFNNEHsWRmZ61jsiWRfQwM4hSRTkIaActEbrVLulG",
        model_provider='openai'
        )


def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = create_agent(
    model=model,
    tools=[get_weather],
    system_prompt="You are a helpful assistant",    
)

# Run the agent
response = agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
)


for message in response["messages"]:
    message.pretty_print()

# import os
# from langchain.chat_models import init_chat_model

# os.environ["OPENAI_API_KEY"] = "sk-..."

# model = init_chat_model("gpt-4.1")