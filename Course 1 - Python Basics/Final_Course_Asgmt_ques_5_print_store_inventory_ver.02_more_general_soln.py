# Question no 5:
# Provided is a list of data about a store’s inventory where each item in the list 
# represents the name of an item, how much is in stock, and how much it costs. 
# Print out each item in the list with the same formatting, 
# using the .format method (not string concatenation). 
# For example, the first print statment should read 
#      The store has 12 shoes, each for 29.99 USD.

# This corrected soln, ver.02, removes the spaces for each item on item_info_list.

inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]
for item_info in inventory:
    item_info_list_temp = item_info.split(',')
#    print('item_info_list_temp:', item_info_list_temp)
    item_info_list = []
    for item in item_info_list_temp:
        item_info_list.append(item.strip())
#    print('item_info_list     :', item_info_list)
    print('The store has {} {}, each for {} USD.'.format(item_info_list[1], item_info_list[0], item_info_list[2]))
#    print('The store has{} {}, each for{} USD.'.format(item_info_list[1], item_info_list[0], item_info_list[2]))
