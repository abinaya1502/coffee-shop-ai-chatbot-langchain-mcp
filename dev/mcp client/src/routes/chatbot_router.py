from fastapi import APIRouter

from models.api_response_dto import APIResponse
from models.request_dto import ChatbotRequest
from utils.errors.error_log import log_error
from utils.errors.http_status import HttpStatusCode
from services.chatbot_service import ChatbotService
from models.custome_app_exepction import CustomAppException
from utils.errors.error_codes import ErrorCode
 
 
router = APIRouter(prefix="/api/v1")
 
 
@router.post("/chatbot")
async def chatbot_router(request:ChatbotRequest):
    
    try:
        service = ChatbotService()
        result = await service.chatbot_service(request = request)
 
        return APIResponse(
            data= result,
            code= HttpStatusCode.OK
        ).to_dict()
 
 
    except Exception as e:
        log_error("chatbot_router.py","router",str(e))
        raise CustomAppException(
            message=f"Router error: {str(e)}",
            code=ErrorCode.INTERNAL_SERVER_ERROR,
            status_code=HttpStatusCode.INTERNAL_SERVER_ERROR,
            
        )
 