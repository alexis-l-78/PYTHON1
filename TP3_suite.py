

from TP3 import *
import datetime




def farm_factory(farm_name, animal_description):

	my_current_farm = Farm(farm_name)

	# for each animal in animal_description add it to the farm
	for ...
		my_current_farm..add_animal(..., ...., ...)
		
	return my_current_farm


if __name__ == "__main__":



	# Load JSON file into a variable
	...

	# 

	# Create farms list
	farm_list = []

	# For each farm in JSON file, create it and add it to the farm list

	for .....

		farm_list.append(farm_factory(..., ...))


	# The rest is the same as before.

	# We print the list of farms (and animals)
	for current_farm in farm_list:
		print(current_farm)


	# We start travelling to the future
	print("\nWe start the time...:\n")

	time_iteration = 0

	while time_iteration < 100:

		# Advance time of 28 days = 4 weeks
		future_farms_date = current_farms_date + datetime.timedelta(days = 28)

		print("\n\tAdvancing to : " + str(future_farms_date))

		time_iteration += 1

		for current_farm in farm_list:
			current_farm.pass_time(datetime.timedelta(weeks = 4))


		current_farms_date = future_farms_date



	# We print the list of farms (and animals)
	for current_farm in farm_list:
		print(current_farm)



