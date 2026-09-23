from fastapi import APIRouter , UploadFile ,Form,File
import PyPDF2
from app.schemas.document import documentuploadresponse
from app.services.document_processor import split_doc
import io
router = APIRouter()

@router.post("/document/upload",response_model=documentuploadresponse)
async def pdf_upload(
    bot_id :str= Form(...),
    index_name: str = Form(...),
    document: UploadFile = File(...)
):
    contents = await document.read()
    pdf_reader = PyPDF2.PdfReader(io.BytesIO(contents))  
    text = ""
    for page in  pdf_reader.pages:
        text += page.extract_text()

    split_doc(text,index_name)    
    return {
          "bot_id": bot_id,
          "index_name": index_name,
          "filename": document.filename,
          "pages": len(pdf_reader.pages),
          "message": "Document uploaded successfully"
      }





