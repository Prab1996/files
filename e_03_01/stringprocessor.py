x = "compressed natural gas burns at 689 degrees celcius"

bfind = x.find("burns")
print(bfind)

temp = x[bfind+1:]
print(temp)
