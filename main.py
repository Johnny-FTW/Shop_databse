from db import engine, metadata
from db_utils import create_tables
from requests import RegisterRequest
from requests.LoginRequest import LoginRequest
from requests.ProductADD import Product
from requests.RegisterOrder import Order, OrderItem
from requests.RegisterRequest import Customer
from services.AuthService import login_service
from services.CustomerService import create_customer_service
from services.OrderService import create_order_service, create_order_service_detail, show_order, show_total_price
from services.ProductService import create_product_service

create_tables(engine,metadata)


def create_customer(data: RegisterRequest):
    try:
        customer_id = create_customer_service(data)
        return customer_id
    except Exception as e:
        print(e)


def login(data: LoginRequest):
    try:
        login_service(data)
    except Exception as e:
        print(e)


def create_order(data: Order):
    try:
        order_id = create_order_service(data)
        return order_id
    except Exception as e:
        print(e)




new_customer = Customer(first_name="Jan",last_name = "Hatapka", email="jan.hatapka@gmail.com",password="123456",address="Ul.29.augusta28/c",postcode="81109",country = "Slovakia")

customer_id = create_customer(new_customer)

login_data = LoginRequest(email="jan.hatapka@gmail.com", password="123456")

login(login_data)


# new_customer2 = Customer(first_name="Peter",last_name = "Hrinko", email="jan.hatapka@gmail.com",password="123456",address="Ul.29.augusta28/c",postcode="81109",country = "Slovakia")
#
# create_customer_service(new_customer)
# create_customer_service(new_customer2)
#
# new_product = Product("Bread",50)
# new_product2 = Product("Butter",100)
# new_product3 = Product("Socks",150)
#
# create_product_service(new_product)
# create_product_service(new_product2)
# create_product_service(new_product3)
#
# new_order = Order(1)
# order_id = create_order(new_order)
#
# new_order_detail = OrderItem(order_id=order_id,quantity=1,product_id=1)
# new_order_detail2 = OrderItem(order_id=order_id,quantity=2,product_id=3)
#
# create_order_service_detail(new_order_detail)
# create_order_service_detail(new_order_detail2)
#
# new_order2 =Order(2)
# order_id2 = create_order(new_order2)
#
# new_order_detail3 = OrderItem(order_id=order_id2,quantity=3,product_id=1)
# new_order_detail4 = OrderItem(order_id=order_id2,quantity=4,product_id=2)
#
# create_order_service_detail(new_order_detail3)
# create_order_service_detail(new_order_detail4)
#
# print(show_order(2))
# print(show_total_price(2))



