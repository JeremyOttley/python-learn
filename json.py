#!/usr/bin/env python

import json

with open("pizza_order.json") as file:
  data = json.load(file)
  fname = data['first_name']
  lname = data['last_name']
  email = data['email_address']
  phone = data['phone_number']
  address = data['my_address']
  print(fname + " " + lname + " " "just called from " + phone + ". We'll send them a confirmation to " + email + ". Please deliver this pizza to " + address)
