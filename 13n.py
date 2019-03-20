import math

print('{:^7}  {:^8}  {:^17}'.format('Mantissa', 'Exponent', 'Floating point value'))
print('{:-^8}  {:-^8}  {:-^20}'.format('', '', ''))

for m, e in [ (0.7, -3),
              (0.3,  0),
              (0.5,  3),
              ]:
    x = math.ldexp(m, e)
    print('{:7.2f}  {:7d}  {:7.2f}'.format(m, e, x))
