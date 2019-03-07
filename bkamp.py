
def help():
    message = "convert() takes n and lst as variables, where n = the number you want to 'mod' and lst being the array from which data is taken /n arrayChoice() takes n where n is the array you want"
    return message

def convert(n, lst):
    s = ''
    while True:
        s = lst[n % len(lst)] + s
        if n < len(lst):
            break
        n = n // len(lst) - 1
    return s


def arrayChoice(n):
    if n == 1 or n == "short" or n == "s":
        array = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","e","w","x","y","z"]
    elif n == 2 or n == "full" or n =="s":
        array = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","e","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","E","W","X","Y","Z"]
    return array 

def commonPasswords:
    array = ["password", "123456", "123456", "1234", "qwerty", "12345", "dragon", "pussy", "baseball", "football", "letmein", "monkey", "696969", "abc123", "mustang", "michael", "shadow", "master", "jennifer", "111111", "2000", "jordan", "superman", "harley", "1234567", "fuckme", "hunter", "fuckyou", "trustno1","ranger", "buster"]
    return array
    #source: https://www.passwordrandom.com/most-popular-passwords