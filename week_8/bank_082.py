#!/usr/bin/env python3

class BankAccount(object):

  def __init__(self, balance=0):
    self.balance = balance

  def deposit(self, money):
    self.balance = self.balance + money

  def withdraw(self, money):
    if int(self.balance) >= money:
      self.balance = self.balance - money

  def __str__(self):
   return f'Your current balance is {self.balance:.2f} euro'
