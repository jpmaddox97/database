def add(table_list):
    row = {}
    # Loop through header elements
    for list in table_list[0]:
        for element in list:

            # Show header element
            print(element)
            addition = input("Enter data: ")

            # Add to dictionary with header name as key
            row[element] = addition

        return row
