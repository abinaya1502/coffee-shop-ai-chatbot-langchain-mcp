from sqlalchemy import Boolean, CheckConstraint, Column, DateTime, ForeignKey, Integer, Numeric, String, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid
 
 
Base = declarative_base()
 
class Customer(Base):
    __tablename__ = "customers"
    customer_id = Column(Integer, primary_key=True, index=True)
    customer_uuid = Column(UUID(as_uuid = True),default = uuid.uuid4)
    customer_name = Column(String(100),nullable=False)
    customer_contact = Column(String(50),nullable=False,unique=True)
    customer_email = Column(String(50),unique=True,nullable=False)
    customer_address = Column(String(255),nullable = False)
    is_active = Column(Boolean, default=True)
    created_by = Column(String(50), default="ADMIN",nullable = False)
    created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    updated_by = Column(String(50), default="ADMIN")
    updated_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
 
   
class Item(Base):
    __tablename__ = "items"
    item_id = Column(Integer, primary_key=True, index=True)
    item_uuid = Column(UUID(as_uuid = True),default = uuid.uuid4)
    item_name = Column(String(100), unique=True, nullable=False)
    item_price = Column(Numeric(10,2),nullable = False)
    stock_availability  = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=True)
    created_by = Column(String(50), default="ADMIN",nullable = False)
    created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    updated_by = Column(String(50), default="ADMIN")
    updated_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
 
 
   
class Order(Base):
    __tablename__ = "orders"
    order_id = Column(Integer, primary_key=True, index=True)
    order_uuid = Column(UUID(as_uuid = True),default = uuid.uuid4)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"), nullable=False)
    order_status = Column(String(100),CheckConstraint("order_status IN ('Pending','Ordered')"), default="Pending")
    is_active = Column(Boolean, default=True)
    created_by = Column(String(50), default="ADMIN",nullable = False)
    created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    updated_by = Column(String(50), default="ADMIN")
    updated_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
 
 
 
 
 
 
   
class OrderItemMapping(Base):
    __tablename__ = "order_item_mapping"
    order_item_mapping_id = Column(Integer, primary_key=True, index=True)
    order_item_mapping_uuid = Column(UUID(as_uuid = True),default = uuid.uuid4)
    order_id = Column(Integer, ForeignKey("orders.order_id"), nullable=False)
    item_id = Column(Integer, ForeignKey("items.item_id"), nullable=False)
    quantity = Column(Integer,default=1)
    is_active = Column(Boolean, default=True)
    created_by = Column(String(50), default="ADMIN",nullable = False)
    created_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
    updated_by = Column(String(50), default="ADMIN")
    updated_at = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))
 
   
 
 
 