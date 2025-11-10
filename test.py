from langchain.chat_models import init_chat_model

model = init_chat_model(
    model="deepseek-v3",
    base_url="https://api.lkeap.cloud.tencent.com/v1",
    api_key="sk-pPa4s9UEFNNEHsWRmZ61jsiWRfQwM4hSRTkIaActEbrVLulG",
    model_provider='openai'
    )

print(type(model))

