
 
from fastmcp import FastMCP


mcp_router = FastMCP("mcp-router")

 
 

from tools.tools import check_order_status
from tools.tools import check_inventory,place_order
from resourses.resourse import get_menu,get_location
from prompts.prompt import diet_planning,explain_menu,normal_prompt

