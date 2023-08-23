import enum

class AppException(enum.Enum):
    def __new__(cls, code, message, exceptionType):
        member = object.__new__(cls)
        member._value_= code
        member.message = message
        member.exceptionType = exceptionType
        return member
    
    @property
    def code(self):
        return self.value 
    
    def throw(self):
        raise self.exceptionType(f'{self.code} - {self.message}')

    NotInteger = (100,'Value must be an Integer',ValueError)
    NotChar = (101,'Value must be a string',ValueError)

print(AppException['NotChar'])
print(AppException(101))
print(AppException.NotInteger.message)
print(AppException.NotInteger.throw())