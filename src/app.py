from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from bs4 import BeautifulSoup
from src.model_invoke import generate_summary
from src.postprocess_xml import process_xml_file
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

app = FastAPI()


@app.post("/summarize")
async def summarize(file: UploadFile = File(...)):
    # Ensure the uploaded file is an XML file
    if not file.filename.endswith('.xml'):
        raise HTTPException(status_code=400, detail="Invalid file format. Please upload an XML file.")
    try:
        content = await file.read()
        xml_content = content.decode('utf-8')
        soup = BeautifulSoup(xml_content, 'xml')
        logger.info("Received a request to the root endpoint with the xml file")
        text_to_summarize = process_xml_file(soup)
        if not text_to_summarize:
            raise HTTPException(status_code=400, detail="No text found in the XML file.")
        summary = generate_summary(text_to_summarize)
        return JSONResponse(content={"summary": summary})

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Start the FastAPI app with Uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

