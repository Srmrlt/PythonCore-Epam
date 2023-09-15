from task import Euro
from task import Dollar
from task import Pound


print(
      f"Euro.course(Pound)   ==> {Euro.course(Pound)}\n"
      f"Dollar.course(Pound) ==> {Dollar.course(Pound)}\n"
      f"Pound.course(Euro)   ==> {Pound.course(Euro)}\n"
  )
print('-----------------------------------------------')

e = Euro(100)
r = Pound(100)
d = Dollar(200)

print(
      f"e = {e}\n"
      f"e.to_currency(Dollar) = {e.to_currency(Dollar)}\n"
      f"e.to_currency(Pound) = {e.to_currency(Pound)}\n"
      f"e.to_currency(Euro)   = {e.to_currency(Euro)}\n"
  )
print('-----------------------------------------------')
print(
      f"r = {r}\n"
      f"r.to_currency(Dollar) = {r.to_currency(Dollar)}\n"
      f"r.to_currency(Euro)   = {r.to_currency(Euro)}\n"
      f"r.to_currency(Pound) = {r.to_currency(Pound)}\n"
  )
print('-----------------------------------------------')
print(
      f"e + r  =>  {e + r}\n"
      f"r + d  =>  {r + d}\n"
      f"d + e  =>  {d + e}\n"
  )
print('-----------------------------------------------')
print(
      f"e > r  =>  {e > r}\n"
      f"r > d  =>  {r > d}\n"
      f"d > e  =>  {d > e}\n"
  )
print('-----------------------------------------------')
print(
      f"e < r  =>  {e < r}\n"
      f"r < d  =>  {r < d}\n"
      f"d < e  =>  {d < e}\n"
  )
print('-----------------------------------------------')
print(
      f"e == r  =>  {e == r}\n"
      f"r == d  =>  {r == d}\n"
      f"d == e  =>  {d == e}\n"
  )
