'''
Integer and String descriptors
'''
import collections.abc

class BaseValidator:
    '''
    Descriptor to check if input:
    -is of specific type (Integer or String)
    -between minimum and maximum value/length
    '''
    def __init__(self, type_, min = None, max = None) -> None:
        self._type = type_
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
        if not isinstance(value, self._type):
            raise TypeError(f'{self.property_name} must be a type of {self._type.__name__}.')
        
        if value is not None:
            if isinstance(value, collections.abc.Sequence):
                if self.min is not None and len(value) < self.min:
                    raise ValueError(f'{self.property_name} length must be greater than {self.min}.')
                if self.max is not None and len(value) > self.max:
                    raise ValueError(f'{self.property_name} length must be less than {self.max}.')
            
            else:
                if self.min is not None and value < self.min:
                    raise ValueError(f'{self.property_name} must be greater than {self.min}.')
                if self.max is not None and value > self.max:
                    raise ValueError(f'{self.property_name} must be less than {self.max}.')
            
        instance.__dict__[self.property_name] = value

class IntegerField(BaseValidator):
    '''
    Descriptor to check if input is of type integral and between minimum and maximum value.

    Child of BaseVaildator.
    '''
    def __init__(self, min=None, max=None) -> None:
        super().__init__(int, min, max)

class CharField(BaseValidator):
    '''
    Descriptor to check if input is of type string and its length is between minimum and maximum value.

    Child of BaseVaildator.
    '''
    def __init__(self, min=None, max=None) -> None:
        super().__init__(str, min, max)


class Person:
    name = CharField(1, 50)
    age = IntegerField(0, 200)
