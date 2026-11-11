from repositories.mcp_server_repository import ChatbotRepository
from routes.mcp_server_router import mcp_router
repository=ChatbotRepository()
     
@mcp_router.tool
def check_order_status(order_id:int):
    """Check the status of a food order using the order ID"""
    status = repository.check_order_status_repo(order_id)
    if not status:
        return "No order found"
    return status


@mcp_router.tool
def check_inventory(item_name:str):
    """Check the inventory of the item"""

    inventory = repository.check_inventory_repo(item_name)
    if not inventory:
        return "Item not found"
    return inventory


@mcp_router.tool
def place_order(customer_id: int, items: list):
    """ Place the order for particular customer"""
    order = repository.place_order_repo(customer_id,items)
    return order



