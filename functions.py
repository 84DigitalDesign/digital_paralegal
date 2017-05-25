from __future__ import print_function
from tkinter import *
from mailmerge import MailMerge
from datetime import date
import sys

#having trouble getting the submit button to work correctly.
#The tkinter should alow me to get() the information from 

def submit_b ():
    py_buyer = sys.grantor_entry.get()
    py_seller = grantee_entry.get()
    py_buyer_address1 = grantor_address_entry.get()
    py_buyer_address2 = grantor_address2_entry.get()
    py_seller_address1 = grantee_address_entry.get()
    py_seller_address2 = grantee_address2_entry.get()
    py_seller_property = property_entry.get()
    TMS_entry.get()
    purchase_entry.get()

    
#this one works, I just need to be able to get the information from the UI once entered.

def create_firpta():
    template = "Draft Templates\FIRPTA template1.docx"

    document = MailMerge(template)
    print(document.get_merge_fields())

    document.merge(
        seller= sys.py_seller,
        seller_property= sys.py_seller_property,
        tms= sys.py_tms,
        seller_ssn= sys.py_seller_ssn,
        seller_address1= sys.py_seller_address1,
        seller_address2= sys.py_seller_address2,
        month = '{:%B}'.format(date.today()),
        year = '{:%Y}'.format(date.today()),
    )

    document.write('test-output.docx')

    print("Created FIRPTA.")
