n = input()
numbers = list(map(int,(input().split())))

def turn (numbers):

    if len(numbers) == 0:
        return []

    return [numbers[-1]] + turn(numbers[0:len(numbers)-1])
    

print(' '.join(map(str, turn(numbers))))