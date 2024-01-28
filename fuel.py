def main():
     while True:
        try:
            fraction_str = input("Fraction: ")
            percentage = convert(fraction_str)
            result = gauge(percentage)
            print(result)
            break
        except (ValueError,ZeroDivisionError):
            continue


def convert(fraction):
    x, y = map(int, fraction.split('/'))
    if not (isinstance(x, int) and isinstance(y, int)):
        raise ValueError
    if x > y:
        raise ValueError
    if y == 0:
        raise ZeroDivisionError
    percentage = round((x / y) * 100)
    return percentage

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()



