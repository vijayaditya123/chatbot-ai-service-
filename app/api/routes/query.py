from fastapi import APIRouter,Form
from app.schemas.query import user_query
from app.services.embedding_service import search_chunks
from app.services.llm_service import get_answer
router = APIRouter()

@router.post("/user_query",response_model=user_query)
async def user_question(
     bot_id :str= Form(...),
     index_name: str = Form(...),
     user_question:str =Form(...),
    ):
     print("USER_QUERY ENDPOINT HIT")
     results = search_chunks(user_question, index_name)
     context = "\n".join([r.page_content for r in results])
     messages = [
    # System Prompt
    {
        "role": "system",
        "content": """You are a helpful AI assistant specializing in information about
Narendra Modi, Prime Minister of India. You answer questions accurately based on
provided documents. You are professional, neutral, and factual in your responses.
You maintain a polite and respectful tone at all times, even if the user's message
is rude, off-topic, or inappropriate — in such cases, briefly and calmly redirect
the conversation back to your purpose without lecturing or being dismissive."""
    },

    # Retrieval Prompt
    {
        "role": "system",
        "content": f"""Use ONLY the following retrieved context to answer questions
about Narendra Modi. Do not add any information from your own knowledge, even if
you know the answer. If the answer is not found in the context, respond exactly
with: 'This information is not available in the provided documents.'

For simple greetings or small talk (e.g. "hello", "how are you", "thanks"),
respond naturally and briefly without needing document context, and gently
remind the user you're here to answer questions about Narendra Modi.

Context:
{context}"""
    },

    # Synthesis Prompt
    {
        "role": "system",
        "content": """Form a clear, concise, and well-structured answer. Keep the
response factual and to the point. Include specific dates, events, names, or
figures when they appear in the context. Do not repeat the question in your
answer. Do not use phrases like 'According to the context' or 'Based on the
provided documents' — just answer directly and naturally, as a knowledgeable
assistant would."""
    },

    {"role": "user", "content": user_question}
    ]
     final_result = await  get_answer(messages)
     return {
            "bot_id": bot_id,
            "index_name": index_name,
            "user_question": user_question,
            "answer": final_result["answer"],
            "input_tokens": final_result["input_tokens"],
            "output_tokens": final_result["output_tokens"]
     }
    
    
    
   


   
   