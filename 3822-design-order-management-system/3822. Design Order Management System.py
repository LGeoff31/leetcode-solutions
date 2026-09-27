class OrderManagementSystem:
    def __init__(self):
        self.buy_active_orders = {} # order_id: price
        self.sell_active_orders = {} # order_id: price

        
    def addOrder(self, orderId: int, orderType: str, price: int) -> None:
        if orderType=="buy":
            self.buy_active_orders[orderId] = price
        else:
            self.sell_active_orders[orderId] = price

    def modifyOrder(self, orderId: int, newPrice: int) -> None:
        if orderId in self.buy_active_orders:
            self.buy_active_orders[orderId] = newPrice
        else:
            self.sell_active_orders[orderId] = newPrice

    def cancelOrder(self, orderId: int) -> None:
        if orderId in self.buy_active_orders:
            del self.buy_active_orders[orderId]
        else:
            del self.sell_active_orders[orderId]

    def getOrdersAtPrice(self, orderType: str, price: int) -> List[int]:
        res = []
        if orderType == "buy":
            for order_id, p in self.buy_active_orders.items():
                if p == price:
                    res.append(order_id)
        else:
            for order_id, p in self.sell_active_orders.items():
                if p == price:
                    res.append(order_id)
        return res


# Your OrderManagementSystem object will be instantiated and called as such:
# obj = OrderManagementSystem()
# obj.addOrder(orderId,orderType,price)
# obj.modifyOrder(orderId,newPrice)
# obj.cancelOrder(orderId)
# param_4 = obj.getOrdersAtPrice(orderType,price)