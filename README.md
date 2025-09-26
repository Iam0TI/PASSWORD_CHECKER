# Password Checker using Pwned Passwords API

This is a Python script that checks if a given password has been compromised using the Pwned Passwords API. The script converts the password into a SHA-1 hash and sends the first five characters of the hash to the API to retrieve a list of hash suffixes that match. It then checks if the full hash of the password is present in the API response.

## Prerequisites

Before using the script, you need to have Python installed on your system. You can download and install Python from the official [Python website](https://www.python.org/downloads/).

## Usage

1. Clone this repository or download the `password_checker.py` script.
2. Open a terminal or command prompt.
3. Navigate to the directory where the `password_checker.py` script is located.
4. Run the script by providing one or more passwords as command-line arguments. For example:

    ```bash
    python password_checker.py password1 password2 password3
    ```

5. The script will check each provided password and display whether it has been compromised or not.

## How It Works

The script uses the Pwned Passwords API to check if a password has been exposed in data breaches. It follows these steps:

1. Converts the password to a SHA-1 hash.
2. Sends the first five characters of the hash to the Pwned Passwords API.
3. Receives a list of hash suffixes that match the API query.
4. Checks if the full hash of the password is present in the received list.

If the password is found in the Pwned Passwords database, the script suggests using a better password.

## Disclaimer

This script is provided for educational purposes and as a reference. It's important to note that the script sends a partial hash of the password to the Pwned Passwords API for privacy reasons. However, if you have concerns about using external APIs for password checking, you might want to consider other methods of password security.

## Credits

Script created by iam0ti
	
