def remove_fourth_character(word: str) -> str:
    before_remove = word[:3]
    after_remove = word[4:]

    return before_remove + after_remove


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
