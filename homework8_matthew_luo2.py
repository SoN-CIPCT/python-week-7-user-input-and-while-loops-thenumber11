pizza_orders = []
finished_pizzas = []
prompt = '\nWhat type of pizza would you like?'
prompt += '\n[Enter "quit" when finished.]'

while True:
    order = input(prompt).lower()
    if order == "quit":
        break
    else:
        pizza_orders.append(order)
        print(f'\nYour {order} pizza pie is finished!')
        finished_pizzas.append(order)
    
i = 0
while i < len(finished_pizzas):
    pizza = finished_pizzas[i]
    print(f"The pizza {pizza} was made.")
    i += 1
