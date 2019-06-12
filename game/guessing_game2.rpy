label guessing_game2:
    python:
        import importlib
        import random
        import submit

        solved = False
        secret = random.randint(0, 1000)

        def read_guess_from_terminal():
            return int(renpy.input("what's the password? (3 digits)"))

        def check_guess(guess):
            global solved, secret
            if guess == secret:
                solved = True

        def reload_submit_guess():
            global submit
            submit = importlib.reload(submit)
            submit.read_guess_from_terminal = read_guess_from_terminal
            submit.submit_guess = check_guess
            submit.main()

        while not solved:
            try:
                reload_submit_guess()
            except Exception as e:
                renpy.say("Clara","Error booting the password checker!")
                renpy.say("Clara","[e]") #print(e)
                renpy.say("Clara","Press enter to restart the computer")
                continue
            if not solved:
                renpy.say("Clara","Wrong!")
                renpy.input("Press enter to restart the computer")
        renpy.say("Clara","You're in!")

    return