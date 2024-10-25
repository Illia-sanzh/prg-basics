def m_to_cm(n):
    return n*100

def cm_to_m(n):
    return n/100

def cm_to_inch(n):
    return n/2.52

def feetandinch_to_cm(feet, inches):
    return (feet*30.24) + (inches*2.52)

if __name__ == "__main__":
    # only execute when you run this module
    # so you can test the functions in this place
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')

