
from django.http import HttpResponse
from django.utils import timezone
a = 11
b = 22
c = a + b
print("c",c)

def test(a,b,c):
	return c >= a - b

print("Test():",test(6,2,3))

import datetime
print(datetime.timedelta(days=1))
