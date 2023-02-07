from helpers.json_funcs import read_json_file, append_to_json_file, create_json_file, overwrite_json_file
import os

def get_first_name(file_path, email):
    contents = read_json_file(file_path)
    for pos in range(len(contents)):
        for key, value in contents[pos].items():
            if value[0] == email:
                return key.split()[0]

def get_products(file_path):
    '''Returns None if there are no items in the file, else returns a list'''
    return read_json_file(file_path)

def delete_product(global_products_path, university_products_path, student_products_path, product_id):
    global_json = read_json_file(global_products_path)
    uni_json = read_json_file(university_products_path)
    student_json = read_json_file(student_products_path)

    data = [global_json, uni_json, student_json]

    for lst in data:
        for dictionary in lst:
            for key, value in dictionary.items():
                if key == product_id:
                    lst.remove(dictionary)

    overwrite_json_file(global_products_path, global_json)
    overwrite_json_file(university_products_path, uni_json) #University file being overwritten
    overwrite_json_file(student_products_path, student_json) #Student file being overwritten

def add_product(university_products_path, student_path, all_products_path, product_id, product_name, product_description, product_price, product_img):
    '''
    Creates a new json file with details about a new product.
    Adds the product to "all_products.json" in /Data Files and "all_products.json" within the correct University folder
    \n***Parameters***
    \nuniversity_products_path: The path to the university's "all_products.json" file
    \n student_dir: The path to the logged in student's personal "products.json" file in their folder
    \nall_products_path: The path to the "all_products.json" file located directly inside "/Data Files"
    \nproduct_id: The random ID assigned to the product
    \nproduct_name: The name of the product
    \nproduct_description: The description of the product
    \nproduct_price: The price of the product
    '''
    product_info = {product_id: [product_name, product_description, product_price, product_img]}
    append_to_json_file(all_products_path, product_info)
    append_to_json_file(student_path, product_info)
    append_to_json_file(university_products_path, product_info)

def create_student_directory(parent_path, student_email):
    os.chdir(parent_path)
    os.mkdir(student_email)
    create_json_file(os.path.join(parent_path, student_email), "student_products.json")

def email_exists(file, email) -> bool:
    '''Returns 'True' if the email exists'''
    student_data = read_json_file(file)
    for elem in student_data:
        for values in elem.values():
            if values[0] == email:
                return True
    return False

def is_matching_password(file, email, password) -> bool:
    '''Returns 'True' if password equals the password paired with the email '''
    student_data = read_json_file(file)
    for elem in student_data:
        for values in elem.values():
            if values[0] == email and values[1] == password:
                    return True
    return False
