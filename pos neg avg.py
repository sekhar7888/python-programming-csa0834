positive_sum = 0
negative_sum = 0
positive_count = 0
negative_count = 0

while True:
    num = int(input("Enter a number (or -1 to exit): "))
    if num == -1:
        break
    if num > 0:
        positive_sum += num
        positive_count += 1
    elif num < 0:
        negative_sum += num
        negative_count += 1

if positive_count > 0:
    positive_average = positive_sum / positive_count
    print("The average of positive numbers is:", positive_average)
if negative_count > 0:
    negative_average = negative_sum / negative_count
    print("The average of negative numbers is:", negative_average)
