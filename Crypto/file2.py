#!/usr/bin/env python3
# -*- coding: latin-1 -*-
blob = """
    '?E ?>?"?????T?ސG?p(z$nwzG?6?p??pI??;??ϻK?5v???E-jvgX??8`?T6???q?-Ɲ?8?ڂ?,?%?LY9?5/?p???????<B???	˖ɓX??t??L?
"""
from hashlib import sha256
print(sha256(blob.encode()).hexdigest())
