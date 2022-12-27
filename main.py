from db import engine, metadata
from db_utils import create_tables
from requests.ProductADD import Product
from requests.RegisterOrder import Order, OrderDetail
from requests.RegisterRequest import Customer
from services.CustomerService import create_customer_service
from services.OrderService import create_order_service, create_order_service_detail, show_order, show_total_price
from services.ProductService import create_product_service


def create_order(data: Order):
    try:
        order_id = create_order_service(data)
        return order_id
    except Exception as e:
        print(e)


create_tables(engine,metadata)

new_customer = Customer(first_name="Jan",last_name = "Hatapka",country = "Slovakia")
new_customer2 = Customer(first_name="Peter",last_name = "Hrinko",country = "Hungary")

create_customer_service(new_customer)
create_customer_service(new_customer2)

new_product = Product("Bread",50)
new_product2 = Product("Butter",100)
new_product3 = Product("Socks",150)

create_product_service(new_product)
create_product_service(new_product2)
create_product_service(new_product3)

new_order = Order(1)
order_id = create_order(new_order)

new_order_detail = OrderDetail(order_id=order_id,quantity=1,product_id=1)
new_order_detail2 = OrderDetail(order_id=order_id,quantity=2,product_id=3)

create_order_service_detail(new_order_detail)
create_order_service_detail(new_order_detail2)

new_order2 =Order(2)
order_id2 = create_order(new_order2)

new_order_detail3 = OrderDetail(order_id=order_id2,quantity=3,product_id=1)
new_order_detail4 = OrderDetail(order_id=order_id2,quantity=4,product_id=2)

create_order_service_detail(new_order_detail3)
create_order_service_detail(new_order_detail4)

show_order(2)
show_total_price(2)



