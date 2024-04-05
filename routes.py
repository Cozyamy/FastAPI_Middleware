from fastapi import APIRouter, File, UploadFile
from services import get_file_mime_type

router = APIRouter()

@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    """
    Uploads a file and returns its filename and MIME type.

    Parameters:
        file (UploadFile): The file to upload.

    Returns:
        dict: A dictionary containing the filename and MIME type of the uploaded file.
    """
    file_content = await file.read()
    mime_type = get_file_mime_type(file_content)
    return {"filename": file.filename, "mime_type": mime_type}