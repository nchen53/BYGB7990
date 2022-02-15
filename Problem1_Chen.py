#!/usr/bin/env python
# coding: utf-8

# # 4.You are asked to develop a Python program that calculates tip and total bill for a restaurant. Upon running the program, it asks the user:
# How much is your original bill?
# What percentage is your tip?
# The program takes the original bill amount as an input to calculate tip and total bill. Tip is based on the desired percentage of the original bill. It outputs
# 
# Your tip based on __% is   ______ (fill in tip % and tip amount here)
# Your total bill is ___________ (fill in total bill here)

# This program is about calculate the tip and total bill for a restaurant.

# In[2]:


#ask to input the original bill.
bill=float(input('How much is your original bill: '))

#ask to input the tip in percentage %
tip=float(input('What percentage is your tip(in %): '))

#calculate the tip amount and store.
tip_amount=bill*tip*0.01

#calculate the total bill.
total=bill+tip_amount

#out put:
print('Your tip based on',tip,' % is ',tip_amount)
print('Your total bill is ',total)


# In[ ]:




