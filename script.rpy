init python:
    import random
    def shuffle_answers(x):
            random.shuffle(x)
            return x
label start:
    "THIS BUILD YOU ARE PLAYING IS JUST A TEST BUILD AND JUST A DEMO OF THE QUIZ PART OF THE ET"
    "THIS BUILD CURRENTLY HAS 10 QUESTIONS IN WHICH THE PROGRAM WILL PICK AND DISPLAY ONLY 5"
    "JUST CHECK THE SCRIPT CODE TO CHECK FOR THE RIGHT ANSWER"
    "BREAK THIS SKRUB"
    "jk pls no hab mercy"

    $ easyQuestions = [
        {"question": "Which one is the first fully supported 64-bit operating system" , "answer" : [["Linux" , "right"] , ["Windows Vista" , "wrong"] , ["Mac" , "wrong"] ,["Windows XP" , "wrong"]]},
        {"question": "Hard Disk was first introduced in 1956 by" , "answer" : [["IBM" , "right"] , ["Dell" , "wrong"] , ["Apple" , "wrong"] ,["Microsoft" , "wrong"]]},
        {"question": "Which of the Following is not a web browser" , "answer" : [["Facebook" , "right"] , ["MOSAIC" , "wrong"] , ["WWW" , "wrong"] ,["Chrome" , "wrong"]]},
        {"question": "Trojan Refers to" , "answer" : [["Malware" , "right"] , ["Spyware" , "wrong"] , ["Worm" , "wrong"] ,["Virus" , "wrong"]]},
        {"question": "Which of the following is a programming language?" , "answer" : [["HPML" , "right"] , ["HTTP" , "wrong"] , ["HTML" , "wrong"] ,["FTP" , "wrong"]]},
        {"question": "Which protocol is used to receive email" , "answer" : [["POP3" , "right"] , ["SMTP" , "wrong"] , ["HTTP" , "wrong"] ,["FTP" , "wrong"]]},
        {"question": "What converts assembly language to machine language" , "answer" : [["Assembler" , "right"] , ["Interpreter" , "wrong"] , ["Compiler" , "wrong"] ,["Comparator" , "wrong"]]},
        {"question": "In which year the @ sign was first used for email" , "answer" : [["1972" , "right"] , ["1976" , "wrong"] , ["1980" , "wrong"] ,["1977" , "wrong"]]},
        {"question": "A folder in the windows os cant be made with the name" , "answer" : [["con" , "right"] , ["can" , "wrong"] , ["mak" , "wrong"] ,["make" , "wrong"]]},
        {"question": "what number system does a computer use to store data" , "answer" : [["binary" , "right"] , ["decimal" , "wrong"] , ["octal" , "wrong"] ,["hexadecimal" , "wrong"]]},
    ]

    $ quizPoints = 0
    $ quiz_length = 5
    $ answer_length = 4
    $ q_ask = []
    $ a_ask = []

    while len(q_ask) < quiz_length:
        $ a = random.choice(easyQuestions)
        if a not in q_ask:
            $ q_ask.append(a)
        if a not in a_ask:
            $ a_ask.append(a)

    label quize_game:
        $ a = random.choice(q_ask)
        $ q_ask.remove(a)
        $ b = shuffle_answers(a["answer"])
        $ d = []
        $ question = a["question"]


        if b[0][1] == "right":
            $ ans_0 = b[0][0]
            $ d.append(b[0][0])
        elif b not in d:
            $ d.append(b[0][0])
            $ ans_0 = d[0]
        if b[1][1] == "right":
            $ ans_1 = b[1][0]
            $ d.append(b[1][0])
        elif b not in d:
            $ d.append(b[1][0])
            $ ans_1 = d[1]
        if b[2][1] == "right":
            $ ans_2 = b[2][0]
            $ d.append(b[2][0])
        elif b not in d:
            $ d.append(b[2][0])
            $ ans_2 = d[2]
        if b[3][1] == "right":
            $ ans_3 = b[3][0]
            $ d.append(b[3][0])
        elif b not in d:
            $ d.append(b[3][0])
            $ ans_3 = d[3]

        menu:
            "[question]"
            "[ans_0]":
                if b[0][1] == "right":
                    $ quizPoints += 1
                else:
                    "Wrong Answer"
            "[ans_1]":
                if b[1][1] == "right":
                    $ quizPoints += 1
                else:
                    "Wrong"
            "[ans_2]":
                if b[2][1] == "right":
                    $ quizPoints += 1
                else:
                    "Wrong"
            "[ans_3]":
                if b[3][1] == "right":
                    $ quizPoints += 1
                else:
                    "Wrong"
        $ quiz_length -= 1
        if quiz_length > 0:
            jump quize_game

    "The result is [quizPoints]"
