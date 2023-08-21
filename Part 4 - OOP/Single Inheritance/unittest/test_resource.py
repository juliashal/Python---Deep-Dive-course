'''
Tests for Resource class
'''

import pytest
import sys
sys.path.append('C:/Projects/Python - Deep Dive course/Part 4 - OOP/Single Inheritance/app')

import inventory

def test_create_resource():
    resource = inventory.Resource('Computer','Big one', 100,50)
    assert resource.name == 'Computer'
    assert resource.manufacturer == 'Big one'
    assert resource.total == 100
    assert resource.allocated == 50

def test_create_invalid_total_type():
    with pytest.raises(TypeError):
        inventory.Resource('Computer','Big one', 'a hundred',50)

def test_create_invalid_allocated_type():
    with pytest.raises(TypeError):
        inventory.Resource('Computer','Big one', 100,'fifty')

def test_create_invalid_total_value():
    with pytest.raises(ValueError):
        inventory.Resource('Computer','Big one', -10, 50)

@pytest.mark.parametrize('total,allocated',[(10, -5), (10,20)])
def test_create_invalid_allocated_value(total, allocated):
    with pytest.raises(ValueError):
        inventory.Resource('Computer','Big one', total, allocated)

@pytest.mark.parametrize('value',[-1, 0, 1000])
def test_create_invalid_claim_value(value):
    '''
    testing 3 different values for claims
    '''
    resource = inventory.Resource('Computer','Big one', 100,50)
    with pytest.raises(ValueError):
        resource.claim(value)

@pytest.mark.parametrize('value',[-1, 0, 1000])
def test_create_invalid_freeup_value(value):
    '''
    testing 3 different values for freeup method
    '''
    resource = inventory.Resource('Computer','Big one', 100,50)
    with pytest.raises(ValueError):
        resource.freeup(value)

@pytest.mark.parametrize('value',[-1, 0, 1000])
def test_create_invalid_died_value(value):
    '''
    testing 3 different values for died method
    '''
    resource = inventory.Resource('Computer','Big one', 100,50)
    with pytest.raises(ValueError):
        resource.died(value)
