# Without using regex:


def check_password(password):
    special_sym = ['$', '@', '#', '%']
    val = True

    if len(password) < 8:
        print('length should be at least 8')
        val = False

    if len(password) > 10:
        print('length should be not be greater than 10')
        val = False

    if not any(char.isdigit() for char in password):
        print('Password should have at least one numeral')
        val = False

    if not any(char.isupper() for char in password):
        print('Password should have at least one uppercase letter')
        val = False

    if not any(char.islower() for char in password):
        print('Password should have at least one lowercase letter')
        val = False

    if not any(char in special_sym for char in password):
        print('Password should have at least one of the symbols $@#%')
        val = False
    if val:
        return val


password = input("Enter your Password:")
check_password(password)
if check_password(password):
    print("Password is valid")
else:
    print("Invalid Password !!")
# Using regex:
"""
import re 
  
def main(): 
    password = 'Geek12@'
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
      
    # compiling regex 
    pattern = re.compile(reg) 
      
    # searching regex                  
    match = re.search(pattern, password) 
      
    # validating conditions 
    if match: 
        print("Password is valid.") 
    else: 
        print("Password invalid !!") 
  
# Driver Code      
if __name__ == '__main__': 
    main() """