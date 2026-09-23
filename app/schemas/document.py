from pydantic import BaseModel

class documentupload(BaseModel):
    bot_id: str
    index_name: str
    document: str

class documentuploadresponse(BaseModel):
      bot_id: str
      index_name: str
      filename: str
      pages: int
      message: str