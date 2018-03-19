while True:
    first_number = input('Fist Number:\n')
    
    if first_number == 'q':
        break
    
    second_number = input('Second Number:\n')

    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print('you can not devide by 0')
    except:
        print('Input Error')
    else:
        print(answer)
