"""
Write a function named setAlarm/set_alarm/set-alarm/setalarm
(depending on language) which receives two parameters.

The first parameter, employed,
is true whenever you are employed and the second parameter,
vacation is true whenever you are on vacation.

The function should return true if you are employed and not on vacation
(because these are the circumstances under which you need to set an alarm).

It should return false otherwise. Examples:

employed | vacation
true     | true     => false
true     | false    => true
false    | true     => false
false    | false    => false


employed - true - когда работаем
vacation - true - когда в отпуске


"""

def set_alarm(employed: bool, vacation: bool) -> bool:
    if employed == True and vacation == True:
        return False

    elif employed == True and vacation == False:
        return True

    elif employed == False and vacation == True:
        return False

    elif employed == False and vacation == False:
        return False



if __name__ == "__main__":
    print(set_alarm(True, True))