# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1O9UujWTma21lweK74PYowp-m56J7CfG9
"""

with open('/content/output_version27.txt', 'r') as f_in, open('/content/output.txt', 'w') as f_out:
    for line in f_in:
        new_line = '2.0.27' + line
        f_out.write(new_line)