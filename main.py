# Refer to the README.md file in this project for a description 
# of the challenge and requirements. When viewing the README.md, 
# replit will show an option to Open Preview, which will open a 
# more readable view.

# The Python module math is imported and available to use but not required.
# Please do not import any additional modules (such as NumPy).

import math

trip_length = 1000
charge_cost = 5
charge_number = []
trip_cost = []

def ev_roadtrip(vehicle_names, vehicle_ranges, vehicle_rental_prices):
  index = 0
  
  for vehicle in vehicle_names:
      # adds the number of times vehicle needs to be charged for trip rounded up
      charge_number.append(math.ceil(trip_length/vehicle_ranges[index]))
      # creates a list with total cost per vehicle per trip # charges * cost plus rental * 3 days
      trip_cost.append((charge_number[index] * charge_cost) + (vehicle_rental_prices[index] * 3))
      index = index + 1

  min_ele = trip_cost[0]
  for i in range(1, len(trip_cost)):
    if trip_cost[i] < min_ele:
      min_ele = trip_cost[i]
  min_ele_dollars = "$" + str(format(min_ele,'.2f'))

  #Gets index of most affordable trip for matching with vehicle_names list
  index_min_ele = trip_cost.index(min_ele)

  print(f"The least expensive vehicle is the {vehicle_names[index_min_ele]} which will cost {min_ele_dollars} to take on the trip.")

pass

vehicle_names = ["Leaf"]
vehicle_ranges = [200]
vehicle_rental_prices = [75.00]

ev_roadtrip(vehicle_names, vehicle_ranges, vehicle_rental_prices)
# You may call ev_roadtrip with your own arguments here.
# For example, if the following line is uncommented, and the Run button
# is clicked, it will call ev_roadtrip with the listed
# parameters. The supplied example uses the same arguments as the
# test Challenge01.
    
# ev_roadtrip([‘Toyota Prius’, ‘Leaf’, ‘ID4’], [100, 200, 75]], [50.00, 75.00, 100.00])

# The challenges are provided as a set of tests that can be run 
# from the Tests panel at the left (the icon looks like a check 
# mark). Clicking the Run tests button will run the Challenge 
# inputs against your code, displaying either a success message, 
# or a message about what was expected and what was observed.
