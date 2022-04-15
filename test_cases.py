#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import product_import_helper


def test_deleted_filter():
    #Deleted Items Test Case - the first item is marked as deleted, the second item is not
    products=[{'deleted': True,
      'price': '$10.00',
      'brand_name': 'Acme',
      'id': 2000,
      'hidden': False,
      'product_name': 'Anvil'},
     {'deleted': False,
      'price': '$123.45',
      'brand_name': 'Acme',
      'id': 2001,
      'hidden': False,
      'product_name': 'Giant Anvil'}]
    
    non_deleted_products=product_import_helper.remove_deleted(products)
    
    correct_non_deleted=[{'deleted': False, #only the second item that is not marked as deleted should remain
      'price': '$123.45',
      'brand_name': 'Acme',
      'id': 2001,
      'hidden': False,
      'product_name': 'Giant Anvil'}]    
    
    assert non_deleted_products == correct_non_deleted


def test_hidden_filter():
    #Hidden items test case
    products=[{'deleted': False,  #the first item is marked as hidden, the second item is not
      'price': '$10.00',
      'brand_name': 'Acme',
      'id': 2000,
      'hidden': True,
      'product_name': 'Anvil'},
     {'deleted': False,
      'price': '$123.45',
      'brand_name': 'Acme',
      'id': 2001,
      'hidden': False,
      'product_name': 'Giant Anvil'}]
    
    non_hidden_products=product_import_helper.remove_hidden(products)
    
    correct_non_hidden=[{'deleted': False, #only the second item that is not marked as hidden should remain
      'price': '$123.45',
      'brand_name': 'Acme',
      'id': 2001,
      'hidden': False,
      'product_name': 'Giant Anvil'}]    
    
    assert non_hidden_products == correct_non_hidden


def test_sorting():
    #Sorting by lowest to highest price and if two items have the same price, by name test case
    products=[{'deleted': False, #the pre-sorted products are not in order of price or name
      'price': '$123.45',
      'brand_name': 'Acme',
      'id': 2001,
      'hidden': False,
      'product_name': 'Giant Anvil'},
     {'deleted': True,
      'price': '$10.00',
      'brand_name': 'Acme',
      'id': 2003,
      'hidden': True,
      'product_name': 'B'},
      {'deleted': False,
       'price': '$10.00',
       'brand_name': 'Acme',
       'id': 2000,
       'hidden': False,
       'product_name': 'A'}]
    
    sorted_products=product_import_helper.sort_by_price_name(products)
    
    correct_sorted=[{'deleted': False, #the sorted items - two $10 itesms first, $123.45 after
       'price': '$10.00',              
       'brand_name': 'Acme',
       'id': 2000,
       'hidden': False,
       'product_name': 'A'}, #the A product comes before B product when they are priced the same
      {'deleted': True,
       'price': '$10.00',
       'brand_name': 'Acme',
       'id': 2003,
       'hidden': True,
       'product_name': 'B'},
      {'deleted': False,
       'price': '$123.45',  #The Giant Anvil is last because it has the highest price
       'brand_name': 'Acme',
       'id': 2001,
       'hidden': False,
       'product_name': 'Giant Anvil'}] 
    
    assert sorted_products == correct_sorted


def test_non_duplicate():
    #Deleting Duplicates Test Case - the last two items are duplicates
    products=[{'deleted': False,
      'price': '$10.00',
      'brand_name': 'Acme',
      'id': 2000,
      'hidden': False,
      'product_name': 'Anvil'},
     {'deleted': True,
      'price': '$10.00',
      'brand_name': 'Acme',
      'id': 2003,
      'hidden': True,
      'product_name': 'Anvil - Two Pack'},
     {'deleted': True,
      'price': '$10.00',
      'brand_name': 'Acme',
      'id': 2003,
      'hidden': True,
      'product_name': 'Anvil - Two Pack'}]
    
    non_duplicate_products=product_import_helper.delete_duplicates(products)
    
    correct_non_duplicate=[{'deleted': False, #only one of the last two items remains
      'price': '$10.00',
      'brand_name': 'Acme',
      'id': 2000,
      'hidden': False,
      'product_name': 'Anvil'},
     {'deleted': True,
      'price': '$10.00',
      'brand_name': 'Acme',
      'id': 2003,
      'hidden': True,
      'product_name': 'Anvil - Two Pack'}]    
    
    assert non_duplicate_products == correct_non_duplicate
