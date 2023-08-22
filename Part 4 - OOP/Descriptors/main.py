'''
Integer and String descriptors
'''

class IntegerField:
    '''
    Descriptor to check if input:
    -type integral
    -between minimum and maximum value
    '''
    def __init__(self, min = None, max = None) -> None:
        self.min = min
        self.max = max

    def __set_name__(self, owner_class, property_name):
        self.property_name = property_name
    
    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.property_name, None)
        
    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError(f'{self.property_name} must be an integer.')
        if value is not None and value < self.min:
            raise ValueError(f'{self.property_name} must be greater than {self.min}.')
        if value is not None and value > self.max:
            raise ValueError(f'{self.property_name} must be less than {self.max}.')
        
        instance.__dict__[self.property_name] = value

class CharField:
    '''
    Descriptor to check if input:
    -is of type string
    -between minimum and maximum length
    '''
    def __init__(self, min_length = None, max_length = None) -> None:
        self.min_length = min_length
        self.max_length = max_length

    def __set_name__(self, owner_class, property_name):
        self.property_name = property_name
    
    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.property_name, None)
        
    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f'{self.property_name} must be an integer.')
        if value is not None and len(value) < self.min_length:
            raise ValueError(f'{self.property_name} length must be greater than {self.min_length}.')
        if value is not None and len(value) > self.max_length:
            raise ValueError(f'{self.property_name} length must be less than {self.max_length}.')
        
        instance.__dict__[self.property_name] = value

class Person:
    name = CharField(1, 50)
    age = IntegerField(0, 200)

p = Person()
