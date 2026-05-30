from datetime import datetime
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)

from app.core.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    phone_number = Column(String(20), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    user_role = Column(String(20), default="customer")
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)


class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, autoincrement=True)
    category_name = Column(String(50), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    brand = Column(String(100), nullable=False)
    style = Column(String(50), nullable=False)
    description = Column(String(300))
    category_id = Column(
        Integer,
        ForeignKey("categories.id"),
        nullable=False,
    )
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)


class ProductVariant(Base):
    __tablename__ = "product_variants"
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(
        Integer,
        ForeignKey("products.id"),
        nullable=False,
    )
    size = Column(String(10), nullable=False)
    color = Column(String(20), nullable=False)
    price = Column(Integer, nullable=False)
    stock = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)


class Cart(Base):
    __tablename__ = "carts"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
    )
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)


class CartItem(Base):
    __tablename__ = "cart_items"
    id = Column(Integer, primary_key=True, autoincrement=True)
    cart_id = Column(
        Integer,
        ForeignKey("carts.id"),
        nullable=False,
    )
    product_variant_id = Column(
        Integer,
        ForeignKey("product_variants.id"),
        nullable=False,
    )
    quantity = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)


class Address(Base):
    __tablename__ = "addresses"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
    )
    full_name = Column(String(100), nullable=False)
    phone_number = Column(String(20), nullable=False)
    street = Column(String(255), nullable=False)
    city = Column(String(50), nullable=False)
    state = Column(String(50), nullable=False)
    postal_code = Column(String(20), nullable=False)
    country = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)


class Coupon(Base):
    __tablename__ = "coupons"
    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(20), unique=True, nullable=False)
    amount = Column(Integer, nullable=False)
    minimum_amount = Column(Integer, nullable=False)
    is_active = Column(Boolean, default=True)
    expiry = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)


class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
    )
    address_id = Column(
        Integer,
        ForeignKey("addresses.id"),
        nullable=False,
    )
    coupon_id = Column(
        Integer,
        ForeignKey("coupons.id"),
        nullable=True,
    )
    total_amount = Column(Integer, nullable=False)
    status = Column(String(30), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)


class OrderItem(Base):
    __tablename__ = "order_items"
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(
        Integer,
        ForeignKey("orders.id"),
        nullable=False,
    )
    product_variant_id = Column(
        Integer,
        ForeignKey("product_variants.id"),
        nullable=False,
    )
    product_name = Column(String(100), nullable=False)
    size = Column(String(10), nullable=False)
    color = Column(String(20), nullable=False)
    price_at_purchase = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)


class Payment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
    )
    order_id = Column(
        Integer,
        ForeignKey("orders.id"),
        nullable=False,
    )
    payment_type = Column(String(30), nullable=False)
    transaction_id = Column(
        String(100),
        unique=True,
        nullable=False,
    )
    amount = Column(Integer, nullable=False)
    status = Column(String(30), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)


class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
    )
    product_id = Column(
        Integer,
        ForeignKey("products.id"),
        nullable=False,
    )
    order_id = Column(
        Integer,
        ForeignKey("orders.id"),
        nullable=False,
    )
    rating = Column(Integer, nullable=False)
    comment = Column(String(400))
    created_at = Column(DateTime, default=datetime.utcnow)
