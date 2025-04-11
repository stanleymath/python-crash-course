request_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in request_toppings:
    print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")

# caso n tenho algum igrediente

request_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in request_toppings:
    if requested_topping == 'green peppers':
        print("\nSorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}")

print("\nFinished making your pizza!")