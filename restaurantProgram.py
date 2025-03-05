import random
from restaurantTables import restaurant_tables  # Import the restaurant_tables variable from the .py file

###LEVEL 1

def display_available_tables(restaurant_tables):
    # Step 1: Loop through each column in row 0 (Skipping the first column)
    for col_index in range(1, len(restaurant_tables[0])):
        # Extract the table label (e.g., 'T1(2)')
        table_label = restaurant_tables[0][col_index]
        
        # Step 2: Loop through each row (Individual tables under each column)
        for row_index in range(1, len(restaurant_tables)):
            # Generate a unique table ID (e.g., T11-12345, T12-23456)
            table_id = f"T{col_index}{row_index}-{random.randint(10000, 99999)}"
            
            # Print the available table details if the table is available ('o')
            if restaurant_tables[row_index][col_index] == 'o':
                print(f"Table {table_label}, ID: {table_id}, Status: Available")

# Call the function to display all available tables
display_available_tables(restaurant_tables)


###LEVEL 2

'''
def find_party_table(restaurant_tables, party_size):
    """Finds and prints an available table that fits the given party size."""
    
    # Step 1: Loop through each column in row 0 (Skipping the first column)
    for col_index in range(1, len(restaurant_tables[0])):
        # Extract the table label (e.g., 'T1(2)')
        table_label = restaurant_tables[0][col_index]

        # Extract the seating capacity from the label (number inside parentheses)
        capacity = int(table_label.split('(')[1].split(')')[0])

        # Step 2: If capacity is large enough, check for availability
        if capacity >= party_size:
            # Step 3: Loop through each row to find a free table
            for row_index in range(1, len(restaurant_tables)):
                # Check if the table is free ('o')
                if restaurant_tables[row_index][col_index] == 'o':
                    # Generate a unique table ID (e.g., T11-12345)
                    table_id = f"T{col_index}{row_index}-{random.randint(10000, 99999)}"

                    # Print the available table details
                    print(f"Table {table_label}, ID: {table_id}, Status: Available")
                    
                    return # Stop printing after finding one table

         # Step 4: If no table is found, notify the user
                else:
                    print("Sorry, there are currently no available tables that fit the requested party size.")

# Example usage:
find_party_table(restaurant_tables, 4)  # Call the function with a party size of 4



#LEVEL 3

def find_party_tables(restaurant_tables, party_size):
    """Finds and prints available tables that fit the given party size."""
    
    # Step 1: Loop through each column in row 0 (Skipping the first column)
    for col_index in range(1, len(restaurant_tables[0])):
        # Extract the table label (e.g., 'T1(2)')
        table_label = restaurant_tables[0][col_index]

        # Extract the seating capacity from the label (number inside parentheses)
        capacity = int(table_label.split('(')[1].split(')')[0])

        # Step 2: If capacity is large enough, check for availability
        if capacity >= party_size:
            # Step 3: Loop through each row to find a free table
            for row_index in range(1, len(restaurant_tables)):
                # Check if the table is free ('o')
                if restaurant_tables[row_index][col_index] == 'o':
                    # Generate a unique table ID (e.g., T11-12345)
                    table_id = f"T{col_index}{row_index}-{random.randint(10000, 99999)}"

                    # Print the available table details
                    print(f"Table {table_label}, ID: {table_id}, Status: Available")

                else:
                    print("Sorry, there are currently no available tables that fit the requested party size.")

# Example usage:
find_party_tables(restaurant_tables, 4)  # Call the function with a party size of 4


# LEVEL 4

def find_tables_including_combos(restaurant_tables,party_size):
    """Finds available tables for a party size, combining tables if necessary."""
     # Step 1: Loop through each column in row 0 (Skipping the first column)
    for col_index in range(1, len(restaurant_tables[0])):
        # Extract the table label (e.g., 'T1(2)')
        table_label = restaurant_tables[0][col_index]

        # Extract the seating capacity from the label (number inside parentheses)
        capacity = int(table_label.split('(')[1].split(')')[0])
        
        # Step 2: If capacity is large enough, check for availability
        if capacity >= party_size:
            for row_index in range(1, len(restaurant_tables)):
                if restaurant_tables[row_index][col_index] == 'o':  # Check if table is free
                    table_id = f"T{col_index}{row_index}-{random.randint(10000, 99999)}"
                    print(f"Table {table_label}, ID: {table_id}, Status: Available")
                    

        # Step 3: If capacity is too small, attempt to combine adjacent tables
        elif capacity < party_size:
            for row_index in range(1, len(restaurant_tables)):
                if restaurant_tables[row_index][col_index] == 'o':
                    #If there are free tables, begin to add the adjacent ones.
                    #Create a new code that takes each open cell position and adds its current value to an adjacent cell's value. 

                    #Print the combined available tables.
				    
find_tables_including_combos(restaurant_tables,4)
'''