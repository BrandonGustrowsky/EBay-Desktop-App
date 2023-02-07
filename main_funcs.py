from helpers.student import email_exists, is_matching_password, create_student_directory, add_product, delete_product, get_products
from helpers.university import is_university, add_university, show_new_products, product_search
from helpers.json_funcs import append_to_json_file
import os
import random
import string

BASE_PATH = os.path.dirname(__file__)
DATA_FILES_PATH = os.path.join(BASE_PATH, "Data Files")
IMAGES_PATH = os.path.join(BASE_PATH, "Images")
ALL_UNIVERSITIES_FILE = os.path.join(DATA_FILES_PATH, "all_universities.json")
ALL_STUDENT_INFO_FILE = os.path.join(DATA_FILES_PATH, "all_student_info.json")
ALL_PRODUCTS_FILE = os.path.join(DATA_FILES_PATH, "all_products.json")

def buy_product(university_name, student_email, product_id):
    delete_product(ALL_PRODUCTS_FILE, os.path.join(DATA_FILES_PATH, university_name, "all_products.json"), os.path.join(DATA_FILES_PATH, university_name, student_email, "student_products.json"), product_id)

def search(university_name, item):
    search_results = product_search(os.path.join(DATA_FILES_PATH, university_name, "all_products.json"), item)
    return search_results

def create_product_id(size: str = 10, chars = string.ascii_uppercase + string.digits):
    '''Creates special product ID'''
    product_id = ''.join(random.choice(chars) for _ in range(size))
    return product_id

def create_new_product(university_name, student_email, title, description, price, img_path):
    add_product(os.path.join(DATA_FILES_PATH, university_name, "all_products.json"), os.path.join(DATA_FILES_PATH, university_name, student_email, "student_products.json"), ALL_PRODUCTS_FILE, create_product_id(), title, description, price, img_path)

def view_recently_added_products(university_name):
    '''Allows the user to view recently added products.'''
    products = show_new_products(os.path.join(DATA_FILES_PATH, university_name, "all_products.json"))
    return products

def create_account(university, new_name, new_email, new_password):
    if len(university) > 0:
        if len(new_name) > 0:
            if len(new_email) > 0 and not email_exists(ALL_STUDENT_INFO_FILE, new_email):
                if len(new_password) > 0:
                    temp_dict = {new_name: [new_email, new_password]}
                    # Creates a new university if the entered name does not exist
                    if not is_university(ALL_UNIVERSITIES_FILE, university):
                        add_university(DATA_FILES_PATH,
                                       ALL_UNIVERSITIES_FILE, university)
                    create_student_directory(os.path.join(
                        DATA_FILES_PATH, university), new_email)
                    # Appends data to the global all_student_info file in Data Files
                    append_to_json_file(ALL_STUDENT_INFO_FILE, temp_dict)
                    # Appends data to the University's individual student info file
                    append_to_json_file(os.path.join(
                        DATA_FILES_PATH, university, "all_students.json"), temp_dict)
                    return True
    return False

def login(university, email, password):
    if len(university) > 0 and is_university(ALL_UNIVERSITIES_FILE, university):
        if len(email) > 0 and email_exists(ALL_STUDENT_INFO_FILE, email):
            if len(password) > 0 and is_matching_password(ALL_STUDENT_INFO_FILE, email, password):
                return True
    return False
