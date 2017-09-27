# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 12:37:30 2016

@author: abhishekr
"""
def reg():
    import pandas
    month=int(input("enter number of months:"))
    inter=int(input("enter intercept:"))
    slope=int(input("enter slope:"))
    price=month*slope+inter
    price=float(price)
    print('the value of house is',' ',price,' ','dollars only')


reg()


