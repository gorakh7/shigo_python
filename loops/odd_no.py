# -*- coding: utf-8 -*-
# Author : Gorakhnath Suryawanshi
# print odd numbers 1 to 100

n = int(input("Enter the no::")) #0
n1 = int(input("Enter the no::")) #101
for x in range(n,n1):
    if (x%2!=0):
        print(x)