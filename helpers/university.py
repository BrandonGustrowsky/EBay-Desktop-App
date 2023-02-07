from helpers.json_funcs import create_json_file, append_to_json_file, read_json_file
import os

def product_search(file_path, product_name):
    products_list = read_json_file(file_path)
    if len(products_list) == 0:
        return "There is no product in our database that matches your search.  Use only the name of the product you wish to find.  Searching by prices, images, or descriptions will not guarantee a desired result.   :)"
    matching_products = []
    for pos in range(len(products_list)):
        for item in products_list[pos].values():
            print(f"{item}")
            if item[0].casefold() == product_name.casefold():# or product_name.casefold() in item[0]
                for key, value in products_list[pos].items():
                    matching_products.append(key)
                matching_products.append(item)
            else:
                product_search_name = item[0].split()
                for word in product_search_name:
                    if word.casefold() in product_name.casefold():
                        for key, value in products_list[pos].items():
                            matching_products.append(key)
                        matching_products.append(item)

    if len(matching_products) == 0:
        return "There is no product in our database that matches your search.  Use only the name of the product you wish to find.  Searching by prices, images, or descriptions will not guarantee a desired result.   :)"
    return matching_products

def show_new_products(file_path):
    products_list = read_json_file(file_path)
    list_to_return = []
   
        #If there are fewer than 8 products in the list
    if len(products_list) <= 8 and len(products_list) >= 1:
        for pos in range(len(products_list)):
            for key, value in products_list[pos].items():
                list_to_return.append(key)
                for item_info in products_list[pos].values():
                    list_to_return.append(item_info)
        return list_to_return
    elif len(products_list) > 8:   #If there are enough products to display on the page (at least 8)
        for pos in range(len(products_list)-8, len(products_list)):
            for key, value in products_list[pos].items():
                list_to_return.append(key)
                for item_info in products_list[pos].values():
                    list_to_return.append(item_info)
        #This statement is only reached if the products_list is greater than 8 (The else statement on line 38)
        return list_to_return
    else:
        #If there are no products to display
        return "There are no products to display :("

def is_university(file_path, name) -> bool:
    '''Determines if university exists'''
    university_list = read_json_file(file_path)
    for school in university_list:
        if school.casefold() == name.casefold():
            return True

def add_university(parent_path, file_path, name):
    '''Adds a university to the program. Appends it to the all_universities.json file
    and creates a new directory with the university name. Also, it creates two new data files
    to store information about students and products associated with that university.'''
    os.chdir(parent_path)
    os.mkdir(name)
    create_json_file(os.path.join(parent_path, name), "all_students.json")
    create_json_file(os.path.join(parent_path, name), "all_products.json")
    append_to_json_file(file_path, name)

