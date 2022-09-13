kurs_btc = float(input("What is Bitcoin price today?  "))
money = float(input("How much $ do you have?  "))

res = money / kurs_btc
res_str ='You can buy ' + str(format(res, '.7f')) + ' BTC'
print(res_str)

