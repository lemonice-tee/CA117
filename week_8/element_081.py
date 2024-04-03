#!/usr/bin/env python3

import sys

class Element(object):

  def set_attributes(element_object, number, name, symbol, bp):
    element_object.number = number
    element_object.name = name
    element_object.symbol = symbol
    element_object.bp = bp

  def print_attributes(element_object):
    print(f'Number: {element_object.number}')
    print(f'Name: {element_object.name}')
    print(f'Symbol: {element_object.symbol}')
    print(f'Boiling point: {element_object.bp} K')
