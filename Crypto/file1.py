#!/usr/bin/env python3
# -*- coding: latin-1 -*-
blob = """
    '�E �>�"�����T�ސ��p(z$nwzG�6�p��pI��;��;K�5v���E-jv�gX��8`�T6���q�-Ɲ���ڂ�,�%�LY9�5/�p��������B��	˖ɓX�����L�
"""
from hashlib import sha256
print(sha256(blob.encode()).hexdigest())
