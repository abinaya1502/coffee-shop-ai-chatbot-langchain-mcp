from sqlalchemy.orm import Session
from repositories.database import Database
from repositories.schema.schema import Customer, Item, Order, OrderItemMapping
 
 
class Seeder:
    def __init__(self):
        self.db = Database()
       
    def seed_data(self):
        session = self.db.SessionLocal()
        try:
 
            if not session.query(Customer).first():
                session.add_all([
                    Customer(customer_name="Abinaya",customer_contact="9876543210",customer_email="abi@gmail.com",customer_address="Bangalore"),
                    Customer(customer_name="Rithanya",customer_contact="9876543211",customer_email="rithanya@gmail.com",customer_address="Coimbatore"),
                    Customer(customer_name="Kesav",customer_contact="9876543212",customer_email="kesav@gmail.com",customer_address="Hyderabad"),
                    Customer(customer_name="Naufal",customer_contact="9876543322",customer_email="naufal@gmail.com",customer_address="Chennai"),
                    Customer(customer_name="Madhu",customer_contact="9856543212",customer_email="madhu@gmail.com",customer_address="Mumbai")
                ])
                session.commit()
 
           
            if not session.query(Item).first():
                session.add_all([
                    Item(item_name="Coffee",item_price=100,stock_availability=100),
                    Item(item_name="Icecream",item_price=250,stock_availability=75),
                    Item(item_name="Tea",item_price=50,stock_availability=200),
                    Item(item_name="Chocolate",item_price=120,stock_availability=200),
                    Item(item_name="Cappuccino",item_price=100,stock_availability=50),
                ])
           
                session.commit()
 
 
            if not session.query(Order).first():
                session.add_all([
                    Order(customer_id=1,order_status="Pending"),
                    Order(customer_id=2,order_status="Ordered"),
                    Order(customer_id=3,order_status="Pending"),
                    Order(customer_id=4,order_status="Ordered"),
                    Order(customer_id=5,order_status="Pending"),
                ])
           
                session.commit()
 
            if not session.query(OrderItemMapping).first():
                session.add_all([
                    OrderItemMapping(order_id=1,item_id=2,quantity=4),
                    OrderItemMapping(order_id=2,item_id=3,quantity=5),
                    OrderItemMapping(order_id=3,item_id=1,quantity=3),
                    OrderItemMapping(order_id=4,item_id=5,quantity=10),
                    OrderItemMapping(order_id=5,item_id=4,quantity=2),
                ])
           
                session.commit()
            print("✓ Database seeded successfully")
           
        except Exception as e:
            session.rollback()
            print(f"✗ Error seeding database: {str(e)}")
            raise e
        finally:
            session.close()
 
    def run_startup_seeding(self):
        self.seed_data()
 
if __name__ == "__main__":
    seeder = Seeder()
    seeder.seed_data()
 