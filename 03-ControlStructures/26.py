temp = 10
match temp:
    case temp if temp > 35:
        print("It is extremely hot")
    case temp if temp > 30:
        print("It is hot")
    case temp if temp > 15:
        print('it is warm')
    case temp if temp > 0:
        print('it is cold')
    case temp if temp <= 0:
        print('it is freezing')