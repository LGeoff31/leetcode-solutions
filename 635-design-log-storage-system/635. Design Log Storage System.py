class LogSystem:

    def __init__(self):
        self.logs = []

    def put(self, id: int, timestamp: str) -> None: # O(1)
        self.logs.append((id, timestamp))
    
    def retrieve(self, start, end, gra):
        index = {'Year': 5, 'Month': 8, 'Day': 11, 
                 'Hour': 14, 'Minute': 17, 'Second': 20}[gra]
        s = start[:index]
        e = end[:index]
        return sorted(id for id, timestamp in self.logs if s <= timestamp[:index] <= e)
