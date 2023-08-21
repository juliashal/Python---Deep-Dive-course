import pytest
import sys
sys.path.append('C:/Projects/Python - Deep Dive course/Part 4 - OOP/Single Inheritance/app/utils')

from validators import integer_check

class TestIntegerValidator:
    def test_valid(self):
        integer_check("arg", 10, 0, 20)
    
    def test_type_error(self):
        with pytest.raises(TypeError):
            integer_check("arg","kssts")
    
    def test_int_negative_error(self):
        with pytest.raises(ValueError):
            integer_check("arg",-1000)
    
    def test_int_minimum_error(self):
        with pytest.raises(ValueError):
            integer_check("arg",1,10,35)
    
    def test_int_maximum_error(self):
        with pytest.raises(ValueError):
            integer_check("arg",55,10,35)