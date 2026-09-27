class OrderManagementSystem:
    def __init__(self):
        self.order_dic = {} # order_id: (price, type)
        self.orders_with_price = defaultdict(set) # (price, type): [order_id's]

    def addOrder(self, orderId: int, orderType: str, price: int) -> None:
        self.order_dic[orderId] = (price, orderType)
        self.orders_with_price[(price, orderType)].add(orderId)

    def modifyOrder(self, orderId: int, newPrice: int) -> None:
        price, _type = self.order_dic[orderId]
        self.order_dic[orderId] = (newPrice, _type)
        self.orders_with_price[(price, _type)].remove(orderId)
        self.orders_with_price[(newPrice, _type)].add(orderId)

    def cancelOrder(self, orderId: int) -> None:
        price, _type = self.order_dic[orderId]
        del self.order_dic[orderId]
        self.orders_with_price[(price, _type)].remove(orderId)

    def getOrdersAtPrice(self, orderType: str, price: int) -> List[int]:
        return list(self.orders_with_price[(price, orderType)])


# Your OrderManagementSystem object will be instantiated and called as such:
# obj = OrderManagementSystem()
# obj.addOrder(orderId,orderType,price)
# obj.modifyOrder(orderId,newPrice)
# obj.cancelOrder(orderId)
# param_4 = obj.getOrdersAtPrice(orderType,price)