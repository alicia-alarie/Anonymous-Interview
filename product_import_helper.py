#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def remove_deleted(products):
    '''remove deleted elements from the products list
    input : products - list of dicts with product details
    output: non_deleted - list of dicts with products that are not deleted'''
    non_deleted=[]
    
    for product in products:
        if product['deleted'] == False:
            #non_deleted.append(product)
            non_deleted=[]
            
    return non_deleted


def remove_hidden(products):
    '''remove hidden elements from the products
    input : products - list of dicts with product details
    output: non_hidden - list of dicts with products that are not hidden'''
    non_hidden=[]
    
    for product in products:
        if product['hidden'] == False:
            non_hidden.append(product)
            
    return non_hidden


def sort_by_price_name(products):
    '''sort the products by price, and if two products have the same price,
    then by name
    input : products -list of dicts with product details
    output: newlist - list of dicts with sorted products'''
    newlist = sorted(products, key=lambda d: (float(d['price'][1:len(d['price'])]),d['product_name']))
    
    return newlist


def delete_duplicates(products):
    '''delete any duplicate products in the list
    input : products - list of dicts with product details
    output: unique _products - list of dicts with product details with no duplicates'''
    unique_products=[]
    
    for product in products:
        if product not in unique_products:
            unique_products.append(product)
    
    return unique_products


def get_unique_brands(products):
    '''returns a list of unique brands from the list of products
    input : products - list of dicts with product details'
    output: brands - list of str with brand names'''
    brands=[]
    
    for product in products:
        if product['brand_name'] not in brands:
            brands.append(product['brand_name'])
            
    return brands


def get_prices(products):
    '''returns a list of prices as floats for each item in the products list
    input : products - list of dicts with product details
    output: prices - list of prices as float'''
    prices=[]
    
    for product in products:
        prices.append(float(product['price'][1:len(product['price'])]))
    
    return prices



