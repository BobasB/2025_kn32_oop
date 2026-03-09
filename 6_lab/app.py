import os
import math

a = os.getenv('USER')
b = os.getenv('ENVIRONMENT')
c = os.getenv('ENV_USER')
print(f"Привіт, {c}! Ви працюєте в середовищі {b} під профайлом {a}.")