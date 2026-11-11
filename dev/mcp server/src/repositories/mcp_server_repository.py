from repositories.database import Database
from repositories.schema.schema import Item, Order, OrderItemMapping



class ChatbotRepository:
    def __init__(self):
        self.db_instance = Database()
    def check_order_status_repo(self,order_id) :
        db=None
        try:
            db = self.db_instance.SessionLocal()
            order = db.query(Order).filter(Order.order_id == order_id).first()
            if not order:
                return None
            return order.order_status
        except Exception as e:
            
            print("Error in repo",str(e))
            db.rollback()
            return None
        finally:
             if db:
                db.close()
    
    def check_inventory_repo(self,item_name) :
        db=None
        try:
            db = self.db_instance.SessionLocal()
            inventory = db.query(Item).filter(Item.item_name.ilike(f"%{item_name}%")).first()
            if not inventory:
                return None
            return inventory.stock_availability
        except Exception as e:
            db.rollback()
            print("Error in repo",str(e))
            db.rollback()
            return None
        finally:
             if db:
                db.close()
    def check_menu_repo(self):
        db=None
        try:
            db = self.db_instance.SessionLocal()
            item = db.query(Item).all()
            menu = []
            for items in item:
                menu.append({
                    "name":items.item_name,
                    "price":items.item_price
                })
           
            return menu
        except Exception as e:
            print("Error in repo",str(e))
            db.rollback()
            return None
            
        finally:
             if db:
                db.close()
    # def get_order_details_repo(self):
    #     db = None
    #     try:
    #         db = self.db_instance.SessionLocal()
    
    #         orders = db.query(Order).all()
    
    #         order_list = []
    
    #         for order in orders:
    
    #             mappings = db.query(OrderItemMapping, Item).join(
    #                 Item, Item.item_id == OrderItemMapping.item_id
    #             ).filter(
    #                 OrderItemMapping.order_id == order.order_id
    #             ).all()
    
    #             items = []
    
    #             for mapping, item in mappings:
    #                 items.append({
    #                     "item_name": item.item_name,
    #                     "price": float(item.item_price),
    #                     "quantity": mapping.quantity
    #                 })
    
    #             order_list.append({
    #                 "order_id": order.order_id,
    #                 "customer_id": order.customer_id,
    #                 "status": order.order_status,
    #                 "items": items
    #             })
    
    #         return order_list
    
    #     except Exception as e:
    #         print("Repo error:", str(e))
    #         return None
    
    #     finally:
    #         if db:
    #             db.close()

    def place_order_repo(self,customer_id, items):
        db=None
        try:
            db = self.db_instance.SessionLocal()
            total = 0
            order = Order(customer_id = customer_id)
            db.add(order)
            db.commit()
            for item in items:
                name = item["item_name"]
                quantity = item["quantity"]
                item = db.query(Item).filter(Item.item_name.ilike(f"%{name}%")).first()
                if item:
                    total += float(item.item_price)* quantity
                    mapping = OrderItemMapping(
                        order_id = order.order_id,
                        item_id = item.item_id,
                        quantity = quantity
                    )
                    db.add(mapping)
            db.commit()
            return {
                "order_id" : order.order_id,
                "total_price": total,
                "items": items
            }
        except Exception as e:
            print("Error in repo",str(e))
            db.rollback()
            return None
            
        finally:
             if db:
                db.close()
    
        
        
    