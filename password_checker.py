"""TO_DO"""
#CREATE THE PASSWORDMAKER AND INTIGRATE THEM  

import requests
import hashlib
import sys

password_list = sys.argv[1:]


def request_api_data (query_char):
    url = 'https://api.pwnedpasswords.com/range/' +str(query_char)
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError (f'Error fetching : {res.status_code},check api url')
    return res

def get_hash_and_count(hashes, hash_to_check ):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    
    for h,count in hashes:
        if hash_to_check == h:
            return count
    return 0

def pwned_api_check(password):
    #check password if it exist in api response
    #convert password to unicode object
    password = password.encode('ascii')
    hash_pass = hashlib.sha1(password)
    hashed_password = hash_pass.hexdigest().upper()
    first5_char , tail = hashed_password[:5],hashed_password[5:]
        # getting response from the api 
    response = request_api_data(first5_char)
    return get_hash_and_count(response, tail)
    

def main(args):
    for password in args :
        count= pwned_api_check(password)
        
        if count:
                print(f'{password} is found {count} times please try a better password :)')
        else:
                print(f'{password} is a good password :)')
    return args 
                

if __name__== "__main__":
    sys.exit(main(password_list))


#implement a function to hash the input from sys.argv using  sha1 and extract the first five char
