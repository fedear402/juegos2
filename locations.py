def sells_to(i, j, num_locations):
    out = [0] * num_locations
    distances_i = [abs(n - i) for n in range(1, num_locations + 1)]
    distances_j = [abs(n - j) for n in range(1, num_locations + 1)]
    for lot in range(num_locations):
        if distances_i[lot] < distances_j[lot]:
            out[lot] = 1
        elif distances_i[lot] > distances_j[lot]:
            out[lot] = 2
        else:
            out[lot] = 0.5
    return out

def utility(i, j, price, num_locations):
    buyers = sells_to(i, j, num_locations)
    u_1 = buyers.count(1) * price + buyers.count(0.5) * price / 2
    u_2 = buyers.count(2) * price + buyers.count(0.5) * price / 2
    return (u_1, u_2)

def u(x, y, price, num_locations):
    dist = price * (1 / 2) * (abs(x - y) + 1)
    if x < y:
        return dist + (x - 1) * price
    elif x > y:
        return dist + (num_locations - x) * price
    elif x == y:
        return price * num_locations / 2

# Parameters
num_locations = 9
price = 12.5

# Dictionary to store utilities
utility_dict = {}

# Calculate and store utilities for each strategy profile
for i in range(1, num_locations + 1):
    for j in range(1, num_locations + 1):
        # Using the utility function
        utility_dict[(i, j)] = utility(i, j, price, num_locations)


# Alternatively, you can also store the results of the `u` function
u_dict = {}

for i in range(1, num_locations + 1):
    for j in range(1, num_locations + 1):
        # Using the `u` function
        u_dict[(i, j)] = u(i, j, price, num_locations)

