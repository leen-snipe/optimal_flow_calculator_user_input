def compare_values(optimal_values, user_values):
    main_water_ratio = user_values[0] / optimal_values[0]

    failed_indexes = []
    result = True

    for i in range(len(optimal_values)):
        if i == 0:
            continue #that means to skip the 1st value as its the Main Water Quantity

        current_ratio = user_values[i] / optimal_values[i]

        if current_ratio > main_water_ratio:
            failed_indexes.append(i)
            result = False

    return result, failed_indexes

optimal_values = [10, 10, 100, 50, 30, 70, 10]
user_values = [100, 1, 500, 10, 3, 170, 30]

result, failed_indexes = compare_values(optimal_values, user_values)

print("Pass/Fail:", result)
print("Failed Indexes:", failed_indexes)
