#!/usr/bin/env python
# coding: utf-8

# ## CAESAR CIPHER

# In[5]:


alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction = input("Type 'encode' for Encryption and 'decode' for decryption: ")
text = input("Enter the text: ")
shift = int(input("Type the shift number: "))

def encryption(plain_text, shift_amount):
    result_str = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        position += shift_amount
        result_str += alphabet[position]
    return result_str

def decryption(caesar_text, shift_amount):
    result_str = ""
    for letter in caesar_text:
        position = alphabet.index(letter)
        position -= shift_amount
        result_str += alphabet[position]
    return result_str

if direction == "encode":
    result = encryption(text,shift)
    print(result)
else:
    result = decryption(text,shift)
    print(result)


# In[ ]:




