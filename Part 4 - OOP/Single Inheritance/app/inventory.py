from utils.validators import integer_check

class Resource:
        
    def __init__(self, name: str, manufacturer: str, total: int, allocated: int):
        self._name = name
        self._manufacturer = manufacturer
        self._total = integer_check("Total",total, min_value=0)
        self._allocated = integer_check("Allocated", allocated, min_value=0, max_value = total)
        
    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return f'Resource model: {self.name}, Manufacturer: {self.manufacturer}, \n In stock: {self.total}'
    
    @property
    def name(self):
        '''
        Returns str: resource name
        '''
        return self._name
    
    @property
    def manufacturer(self):
        '''
        Returns str: resource manufacturer
        '''
        return self._manufacturer
    
    @property
    def total(self):
        return self._total
    
    @property
    def allocated(self):
        return self._allocated
    
    @property
    def category(self):
        return type(self).__name__.lower()

    def claim(self, n):
        '''
        method to take n resources from the pool (as long as inventory is available)
        '''
        _n = integer_check("Num of resources", n, min_value=1)
        if self.allocated+_n < self.total:
            self._allocated += _n
            return f"{_n} units of {self.name} has been successfully claimed"
        else:
            raise ValueError("Not enough inventory")

    def freeup(self, n):
        '''
        method to return n resources to the pool
        '''
        _n = integer_check("Num of resources", n, min_value=1)
        if self.allocated-_n >= 0:
            self._allocated -= _n
            return f"{_n} units of {self.name} has been successfully returned"
        else:
            raise ValueError("Can't return more than allocated")

    def died(self, n):
        '''
        method to return and permanently remove inventory from the pool
        '''
        _n = integer_check("Num of resources",n, min_value=1)
        if self.allocated-_n >= 0 and self.total-_n > 0:
            self._allocated -= _n
            self._total -= _n
            return f"{_n} units of {self.name} has been successfully removed from the db"
        else:
            raise ValueError("Can't remove  more than allocated or in total inventory")
        
    def purchased(self, n):
        '''
        method to add inventory to the pool
        '''
        if integer_check("Num of resources",n):
            self._total+=n
        else:
            raise ValueError("You can't purchase a negative amount")
        
class CPU(Resource):
    def __init__(self, name, manufacturer, total: int, allocated: int, cores: int, socket: str, power_watts:int):
        super().__init__(name, manufacturer, total, allocated)
        self.cores = integer_check("Num of cores",cores, min_value=1)
        self.socket = socket
        self.power_watts = integer_check("Power Watts",power_watts, min_value=1)

class Storage(Resource):
    def __init__(self, name, manufacturer, total: int, allocated: int, capacity_GB: int):
        super().__init__(name, manufacturer, total, allocated)
        self.capacity_GB = integer_check("Capacity",capacity_GB, min_value=1)

class HDD(Storage):
    def __init__(self, name, manufacturer, total: int, allocated: int, capacity_GB: int, size: str, rpm: int):
        super().__init__(name, manufacturer, total, allocated, capacity_GB)
        self.size = size
        self.rpm = integer_check("RPM",rpm, 5000, 10000)

class SSD(Storage):
    def __init__(self, name, manufacturer, total: int, allocated: int, capacity_GB: int, interface: str):
        super().__init__(name, manufacturer, total, allocated, capacity_GB)
        self.interface = interface