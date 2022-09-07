x = int(input("Введите четверть: "))

def check_chetvert(x):
    match x:
        case 1 :
            print("x>0 y>0")
        case 2 :
            print("x>0 y<0")
        case 3 :
            print("x<0 y<0")
        case 4 :
            print("x<0 y>0")
        case default :
            print("Неверная четверть")    

    
check_chetvert(x)