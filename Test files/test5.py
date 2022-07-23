class NotInRangeError(Exception):

	pass


def verbose_grade(grade_int):

    if grade_int == 2:
        return "Плохо"
    elif grade_int == 3:
        return "Плохо"
    elif grade_int == 4:
        return "Хорошо"
    elif grade_int == 5:
        return "Отлично"

    raise NotInRangeError("Value from 2 to 5 expected")

# И сразу же вызовем ее

verbose_grade(1)

# Такой код выведет

NotInRangeError: Value from 2 to 5 expected