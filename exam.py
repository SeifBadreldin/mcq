from utility import*
from test import*
while True:
    print("============")
    print("Multiple choice question system")
    print("============")
    main_choice=process_menu({
    "1":"English Exam",
    "2":"math Exam",
    "3":"programming Exam",
    "4":"French Exam",
    "5":"Exit"})

    if main_choice=="1":
        read_questions = readJson("English.json")
        exam(read_questions)
        print("==========================")
    elif main_choice=="2":
        read_questions = readJson("math.json")
        exam(read_questions)
        print("==========================")
    elif main_choice=="3":
        read_questions = readJson("programming.json")
        exam(read_questions)
        print("==========================")
    elif main_choice=="4":
        read_questions = readJson("french.json")
        exam(read_questions)
        print("==========================")
    elif main_choice=="5":
        break
