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
     results = search_chunks(user_question, index_name)
     context = "\n".join([r.page_content for r in results])
     messages = [
        # System Prompt
        {
          "role": "system", 
          "content": """You are an expert AI assistant specializing in information about
  Narendra Modi, Prime Minister of India. You answer questions accurately based on provided
  documents. You are professional, neutral and factual in your responses."""
      },
      
      # Retrieval Prompt
      {
          "role": "system", 
          "content": f"""Use ONLY the following retrieved information about Narendra Modi to
  answer the question. If the answer is not found in the context, respond with: 'This
  information is not available in the provided documents.' Do not add any information from
  your own knowledge.\n\nContext:\n{context}"""
      },
      
      # Synthesis Prompt
      {
          "role": "system", 
          "content": """Form a clear and concise answer. Keep the response factual and to the
  point. If dates, events or facts are mentioned in context, include them. Do not repeat the
  question in your answer."""
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
    
    
    
   


   
   