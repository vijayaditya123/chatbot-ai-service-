from azure.ai.inference import ChatCompletionsClient
from azure.core.credentials import AzureKeyCredential
from app.core.config import LLM_API_KEY,LLM_BASE_URL,LLM_MODEL




async def get_answer(message):
    client = ChatCompletionsClient(
       endpoint=LLM_BASE_URL,
       credential=AzureKeyCredential(LLM_API_KEY)
  )
    response = client.complete(
    messages = message,
    model = LLM_MODEL,
    temperature= 0.7,
    max_tokens=  150
    )
    return{
        "answer" :  response.choices[0].message.content,
        "why_it_stopped" : response.choices[0].finish_reason,
        "input_tokens" : response.usage.prompt_tokens,
        "output_tokens" : response.usage.completion_tokens
    }
