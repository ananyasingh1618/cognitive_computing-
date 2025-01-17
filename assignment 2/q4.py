A = {34, 56, 78, 90}
B = {78, 45, 90, 23}
unique_scores = A.union(B)
print("Union", unique_scores)
common_scores = A.intersection(B)
print("Intersection", common_scores)
exclusive_scores = A.symmetric_difference(B)
print("Symmetric Difference", exclusive_scores)
is_subset = A.issubset(B)
is_superset = B.issuperset(A)
print("team A's scores a subset of team B?", is_subset)
print("team B's scores a superset of team A?", is_superset)
X = int(input("Enter the score to remove from set A: "))
if X in A:
    A.remove(X)
    print(f"Score {X} removed from set A.")
else:
    print(f"Score {X} is not present in set A.")
