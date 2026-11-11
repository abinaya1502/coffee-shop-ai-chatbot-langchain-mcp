from agents.agent import Agent
from models.request_dto import ChatbotRequest
from utils.errors.error_log import log_error
from utils.errors.http_status import HttpStatusCode
from models.custome_app_exepction import CustomAppException
from utils.errors.error_codes import ErrorCode
import re
from langchain.agents.middleware._redaction import (
    apply_strategy,
    detect_email,
    detect_credit_card,
    detect_ip,
    detect_url,
)
 
class ChatbotService:
    def __init__(self):
        self.agent = Agent()
    async def chatbot_service(self,request: ChatbotRequest):
       
        try: 
            user_query = request.user_query
            customer_uuid = request.customer_uuid

            value = await self.create_pii_guardrails(user_query)
            result = await self.agent.chatbot_agent(value,customer_uuid)
            
            return result
        except Exception as e:
            log_error("chatbot_service.py","chatbot_service",str(e))
            raise CustomAppException(
                message=f"Service error: {str(e)}",
                code=ErrorCode.INTERNAL_SERVER_ERROR,
                status_code=HttpStatusCode.INTERNAL_SERVER_ERROR,
                 
            )
    async def create_pii_guardrails(self,user_query):
       
        try: 
            all_matches = (
                detect_email(user_query)
                + detect_credit_card(user_query)
                + detect_ip(user_query)
                + detect_url(user_query)
            )

            for m in all_matches:
                print(f"  detected  [{m['type']:15}]  {m['value']!r}")

            print()
            print("redact :", apply_strategy(user_query, all_matches, "redact"))
            print("mask   :", apply_strategy(user_query, all_matches, "mask"))
            print("hash   :", apply_strategy(user_query, all_matches, "hash"))

            processed_txt = apply_strategy(user_query, all_matches, "redact")
            return processed_txt
            
            
        except Exception as e:
            log_error("chatbot_service.py","chatbot_service",str(e))
            raise CustomAppException(
                message=f"Service error in creating the pii : {str(e)}",
                code=ErrorCode.INTERNAL_SERVER_ERROR,
                status_code=HttpStatusCode.INTERNAL_SERVER_ERROR,
                 
            )
        

 