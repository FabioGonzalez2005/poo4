values = [1, 4, 5, 6]

try:
    r = values[3]
except IndexError:
    print('Error: Index not in list')
except Exception:
    print("")
else:
    print(f'Your wishes are my command: {r}')
finally:
    print('Have a good day!')