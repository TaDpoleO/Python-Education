fin = open('input.txt')
task_code = int(fin.readline())
interactor_code = int(fin.readline())
checker_code = int(fin.readline())

def answer(task_code, interactor_code, checker_code):
    if interactor_code == 0:
        if task_code != 0:
            return 3
        else:
            return checker_code
    elif interactor_code == 1:
        return checker_code
    elif interactor_code == 4:
        if task_code != 0:
            return 3
        else:
            return 4
    elif interactor_code == 6:
        return 0
    elif interactor_code == 7:
        return 1
    else:
        return interactor_code

print(answer(task_code, interactor_code, checker_code))