scores = (45, 89.5, 76, 45.4, 89, 92, 58, 45)
highest_score = max(scores)
highest_index = scores.index(highest_score)
print("The highest score is", highest_score, "at index", highest_index)
lowest_score = min(scores)
lowest_count = scores.count(lowest_score)
print("The lowest score is", lowest_score, "and it appears", lowest_count, "times")
reversed_scores = list(scores[::-1])
print("Reversed tuple as a list:", reversed_scores)
user_input = float(input("Enter the score to check "))
if user_input in scores:
    first_occurrence_index = scores.index(user_input)
    print("The score", user_input, "is present at index", first_occurrence_index)
else:
    print("The score", user_input, "is not present in the tuple.")
