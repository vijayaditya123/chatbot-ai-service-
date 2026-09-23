from pydantic import BaseModel

class user_query(BaseModel):
    bot_id: str
    index_name: str
    user_question: str
    answer: str
    input_tokens: int
    output_tokens: int