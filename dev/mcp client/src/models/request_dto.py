import decimal

from pydantic import BaseModel

class ChatbotRequest(BaseModel):
    customer_uuid : str
    user_query: str

class ChatbotResponse(BaseModel):
    user_query : str
    response : str

class ChatbotOrderResponse(BaseModel):
    user_query: str
    item_name : list
    quantity : list
    response : str
    