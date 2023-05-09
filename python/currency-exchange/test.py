budget = 1500
exchange_rate = 0.84
spread = 25
denomination = 40

aer = exchange_rate + (spread/100) #ok
print (aer)
pass1 = budget // aer #ok
print(pass1)
bills = pass1 // denomination
print(bills)
max = int(bills * denomination)
print (max)