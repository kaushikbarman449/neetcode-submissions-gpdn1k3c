from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    topper, max_score = scores[0]
    for name, score in scores:
        if score > max_score:
            topper = name
            max_score = score

    return topper

# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
