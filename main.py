#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json
import product_import_helper

#load data from website
url=requests.get("https://www.beautylish.com/rest/interview-product/list")
text = url.text
data=json.loads(text)
products=data['products']

#filter out deleted products
non_deleted_products=product_import_helper.remove_deleted(products)

#filter out hidden products
non_hidden_products=product_import_helper.remove_hidden(non_deleted_products)

#Sort by name and by price secondarily
sorted_products=product_import_helper.sort_by_price_name(non_hidden_products)

#remove any duplicate products
non_duplicate_products=product_import_helper.delete_duplicates(sorted_products)


#Display Product List
print ("{:<30} {:<30} {:<10} \n".format('Brand Name','Product Name','Price')) # print the header

for product in non_duplicate_products:
    print("{:<30} {:<30} {:<10}".format(product['brand_name'],product['product_name'],product['price'])) #print each row


#Calculate Summary Statistics
total_unique_prod=len(non_duplicate_products)

total_unique_brands=len(product_import_helper.get_unique_brands(non_duplicate_products))

avg_price=sum(product_import_helper.get_prices(non_duplicate_products))/len(non_duplicate_products)


#Display summary statistics
print('\n')
print('Total Unique Products : ', str(total_unique_prod))
print('  Total Unique Brands : ', str(total_unique_brands))
print('        Average Price : ', str(avg_price))