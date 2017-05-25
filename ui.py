#!/usr/bin/env python
from tkinter import *
from sys import *
from functions import submit_b

root = Tk()
def DLA_UI():
    #Law Firm=================================================
    case_number = Label(root)

    #Party Names ==============================================
    grantor_label = Label(root, text="Grantor")
    grantor_entry = Entry(root)

    grantee_label = Label(root, text="Grantee")
    grantee_entry = Entry(root)

    #Party Addresses =========================================
    grantor_address_label = Label(root, text="Grantor Street")
    grantor_address2_label = Label(root, text="Grantor City, State Zip")
    grantor_address_entry = Entry(root)
    grantor_address2_entry = Entry(root)

    grantee_address_label = Label(root, text="Grantee Street")
    grantee_address2_label = Label(root, text="Grantee City, State Zip")
    grantee_address_entry = Entry(root)
    grantee_address2_entry = Entry(root)

    # Property info ==========================================
    property_label = Label(root, text="Property Description", anchor=E)
    property_entry = Text(root)

    TMS_label = Label(root, text="Property TMS#")
    TMS_entry = Entry(root)

    purchase_label = Label(root, text="Property Description")
    purchase_entry = Entry(root)

    #Grid ==================================================
    #Grantor Info Input===================
    grantor_label.grid(row=0, sticky=E)
    grantor_entry.grid(row=0, column=1)
    grantor_address_label.grid(row=1, sticky=E)
    grantor_address_entry.grid(row=1, column =1)
    grantor_address2_label.grid(row=2, sticky=E)
    grantor_address2_entry.grid(row=2, column =1)

    #Grantee Info Input=================
    grantee_label.grid(row=0, column=2, sticky=E)
    grantee_entry.grid(row=0, column=3)
    grantee_address_label.grid (row=1, column=2, sticky=E)
    grantee_address_entry.grid(row=1, column =3)
    grantee_address2_label.grid (row=2, column=2, sticky=E)
    grantee_address2_entry.grid(row=2, column =3)

    #Property Info=================

    #Submit Button============================================
    submit_button = Button(root, text="Submit", command = submit_b)
    submit_button.grid(row=5, columnspan=2)
DLA_UI()
root.mainloop()
