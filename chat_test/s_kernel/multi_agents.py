# from semantic_kernel.contents import ChatMessageContent, AuthorRole
# from semantic_kernel import Kernel 
# from semantic_kernel.agents import AzureAIAgent, AgentGroupChat, Agent
# from openai import AzureOpenAI


# from dotenv import load_dotenv
# import os

# load_dotenv()

# # kernel.add_service(
# #     service=AzureChatCompletion(
# #         service_id="chat",
# #         api_key = os.getenv("API_KEY"),
# #         endpoint=os.getenv("ENDPOINT"),
# #         api_version=os.getenv("API_VERSION"),
# #         deployment_name=os.getenv("DEPLOYMENT")
# #     )
# # )

# kernel = Kernel()


# client = AzureOpenAI(
#     api_key=os.getenv("API_KEY"),
#     azure_endpoint=os.getenv("ENDPOINT"),
#     api_version=os.getenv("API_VERSION")
# )


# agent_one = AzureAIAgent(
#     client=client,
#     deployment_name=os.getenv("DEPLOYMENT"),
#     definition=Agent(
#         kernel=kernel,
#         name="agent_summar",
#         description="You are an assistant capable of summarizing any text on the topic it represents.",
#         type="assistant"
#     )
# )

# agent_two = AzureAIAgent(
#     client=client,
#     deployment_name=os.getenv("DEPLOYMENT"),
#     system_prompt="You are an assistant capable of counting the number of characters in a text."
# )


# agent_group = AgentGroupChat(
#     agents=[agent_one,agent_two]
# )

# async def get_message(asks: str):
#     message = ChatMessageContent(
#         role=AuthorRole.USER,
#         content=asks
#     )

#     await agent_group.add_chat_message(message=message)

#     result = await agent_group.run()

#     return result