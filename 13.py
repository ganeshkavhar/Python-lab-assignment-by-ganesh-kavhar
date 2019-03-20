Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math

print('{:^7}  {:^8}  {:^17}'.format('Mantissa', 'Exponent', 'Floating point value'))
print('{:-^8}  {:-^8}  {:-^20}'.format('', '', ''))

for m, e in [ (0.7, -3),
              (0.3,  0),
              (0.5,  3),
              ]:
    x = math.ldexp(m, e)
    print('{:7.2f}  {:7d}  {:7.2f}'.format(m, e, x))
