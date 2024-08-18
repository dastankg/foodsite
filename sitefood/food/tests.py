from django.test import TestCase
from django.core.paginator import Paginator
# Create your tests here.


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pages = Paginator(lst, 2)
p = None
p1 = None
p3 = None

try:
    p3 = pages.page(1)
    p2 = pages.page(2)
    p = pages.page(3)
    p1 = pages.page(4)
    print(p.previous_page_number(), p2.next_page_number(), p.next_page_number())
except:
    print('NO')