# represent %5 as 0.05

money = 1000
apr = 0.05
for i in range(11):
  money += money * apr
  print(f"year {i}  is {round(money,2)}")

