from azure.ai.inference import ChatCompletionsClient
from azure.core.credentials import AzureKeyCredential
from app.core.config import LLM_API_KEY, LLM_MODEL

AZURE_RESOURCE_URL = "https://aditya-foundry-ai.openai.azure.com"


async def get_answer(message):
    client = ChatCompletionsClient(
        endpoint=f"{AZURE_RESOURCE_URL}/openai/deployments/{LLM_MODEL}",
        credential=AzureKeyCredential(LLM_API_KEY),
        api_version="2024-06-01",
    )

    response = client.complete(
        messages=message,
        model_extras={
            "max_completion_tokens": 250
        },
    )

    return {
        "answer": response.choices[0].message.content,
        "why_it_stopped": response.choices[0].finish_reason,
        "input_tokens": response.usage.prompt_tokens,
        "output_tokens": response.usage.completion_tokens,
    }