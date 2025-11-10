import os
from model import model,memory
from dotenv import load_dotenv
import tools
from langchain.agents import create_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, SystemMessage
from state import DeepAgentState
from prompt import TODO_USAGE_INSTRUCTIONS,KYC_SYSTEM_BACKGROUND,FILE_USAGE_INSTRUCTIONS
from logconfig import logger

agent_executor = create_agent(
    model=model, 
    tools=tools.kyctools,
    checkpointer=memory,
    state_schema=DeepAgentState
    )

config = {"configurable": {"thread_id": "abc123"}}

load_dotenv()

INSTRUCTIONS = (
    f"You serve as a knowledgeable KYC SRE Engineer, providing expert assistance within compliance boundaries.\n\n Here are some backgrouds of the system: {KYC_SYSTEM_BACKGROUND} \n\n" + "=" * 80 + "\n\n" + f"Leverage available tools effectively to resolve issues while adhering to the following principles:\n\n{TODO_USAGE_INSTRUCTIONS}\n\n" + "=" * 80 + "\n\n" + f" Always write important information to files to retain context for later use. Use the file system as your long-term memory while adhering to the following principles: \n\n {FILE_USAGE_INSTRUCTIONS}"
)


prompt_template = ChatPromptTemplate.from_messages(
    
    
    messages=[
        ("system", INSTRUCTIONS),
        MessagesPlaceholder(variable_name="messages")
    ]
)


# query = "帮我分析一下IDAP-IDASC系统的日志，看看有没有异常？"
# query = "帮我分析一下流水号25102320001185434117360071666459， 这笔流水做了简单比对服务，请分析下这笔请求为什么失败？"

round = 0

while True:

    query = input("请输入你的问题(输入exit退出): ")
    if query.lower() == "exit":
        break

    if round == 0:
        input_messages = [HumanMessage(query)]

        prompt = prompt_template.invoke(input_messages)

        response = agent_executor.invoke({"messages": prompt.to_messages()},config=config)
    else:
        input_messages = [HumanMessage(query)]
        response = agent_executor.invoke({"messages": input_messages},config=config)

    
    # print("Final Response:", response)

    # for message in response["messages"]:
    #     message.pretty_print()

    for message in response["messages"]:
        logger.info(message.content)
    print(response["messages"][-1].content)

    round += 1

