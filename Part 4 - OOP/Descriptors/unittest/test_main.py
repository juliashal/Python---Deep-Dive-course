'''
Tests for Resource class
'''

import pytest
import sys
sys.path.append('C:/Projects/Python - Deep Dive course/Part 4 - OOP/Descriptors')

import main

'''
class Person:
    name = CharField(1, 50)
    age = IntegerField(0, 200)
'''

@pytest.mark.parametrize('age_value',[-15, 325])
def test_create_invalid_age(age_value):
    '''
    testing 2 different values for age attribute
    '''
    p = main.Person()
    with pytest.raises(ValueError):
        p.age = age_value

@pytest.mark.parametrize('name_value',['','sdhjbsfjsfjdsbfjsdfjdsjfsdjfhgsjkdfnshjgsfhgjkdfdsfgfhgtrhbvcbcvfdssdfsefasnfkgndfkgnrtg'])
def test_create_invalid_age(name_value):
    '''
    testing 2 different values for name attribute
    '''
    p = main.Person()
    with pytest.raises(ValueError):
        p.name = name_value