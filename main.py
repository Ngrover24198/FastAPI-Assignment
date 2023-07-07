import uvicorn
import logging
from fastapi import FastAPI

from fastapi import Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from models.db_models import Assignment
from models import db_models
from utils.utils import get_add_details, update_details, get_data_response, get_trigger_data_response
from schema.request_schema import AddDataRequest, GetDataRequest, UpdateDataRequest
from schema.response_schema import GetDataResponse
from config.db_config import get_db, engine

# Using loggers in the code
logger = logging.getLogger(__name__)

# fast api binding the db engine
db_models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Add your routes and business logic here
# api endpoint to add the data in the db
@app.post("/add_data")
def add_data(user: AddDataRequest,  db: Session = Depends(get_db)):
    try:
        details = get_add_details(user)
        db.add(details)
        db.commit()
        return {"status": "success"}
    except Exception as e:
        logger.error(f"error: {str(e)}")
        return {
            "status": "not success",
            "error": str(e)
            }
        

# api endpoint to update the data in the table
@app.post("/update_data")
def update_data(user: UpdateDataRequest,  db: Session = Depends(get_db)):
    try:
        assignment = db.query(Assignment).filter_by(source_id=user.source_id).first()
        if assignment:
            update_details(assignment, user)
            db.commit()
            return {"status": "success"}
        
        return {
        "status": "success",
        "message": "No data present to be updated"
        }            
    except Exception as e:
        logger.error(f"error: {str(e)}")
        return {
            "status": "Not Success",
            "error": str(e)
            }
        
        
# api endpoint to get the details of the user
@app.post("/get_data")
def get_data(user: GetDataRequest,  db: Session = Depends(get_db)):
    try:
        details = db.query(Assignment).filter_by(source_id=user.source_id).first()
        response = get_data_response(details)
        return {"response": response}
    except Exception as e:
        logger.error(f"error: {str(e)}")
        return {
            "response": "ERROR: response is not generated",
            "error": str(e)
            }


# api endpoint to get trigger data
@app.post("/get_trigger_data")
def get_trigger_data(user: GetDataRequest,  db: Session = Depends(get_db)):
    try:
        details = db.query(Assignment).filter_by(source_id=user.source_id).first()
        response = get_data_response(details)
        if response:
            response = get_trigger_data_response(response)
        return {"response": response}
    except Exception as e:
        logger.error(f"error: {str(e)}")
        return {
            "response": "ERROR: response is not generated",
            "error": str(e)
            }


@app.get("/")
async def root():
    """Defining the root function as asynchronous,
    allows the server to handle multiple requests concurrently and ensures that the 
    application remains responsive even when executing time consuming operations."""
    return {"message": 'Edge Assignment'}

if __name__ == "__main__":
    # Start the FastAPI server at port 8000, http://localhost:8000/
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info", reload=True)