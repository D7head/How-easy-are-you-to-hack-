import itertools 
import string 

def brute_force(password, max_length): 
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits 
    attempts = 0  
    for length in range(1, max_length + 1): 
        for guess in itertools.product(characters, repeat=length): 
            guess = ''.join(guess) 
            attempts += 1  
            print(f'Пробуем: {guess}') 
            if guess == password: 
                return f'Пароль найден: {guess} за {attempts} попыток'
    return 'Пароль не найден' 

if __name__ == '__main__':  
    password_to_crack = input("Введите пароль для подбора: ") 
    max_length = int(input("Введите максимальную длину пароля: ")) 
    result = brute_force(password_to_crack, max_length) 
    print(result)