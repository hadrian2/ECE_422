#!/usr/bin/env python3
# -*- coding: latin-1 -*-
blob = """
    ��ƃ��^G(�?'�w�E_m������x2
.���"��˽�Y�-)���%N}�z�4_8���P�[�v��d;[X�G��o��K_��A���ir��w\�oY�1N%�!��H�|��bA�(�vs
"""
from hashlib import sha256
if "6c26d72" in sha256(blob.encode()).hexdigest():
  print("I come in peace.")
else:
  print("Prepare to be destroyed!")
