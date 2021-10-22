class Main:
    """The main class that controls all of the quiz options."""

    # open().read().splitlines() is necessary so that the index of the question can be found (otherwise the code
    # throws up a ValueError:
    qList = open('questions.txt', 'r', encoding='utf-8').read().splitlines()
    aList = open('answers.txt', 'r', encoding='utf-8').read().splitlines()
    hList = open('hints.txt', 'r', encoding='utf-8').read().splitlines()

    # These strings are split to form lists of generic keywords for certain functions.  They are intended to make
    # the quiz and its operation more user-friendly (you don't have to remember one keyword, but can use one that
    # feels more natural):
    exitKeywords = "exit; end quiz; I'm finished; I'm done; I'm through; no more; fuck this".lower().split('; ')
    statisticsKeywords = "stats; statistics; score".lower().split('; ')
    hintKeywords = "hint; clue; give me a clue; ?; give me a hint; help me out here".lower().split('; ')
    catStatKeywords = "catstats; category statistics; category points; category score; category scores;" \
                      "category stats; cat stats".lower().split('; ')
    helpKeywords = "commandlist; commands; help".lower().split('; ')
    rightKeywords = "right; r; 1; right hand; right-hand".lower().split('; ')
    leftKeywords = "left; l; 0; left hand; left-hand".lower().split('; ')

    # These attributes exist in the class scope so that they can be used across all methods:
    qNumber = 1
    correctAnswers = 0
    qAnswered = 0
    qLength = 0
    longestStreak = 0
    currentStreak = 0
    repeatList = []
    catList = []

    # These attributes are associated with the various hint methods:
    hintsRemaining = 3
    detailedHintsUsed = 0
    wofHintsUsed = 0
    countdownHintsUsed = 0
    hangmanHintsUsed = 0
    hangmanGamesWon = 0

    # For the category statistics:
    categoryDictCorrect = {"ANATOMY": 0, "ARCHITECTURE": 0, "ART": 0, "ASTRONOMY": 0, "BIOCHEMISTRY": 0, "BIOLOGY": 0,
                           "BOTANY": 0, "CASTLES": 0, "CHEMISTRY": 0, "FOOD AND DRINK": 0, "GAMES AND ENTERTAINMENT": 0,
                           "GENERAL KNOWLEDGE": 0, "GENERAL SCIENCE": 0, "GEOGRAPHY": 0, "GEOLOGY": 0,
                           "HARRY POTTER": 0, "HISTORY": 0, "INVENTORS": 0, "LITERATURE": 0, "MATHEMATICS": 0,
                           "MEDICINE": 0, "MUSIC": 0, "MYTHOLOGY": 0, "NATO PHONETIC ALPHABET": 0, "OLOGY": 0,
                           "PHOBIAS": 0, "PHYSICS": 0, "POLITICS": 0, "RELIGION": 0, "ROMAN NUMERALS": 0, "SPORTS": 0,
                           "TECHNOLOGY": 0, "TV AND FILM": 0, "US HISTORY": 0, "WORLD LANGUAGES": 0, "ZOOLOGY": 0}
    categoryDictTotal = {"ANATOMY": 0, "ARCHITECTURE": 0, "ART": 0, "ASTRONOMY": 0, "BIOCHEMISTRY": 0, "BIOLOGY": 0,
                         "BOTANY": 0, "CASTLES": 0, "CHEMISTRY": 0, "FOOD AND DRINK": 0, "GAMES AND ENTERTAINMENT": 0,
                         "GENERAL KNOWLEDGE": 0, "GENERAL SCIENCE": 0, "GEOGRAPHY": 0, "GEOLOGY": 0, "HARRY POTTER": 0,
                         "HISTORY": 0, "INVENTORS": 0, "LITERATURE": 0, "MATHEMATICS": 0, "MEDICINE": 0, "MUSIC": 0,
                         "MYTHOLOGY": 0, "NATO PHONETIC ALPHABET": 0, "OLOGY": 0, "PHOBIAS": 0, "PHYSICS": 0,
                         "POLITICS": 0, "RELIGION": 0, "ROMAN NUMERALS": 0, "SPORTS": 0, "TECHNOLOGY": 0,
                         "TV AND FILM": 0, "US HISTORY": 0, "WORLD LANGUAGES": 0, "ZOOLOGY": 0}

    # For score calculation:
    counter5 = 0
    counter10 = 0
    counter25 = 0
    counter50 = 0
    counter100 = 0
    counter250 = 0
    counter500 = 0
    counter1000 = 0
    pointsFor = 0
    pointsAgainst = 0
    percentage = 0
    totalPts = 0

    # These hint booleans are used in the code to enable/disable hints if they have already been used on a question:
    hangmanHintBool = True
    countdownHintBool = True
    detailedHintBool = True
    wofHintBool = True

    def quiz_menu_categories(self):
        """A method that offers the quiz options and takes a user choice."""

        print("\n_.-:~='*^^*'=~:-._\n SCOTT'S PUB QUIZ \n^*'=~:-.__.-:~='*^")
        self.mainMenuChoice = input("\nWelcome to Scott's Pub Quiz! Please select an option from the list below:"
                                    "\n1 - ALL CATEGORIES (Answer questions from all categories)."
                                    "\n2 - PICK A TOPIC (Answer questions from a category you choose)."
                                    "\n")
        if self.mainMenuChoice == "":
            self.quiz_menu_categories()
        elif self.mainMenuChoice == "1":
            self.quiz_length_menu()
        elif self.mainMenuChoice == "2":
            self.playerCategory = input("\nPick a category from the list below you'd like to practice:"
                                        "\nANATOMY              ARCHITECTURE              ART"
                                        "\nASTRONOMY            BIOCHEMISTRY              BIOLOGY"
                                        "\nBOTANY               CASTLES                   CHEMISTRY"
                                        "\nFOOD AND DRINK       GAMES AND ENTERTAINMENT   GENERAL KNOWLEDGE"
                                        "\nGENERAL SCIENCE      GEOGRAPHY                 GEOLOGY"
                                        "\nHARRY POTTER         HISTORY                   INVENTORS"
                                        "\nLITERATURE           MATHEMATICS               MEDICINE"
                                        "\nMUSIC                MYTHOLOGY                 NATO PHONETIC ALPHABET"
                                        "\nOLOGY                PHOBIAS                   PHYSICS"
                                        "\nPOLITICS             RELIGION                  ROMAN NUMERALS"
                                        "\nSPORTS               TECHNOLOGY                TV AND FILM"
                                        "\nUS HISTORY           WORLD LANGUAGES           ZOOLOGY"
                                        "\n")
            for q in self.qList:
                if self.playerCategory.upper() in q:
                    self.catList.append(q)
                else:
                    pass
            self.quiz_length_menu()
        else:
            self.quiz_menu_categories()

    def quiz_length_menu(self):
        """A menu for navigating the full quiz."""

        self.quizLengthChoice = input("\nPlease select a game mode from list below:"
                                      "\n1 - INFINITE (Keep answering questions until you can't be bothered anymore)."
                                      "\n2 - PICK A LENGTH (Customise your quiz length!)"
                                      "\nX - Back to Main Menu."
                                      "\n")
        if self.quizLengthChoice == "1":
            if self.mainMenuChoice == "1":
                self.full_quiz()
            elif self.mainMenuChoice == "2":
                self.category_quiz()
            else:
                self.quiz_menu_categories()
        elif self.quizLengthChoice == "2":
            self.qLength = int(input("\nHow many questions do you want the quiz to be?"
                                     "\n"))
            if self.mainMenuChoice == "1":
                self.full_quiz()
            elif self.mainMenuChoice == "2":
                self.category_quiz()
            else:
                self.quiz_menu_categories()
        elif self.quizLengthChoice == "":
            self.quiz_length_menu()
        else:
            self.quiz_menu_categories()

    def full_quiz_question_generator(self):
        """A method for generating questions from any category."""

        import random
        import re

        self.hint_bools()

        if self.quizLengthChoice == "2":
            if self.qNumber > self.qLength:
                self.statistics()
                print("\nGAME OVER! Play again sometime!")
                self.quiz_menu_categories()
            else:
                pass
        else:
            pass

        if len(self.repeatList) >= 250:
            self.repeatList.remove(self.repeatList[0])
        else:
            pass

        self.question = random.choice(self.qList)
        if self.question in self.repeatList:
            self.full_quiz_question_generator()
        else:
            self.repeatList.append(self.question)

        self.qIndex = self.qList.index(self.question)
        self.aIndex = self.qIndex
        self.answer = self.aList[self.aIndex]

        categoryPattern = re.compile(r'([A-Z]+[\s]?)+')
        qCategoryRaw = categoryPattern.match(self.question)
        qCategory = qCategoryRaw.group(0)
        self.categoryDictTotal[qCategory] += 1

        # NOTE: This code block has been placed at the end of the method to ensure that if the method needs to run
        # multiple times, hints are not given when they aren't supposed to be. For example, if the player had answered
        # 10 questions, they would be due an additional hint. However, if a repeat question is generated then the
        # method needs to run again. If this code block had been at the start of the method, it would check the
        # questions answered and would distribute a hint. This could happen once or multiple times in error. Putting
        # this code block at the end of the method ensures that a hint is given only once an appropriate question has
        # been generated:
        if self.qAnswered % 10 == 0 and self.qAnswered > 0:
            self.hintsRemaining += 1
            print("YOU GAINED A HINT!")
        else:
            pass

    def category_question_generator(self):
        """A method for generating questions from a chosen category."""

        import random

        self.hint_bools()

        if self.quizLengthChoice == "2":
            if self.qNumber > self.qLength:
                self.statistics()
                print("\nGAME OVER! Play again sometime!")
                self.quiz_menu_categories()
            else:
                pass
        else:
            pass

        self.question = random.choice(self.catList)
        self.qIndex = self.qList.index(self.question)
        self.aIndex = self.qIndex
        self.answer = self.aList[self.aIndex]

        # NOTE: This code block has been placed at the end of the method to ensure that if the method needs to run
        # multiple times, hints are not given when they aren't supposed to be. For example, if the player had answered
        # 10 questions, they would be due an additional hint. However, if a repeat question is generated then the
        # method needs to run again. If this code block had been at the start of the method, it would check the
        # questions answered and would distribute a hint. This could happen once or multiple times in error. Putting
        # this code block at the end of the method ensures that a hint is given only once an appropriate question has
        # been generated:
        if self.qAnswered % 10 == 0 and self.qAnswered > 0:
            self.hintsRemaining += 1
            print("YOU GAINED A HINT!")
        else:
            pass

    def full_quiz_player_input(self):
        """This method handles player input for the full quiz."""

        playerGuess = input(f"\n{self.qNumber}. {self.question}"
                            f"\n").lower()
        if playerGuess in self.exitKeywords:                                # EXIT METHOD
            self.reset_statistics()
        elif playerGuess == "":                                             # NULL ANSWER CONDITION
            self.full_quiz_player_input()
        elif playerGuess in self.statisticsKeywords:                        # PLAYER STATISTICS METHOD
            self.statistics()
            self.full_quiz_player_input()
        elif playerGuess in self.hintKeywords:                              # HINT METHOD
            self.detailed_hint()
            self.full_quiz_player_input()
        elif playerGuess == "wheeloffortune":                               # WHEEL OF FORTUNE HINT METHOD
            if self.wofHintBool:
                self.wheel_of_fortune_hint()
            else:
                print("You only get to use the WHEEL OF FORTUNE hint once per question!")
            self.full_quiz_player_input()
        elif playerGuess == "scorebreakdown":                               # SCORE BREAKDOWN METHOD
            self.score_breakdown()
            self.full_quiz_player_input()
        elif playerGuess in self.catStatKeywords:                           # CATEGORY STATISTICS METHOD
            for keyword in self.catStatKeywords:
                if keyword == playerGuess:
                    self.category_statistics()
                    self.full_quiz_player_input()
                else:
                    pass
        elif playerGuess in self.helpKeywords:                              # HELP METHOD
            for keyword in self.helpKeywords:
                if keyword == playerGuess:
                    self.command_list()
                    self.full_quiz_player_input()
                else:
                    pass
        elif playerGuess == "rachelriley":                                  # COUNTDOWN HINT METHOD
            if self.countdownHintBool:
                self.countdown_hint()
            else:
                print("You only get Rachel's help once per question!")
            self.full_quiz_player_input()
        elif playerGuess == "hangman":                                      # HANGMAN HINT METHOD
            if self.hangmanHintBool:
                self.hangman_hint()
            else:
                print("You only get to play HANGMAN once per question! ...Did I not mention that?")
            self.full_quiz_player_input()
        elif playerGuess in self.answer.lower().split("; "):
            print(f"CORRECT! {playerGuess.upper()}!"
                  f"\n+20 \N{Greek Capital Letter Omega}")
            self.qAnswered += 1
            self.correctAnswers += 1
            self.qNumber += 1
            self.currentStreak += 1
            if self.currentStreak > self.longestStreak:
                self.longestStreak = self.currentStreak
            else:
                pass
            if self.correctAnswers % 1000 == 0:
                """Divisible by 1000."""
                self.counter1000 += 1
                print(f"+1000 \N{Greek Capital Letter Omega} BONUS ({self.correctAnswers} correct answers)")
            else:
                """Divisible by 500, 250, 100, 50, 25, 10 or 5."""
                if self.correctAnswers % 500 == 0:
                    """Divisible by 500."""
                    self.counter500 += 1
                    print(f"+500 \N{Greek Capital Letter Omega} BONUS ({self.correctAnswers} correct answers)")
                else:
                    """Divisible by 250, 100, 50, 25, 10 or 5."""
                    if self.correctAnswers % 250 == 0:
                        """Divisible by 250."""
                        self.counter250 += 1
                        print(f"+250 \N{Greek Capital Letter Omega} BONUS ({self.correctAnswers} correct answers)")
                    else:
                        """Divisible by 100, 50, 25, 10 or 5."""
                        if self.correctAnswers % 100 == 0:
                            """Divisible by 100."""
                            self.counter100 += 1
                            print(f"+100 \N{Greek Capital Letter Omega} BONUS ({self.correctAnswers} correct answers)")
                        else:
                            """Only divisible by 50, 25, 10 or 5."""
                            if self.correctAnswers % 50 == 0:
                                """Divisible by 50."""
                                self.counter50 += 1
                                print(f"+50 \N{Greek Capital Letter Omega} BONUS ({self.correctAnswers} correct answers)")
                            else:
                                """Only divisible by 25, 10 or 5."""
                                if self.correctAnswers % 25 == 0:
                                    """Divisible by 25."""
                                    self.counter25 += 1
                                    print(f"+25 \N{Greek Capital Letter Omega} BONUS ({self.correctAnswers} correct answers)")
                                else:
                                    """Only divisible by 10 or 5."""
                                    if self.correctAnswers % 10 == 0:
                                        """Divisible by 10."""
                                        self.counter10 += 1
                                        print(f"+10 \N{Greek Capital Letter Omega} BONUS ({self.correctAnswers} correct answers)")
                                    else:
                                        """Only divisible by 5."""
                                        if self.correctAnswers % 5 == 0:
                                            """Divisible by 5."""
                                            self.counter5 += 1
                                            print(f"+5 \N{Greek Capital Letter Omega} BONUS ({self.correctAnswers} correct answers)")
                                        else:
                                            pass

            self.category_statistics_checker()
        else:
            acceptableAnswers = self.answer.upper().split('; ')
            if len(acceptableAnswers) > 1:
                print(f"INCORRECT. There are {len(acceptableAnswers)} acceptable answers:")
                for a in acceptableAnswers:
                    print(f"- {a}")
            else:
                print(f"INCORRECT. The answer is {self.answer.upper().split('; ')[0]}.")
            self.qAnswered += 1
            self.qNumber += 1
            self.currentStreak = 0

    def full_quiz(self):
        """This method contains the operational part of the quiz if all categories are involved."""

        while 1:
            self.full_quiz_question_generator()
            self.full_quiz_player_input()

    def category_quiz(self):
        """This method contains the operational part of the quiz if a category is chosen."""

        while 1:
            self.category_question_generator()
            self.full_quiz_player_input()

    def command_list(self):
        """This method prints a list of all of the commands that can be used in the game. It also gives details of
        what each command does."""

        print(f"\n{'-' * 14}\n COMMAND LIST \n{'-' * 14}\n"
              f"\nCOMMANDLIST - This returns the command list for what you can do in the game."
              f"\nEXIT - This ends a game and the player's final score is returned to them."
              f"\nSCORE - This returns the player statistics for the game."
              f"\nSCOREBREAKDOWN - This returns a breakdown of the player's score e.g. hints used, correct answers."
              f"\nCATSTATS - This returns the breakdown of how well the player is doing in each category."
              f"\n - HINTS - "
              f"\nHINT - This returns a detailed hint. Careful - they cost points!"
              f"\nWHEELOFFORTUNE - Pick 5 letters you think are in the letter and they'll show up if you're correct."
              f"\nRACHELRILEY - Shows either the consonants or vowels in an answer. Depends how lucky you are."
              f"\nHANGMAN - Play a game of Hangman for the answer to the question!"
              f"\n")

    def statistics(self):
        """This method gives the stats for the current round of play (e.g. questions answered, correct answers,
        percentage score, hints remaining, etc.)"""

        import tabulate

        print(f"\n{'-' * 19}\n PLAYER STATISTICS \n{'-' * 19}")
        self.score()

        table = [
            [
                "Game Score:",
                f"{self.correctAnswers}/{self.qAnswered}",
                "Current Streak:",
                f"{self.currentStreak}",
                "Hints Used:",
                f"{self.detailedHintsUsed}",
                "Hangman Games Played:",
                f"{self.hangmanHintsUsed}",
            ],
            [
                "Percentage Game Score:",
                f"{self.percentage}%",
                "Longest Streak:",
                f"{self.longestStreak}",
                "Hints Remaining:",
                f"{self.hintsRemaining}",
                "Hangman Games Won:",
                f"{self.hangmanGamesWon}"
            ],
            [
                "",
                "",
                "",
                "",
                "",
                "",
                "Wheel of Fortune Hints Used:",
                f"{self.wofHintsUsed}"
            ],
            [
                "TOTAL:",
                f"{self.totalPts} \N{Greek Capital Letter Omega}",
                "",
                "",
                "",
                "",
                "Countdown Hints Used:",
                f"{self.countdownHintsUsed}"
            ],
        ]

        finalTable = tabulate.tabulate(
            table,
            tablefmt='plain',
            colalign=[
                'right', 'left', 'right', 'left', 'right', 'left'
            ]
        )

        print(f"{finalTable}")

    def score(self):
        """This method calculates the player's overall score."""

        # POINTS FOR:
        correctAnswersPts = self.correctAnswers * 20
        correctAnswersBonusPts = sum(
            (
                self.counter5 * 5,
                self.counter10 * 10,
                self.counter25 * 25,
                self.counter50 * 50,
                self.counter100 * 100,
                self.counter250 * 250,
                self.counter500 * 500,
                self.counter1000 * 1000
            )
        )
        hangmanGamesWonPts = self.hangmanGamesWon * 20

        # POINTS AGAINST:
        detailedHintsUsedPts = self.detailedHintsUsed * 30
        hangmanHintsUsedPts = self.hangmanHintsUsed * 10
        countdownHintsUsedPts = self.countdownHintsUsed * 20
        wofHintsUsedPts = self.wofHintsUsed * 10

        self.pointsFor = sum(
            (
                correctAnswersPts,
                correctAnswersBonusPts,
                hangmanGamesWonPts
            )
        )
        self.pointsAgainst = sum(
            (
                detailedHintsUsedPts,
                hangmanHintsUsedPts,
                countdownHintsUsedPts,
                wofHintsUsedPts
            )
        )

        # MISCELLANEOUS
        self.percentage = round((self.correctAnswers / self.qAnswered) * 100 if self.qAnswered != 0 else 0, 3)

        # TOTAL
        self.totalPts = self.pointsFor - self.pointsAgainst

    def score_breakdown(self):
        """A method to show the player what points they have earned and which ones they've lost."""

        import tabulate

        self.score()

        print(f"\n{'-' * 17}\n SCORE BREAKDOWN \n{'-' * 17}")
        table = [
            [
                "POINTS FOR",
                "",
                "POINTS AGAINST",
                ""
            ],
            [
                f"Correct Answers ({self.correctAnswers}):",
                f"{self.correctAnswers * 20}",
                f"Detailed Hints Used ({self.detailedHintsUsed}):",
                f"{self.detailedHintsUsed * 20}",
            ],
            [
                f"5-Question Bonus ({self.counter5}):",
                f"{self.counter5 * 5}",
                f"Hangman Games Played ({self.hangmanHintsUsed}):",
                f"{self.hangmanHintsUsed * 10}"
            ],
            [
                f"10-Question Bonus ({self.counter10}):",
                f"{self.counter10 * 10}",
                f"Countdown Hints Used ({self.countdownHintsUsed}):",
                f"{self.countdownHintsUsed * 20}"
            ],
            [
                f"25-Question Bonus ({self.counter25}):",
                f"{self.counter25 * 25}",
                f"Wheel of Fortune Hints Used ({self.wofHintsUsed}):",
                f"{self.wofHintsUsed * 10}"
            ],
            [
                f"50-Question Bonus ({self.counter50}):",
                f"{self.counter50 * 50}",
                "",
                ""
            ],
            [
                f"100-Question Bonus ({self.counter100}):",
                f"{self.counter100 * 100}",
                "",
                ""
            ],
            [
                f"Hangman Games Won ({self.hangmanGamesWon}):",
                f"{self.hangmanGamesWon * 20}",
                "",
                ""
            ],
            [
                "SUBTOTAL:",
                f"{self.pointsFor} \N{Greek Capital Letter Omega}",
                "SUBTOTAL:",
                f"{self.pointsAgainst} \N{Greek Capital Letter Omega}"
            ],
            [
                "",
                "",
                "",
                ""
            ],
            [
                "SCORE:",
                f"{self.totalPts} \N{Greek Capital Letter Omega}",
                "",
                ""
            ]
        ]

        finalTable = tabulate.tabulate(
            table,
            tablefmt='plain',
            colalign=[
                'right', 'left', 'right', 'left'
            ]
        )

        print(finalTable)

    def category_statistics_checker(self):
        """This method keeps an eye on how many correct answers come from each category.
        This could be developed into some sort of achievement e.g. get a certain number of correct answers in each
        category."""

        import re

        if self.qNumber == 1:
            for cat in self.categoryDictCorrect:
                self.categoryDictCorrect[cat] = 0
            for cat in self.categoryDictTotal:
                self.categoryDictTotal[cat] = 0
        else:
            pass

        categoryPattern = re.compile(r'([A-Z]+[\s]?)+')
        qCategoryRaw = categoryPattern.match(self.question)
        qCategory = qCategoryRaw.group(0)

        self.categoryDictCorrect[qCategory] += 1

    def category_statistics(self):
        """This method prints out the details of the category statistics checker."""

        import tabulate

        print(f"\n{'-' * 21}\n CATEGORY STATISTICS \n{'-' * 21}")

        table = [
            [
                "ARCHITECTURE" if self.categoryDictCorrect["ARCHITECTURE"] > 0 else "???",
                f"{self.categoryDictCorrect['ARCHITECTURE']}/{self.categoryDictTotal['ARCHITECTURE']}"
                if self.categoryDictCorrect['ARCHITECTURE'] > 0 else "",
                "MYTHOLOGY" if self.categoryDictCorrect["MYTHOLOGY"] > 0 else "???",
                f"{self.categoryDictCorrect['MYTHOLOGY']}/{self.categoryDictTotal['MYTHOLOGY']}"
                if self.categoryDictCorrect['MYTHOLOGY'] > 0 else "",
                "WORLD LANGUAGES" if self.categoryDictCorrect["WORLD LANGUAGES"] > 0 else "???",
                f"{self.categoryDictCorrect['WORLD LANGUAGES']}/{self.categoryDictTotal['WORLD LANGUAGES']}"
                if self.categoryDictCorrect['WORLD LANGUAGES'] > 0 else "",
                "US HISTORY" if self.categoryDictCorrect["US HISTORY"] > 0 else "???",
                f"{self.categoryDictCorrect['US HISTORY']}/{self.categoryDictTotal['US HISTORY']}"
                if self.categoryDictCorrect['US HISTORY'] > 0 else "",
                "GENERAL SCIENCE" if self.categoryDictCorrect["GENERAL SCIENCE"] > 0 else "???",
                f"{self.categoryDictCorrect['GENERAL SCIENCE']}/{self.categoryDictTotal['GENERAL SCIENCE']}"
                if self.categoryDictCorrect['GENERAL SCIENCE'] > 0 else "",
                "MUSIC" if self.categoryDictCorrect["MUSIC"] > 0 else "???",
                f"{self.categoryDictCorrect['MUSIC']}/{self.categoryDictTotal['MUSIC']}"
                if self.categoryDictCorrect['MUSIC'] > 0 else ""
            ],
            [
                "HARRY POTTER" if self.categoryDictCorrect["HARRY POTTER"] > 0 else "???",
                f"{self.categoryDictCorrect['HARRY POTTER']}/{self.categoryDictTotal['HARRY POTTER']}"
                if self.categoryDictCorrect['HARRY POTTER'] > 0 else "",
                "TECHNOLOGY" if self.categoryDictCorrect["TECHNOLOGY"] > 0 else "???",
                f"{self.categoryDictCorrect['TECHNOLOGY']}/{self.categoryDictTotal['TECHNOLOGY']}"
                if self.categoryDictCorrect['TECHNOLOGY'] > 0 else "",
                "MATHEMATICS" if self.categoryDictCorrect["MATHEMATICS"] > 0 else "???",
                f"{self.categoryDictCorrect['MATHEMATICS']}/{self.categoryDictTotal['MATHEMATICS']}"
                if self.categoryDictCorrect['MATHEMATICS'] > 0 else "",
                "GENERAL KNOWLEDGE" if self.categoryDictCorrect["GENERAL KNOWLEDGE"] > 0 else "???",
                f"{self.categoryDictCorrect['GENERAL KNOWLEDGE']}/{self.categoryDictTotal['GENERAL KNOWLEDGE']}"
                if self.categoryDictCorrect['GENERAL KNOWLEDGE'] > 0 else "",
                "ART" if self.categoryDictCorrect["ART"] > 0 else "???",
                f"{self.categoryDictCorrect['ART']}/{self.categoryDictTotal['ART']}"
                if self.categoryDictCorrect['ART'] > 0 else "",
                "GEOLOGY" if self.categoryDictCorrect["GEOLOGY"] > 0 else "???",
                f"{self.categoryDictCorrect['GEOLOGY']}/{self.categoryDictTotal['GEOLOGY']}"
                if self.categoryDictCorrect['GEOLOGY'] > 0 else ""
            ],
            [
                "BIOCHEMISTRY" if self.categoryDictCorrect["BIOCHEMISTRY"] > 0 else "???",
                f"{self.categoryDictCorrect['BIOCHEMISTRY']}/{self.categoryDictTotal['BIOCHEMISTRY']}"
                if self.categoryDictCorrect['BIOCHEMISTRY'] > 0 else "",
                "INVENTORS" if self.categoryDictCorrect["INVENTORS"] > 0 else "???",
                f"{self.categoryDictCorrect['INVENTORS']}/{self.categoryDictTotal['INVENTORS']}"
                if self.categoryDictCorrect['INVENTORS'] > 0 else "",
                "CASTLES" if self.categoryDictCorrect["CASTLES"] > 0 else "???",
                f"{self.categoryDictCorrect['CASTLES']}/{self.categoryDictTotal['CASTLES']}"
                if self.categoryDictCorrect['CASTLES'] > 0 else "",
                "BOTANY" if self.categoryDictCorrect["BOTANY"] > 0 else "???",
                f"{self.categoryDictCorrect['BOTANY']}/{self.categoryDictTotal['BOTANY']}"
                if self.categoryDictCorrect['BOTANY'] > 0 else "",
                "POLITICS" if self.categoryDictCorrect["POLITICS"] > 0 else "???",
                f"{self.categoryDictCorrect['POLITICS']}/{self.categoryDictTotal['POLITICS']}"
                if self.categoryDictCorrect['POLITICS'] > 0 else "",
                "NATO PHONETIC ALPHABET" if self.categoryDictCorrect["NATO PHONETIC ALPHABET"] > 0 else "???",
                f"{self.categoryDictCorrect['NATO PHONETIC ALPHABET']}/{self.categoryDictTotal['NATO PHONETIC ALPHABET']}"
                if self.categoryDictCorrect['NATO PHONETIC ALPHABET'] > 0 else ""
            ],
            [
                "SPORTS" if self.categoryDictCorrect["SPORTS"] > 0 else "???",
                f"{self.categoryDictCorrect['SPORTS']}/{self.categoryDictTotal['SPORTS']}"
                if self.categoryDictCorrect['SPORTS'] > 0 else "",
                "ANATOMY" if self.categoryDictCorrect["ANATOMY"] > 0 else "???",
                f"{self.categoryDictCorrect['ANATOMY']}/{self.categoryDictTotal['ANATOMY']}"
                if self.categoryDictCorrect['ANATOMY'] > 0 else "",
                "GAMES AND ENTERTAINMENT" if self.categoryDictCorrect["GAMES AND ENTERTAINMENT"] > 0 else "???",
                f"{self.categoryDictCorrect['GAMES AND ENTERTAINMENT']}/{self.categoryDictTotal['GAMES AND ENTERTAINMENT']}"
                if self.categoryDictCorrect['GAMES AND ENTERTAINMENT'] > 0 else "",
                "LITERATURE" if self.categoryDictCorrect["LITERATURE"] > 0 else "???",
                f"{self.categoryDictCorrect['LITERATURE']}/{self.categoryDictTotal['LITERATURE']}"
                if self.categoryDictCorrect['LITERATURE'] > 0 else "",
                "BIOLOGY" if self.categoryDictCorrect["BIOLOGY"] > 0 else "???",
                f"{self.categoryDictCorrect['BIOLOGY']}/{self.categoryDictTotal['BIOLOGY']}"
                if self.categoryDictCorrect['BIOLOGY'] > 0 else "",
                "ROMAN NUMERALS" if self.categoryDictCorrect["ROMAN NUMERALS"] > 0 else "???",
                f"{self.categoryDictCorrect['ROMAN NUMERALS']}/{self.categoryDictTotal['ROMAN NUMERALS']}"
                if self.categoryDictCorrect['ROMAN NUMERALS'] > 0 else ""
            ],
            [
                "CHEMISTRY" if self.categoryDictCorrect["CHEMISTRY"] > 0 else "???",
                f"{self.categoryDictCorrect['CHEMISTRY']}/{self.categoryDictTotal['CHEMISTRY']}"
                if self.categoryDictCorrect['CHEMISTRY'] > 0 else "",
                "HISTORY" if self.categoryDictCorrect["HISTORY"] > 0 else "???",
                f"{self.categoryDictCorrect['HISTORY']}/{self.categoryDictTotal['HISTORY']}"
                if self.categoryDictCorrect['HISTORY'] > 0 else "",
                "OLOGY" if self.categoryDictCorrect["OLOGY"] > 0 else "???",
                f"{self.categoryDictCorrect['OLOGY']}/{self.categoryDictTotal['OLOGY']}"
                if self.categoryDictCorrect['OLOGY'] > 0 else "",
                "ZOOLOGY" if self.categoryDictCorrect["ZOOLOGY"] > 0 else "???",
                f"{self.categoryDictCorrect['ZOOLOGY']}/{self.categoryDictTotal['ZOOLOGY']}"
                if self.categoryDictCorrect['ZOOLOGY'] > 0 else "",
                "RELIGION" if self.categoryDictCorrect["RELIGION"] > 0 else "???",
                f"{self.categoryDictCorrect['RELIGION']}/{self.categoryDictTotal['RELIGION']}"
                if self.categoryDictCorrect['RELIGION'] > 0 else "",
                "PHYSICS" if self.categoryDictCorrect["PHYSICS"] > 0 else "???",
                f"{self.categoryDictCorrect['PHYSICS']}/{self.categoryDictTotal['PHYSICS']}"
                if self.categoryDictCorrect['PHYSICS'] > 0 else ""
            ],
            [
                "MEDICINE" if self.categoryDictCorrect["MEDICINE"] > 0 else "???",
                f"{self.categoryDictCorrect['MEDICINE']}/{self.categoryDictTotal['MEDICINE']}"
                if self.categoryDictCorrect['MEDICINE'] > 0 else "",
                "PHOBIAS" if self.categoryDictCorrect["PHOBIAS"] > 0 else "???",
                f"{self.categoryDictCorrect['PHOBIAS']}/{self.categoryDictTotal['PHOBIAS']}"
                if self.categoryDictCorrect['PHOBIAS'] > 0 else "",
                "FOOD AND DRINK" if self.categoryDictCorrect["FOOD AND DRINK"] > 0 else "???",
                f"{self.categoryDictCorrect['FOOD AND DRINK']}/{self.categoryDictTotal['FOOD AND DRINK']}"
                if self.categoryDictCorrect['FOOD AND DRINK'] > 0 else "",
                "ASTRONOMY" if self.categoryDictCorrect["ASTRONOMY"] > 0 else "???",
                f"{self.categoryDictCorrect['ASTRONOMY']}/{self.categoryDictTotal['ASTRONOMY']}"
                if self.categoryDictCorrect['ASTRONOMY'] > 0 else "",
                "GEOGRAPHY" if self.categoryDictCorrect["GEOGRAPHY"] > 0 else "???",
                f"{self.categoryDictCorrect['GEOGRAPHY']}/{self.categoryDictTotal['GEOGRAPHY']}"
                if self.categoryDictCorrect['GEOGRAPHY'] > 0 else "",
                "TV AND FILM" if self.categoryDictCorrect["TV AND FILM"] > 0 else "???",
                f"{self.categoryDictCorrect['TV AND FILM']}/{self.categoryDictTotal['TV AND FILM']}"
                if self.categoryDictCorrect['TV AND FILM'] > 0 else ""
            ],
        ]

        finalTable = tabulate.tabulate(
            table,
            tablefmt='plain'
        )

        print(f"{finalTable}")

    def hint_bools(self):
        """This method is a collection of the hint boolean resets that must be triggered once a new question has been
        generated."""

        self.detailedHintBool = True
        self.hangmanHintBool = True
        self.countdownHintBool = True
        self.wofHintBool = True

    def detailed_hint(self):
        """This method gives a detailed hint from the hint file."""

        if self.hintsRemaining == 0:
            print("You have no more hints remaining!")
            self.full_quiz_player_input()
        else:
            self.detailedHintsUsed += 1
            self.hintsRemaining -= 1

            hIndex = self.qIndex
            detailedHint = self.hList[hIndex]
            print(f"{detailedHint}"
                  f"\n-20 \N{Greek Capital Letter Omega}")

    def wheel_of_fortune_hint(self):
        """This method turns the answer into an anagram and returns this to the player."""

        import string

        self.wofHintsUsed += 1
        self.wofHintBool = False

        letterInput = input("\nPlease enter FIVE letters that you think may be in the answer (separate with commas):"
                            "\n")

        l1, l2, l3, l4, l5 = letterInput.split(', ')

        wofHint = list(self.answer.lower().split('; ')[0])

        for index, letter in enumerate(wofHint):
            if letter in (l1, l2, l3, l4, l5):
                pass
            elif letter in string.digits:
                pass
            elif letter in string.punctuation:
                pass
            elif letter in string.whitespace:
                pass
            else:
                wofHint[index] = "-"

        print(f"{''.join(wofHint).upper()}")

    def countdown_hint(self):
        """A method that fills in either the vowels or consonants in the word, randomly choosing one or the other."""

        import random
        import string

        self.countdownHintsUsed += 1
        self.countdownHintBool = False

        vowels = "aeiou"

        rightHand = str(random.randint(0, 1))
        leftHand = str(0 if rightHand == 1 else 1)

        handChoice = input("\nI have VOWELS in one hand and CONSONANTS in the other.  Pick a hand - RIGHT or LEFT?"
                           "\n")

        if handChoice.lower() in self.rightKeywords and rightHand in self.rightKeywords:
            consonantsHint = list(self.answer.lower().split("; ")[0])

            for index, letter in enumerate(consonantsHint):
                if letter not in vowels:
                    pass
                elif letter in string.digits:
                    pass
                elif letter in string.punctuation:
                    pass
                elif letter in string.whitespace:
                    pass
                else:
                    consonantsHint[index] = "-"
            print(f"{''.join(consonantsHint).upper()}")
        elif handChoice.lower() in self.leftKeywords and leftHand in self.leftKeywords:
            consonantsHint = list(self.answer.lower().split("; ")[0])

            for index, letter in enumerate(consonantsHint):
                if letter not in vowels:
                    pass
                elif letter in string.digits:
                    pass
                elif letter in string.punctuation:
                    pass
                elif letter in string.whitespace:
                    pass
                else:
                    consonantsHint[index] = "-"
            print(f"{''.join(consonantsHint).upper()}")
        else:
            vowelsHint = list(self.answer.lower().split("; ")[0])

            for index, letter in enumerate(vowelsHint):
                if letter in vowels:
                    pass
                elif letter in string.digits:
                    pass
                elif letter in string.punctuation:
                    pass
                elif letter in string.whitespace:
                    pass
                else:
                    vowelsHint[index] = "-"
            print(f"{''.join(vowelsHint).upper()}")

    def hangman_hint(self):
        """This method allows the player to play a game of hangman to try and guess their answer! An incorrect letter
        ends the (hangman) game and the player must then guess an answer based on the letters (if any) they got
        correct."""

        import string

        self.hangmanHintsUsed += 1
        self.hangmanHintBool = False

        guessedLetters = []

        hangmanAnswer = list(self.answer.lower().split('; ')[0])
        hangmanPuzzle = list(self.answer.lower().split('; ')[0])

        for index, letter in enumerate(hangmanPuzzle):
            if letter in string.punctuation:
                pass
            elif letter in string.whitespace:
                pass
            elif letter in string.digits:
                hangmanPuzzle[index] = "#"
            else:
                hangmanPuzzle[index] = "_"

        print("\nLet's play HANGMAN! You know how to play Hangman, right?")

        while 1:
            print(f"Guess a letter or a number:"
                  f"\n{' '.join(hangmanPuzzle).upper()}")
            print(f"{', '.join(guessedLetters).upper()}" if len(guessedLetters) > 0 else "NO LETTERS GUESSED")
            playerCharacter = input().lower()

            if playerCharacter == self.answer.lower().split('; ')[0]:
                print(f"ANSWER: {''.join(hangmanAnswer).upper()}")
                print("WELL DONE! +10 \N{Greek Capital Letter Omega} BONUS!")
                self.hangmanGamesWon += 1
                break
            else:
                pass

            guessedLetters.append(playerCharacter)

            if playerCharacter in hangmanAnswer:
                for index, letter in enumerate(hangmanAnswer):
                    if playerCharacter == letter:
                        hangmanPuzzle[index] = playerCharacter
                    else:
                        pass
            else:
                print(f"WRONG! Here's what you managed to get:"
                      f"\n{' '.join(hangmanPuzzle).upper()}")
                break

            if ''.join(hangmanPuzzle).lower() == self.answer.lower().split("; ")[0]:
                print(f"ANSWER: {''.join(hangmanAnswer).upper()}")
                print(f"WELL DONE! +10 \N{Greek Capital Letter Omega} BONUS!")
                self.hangmanGamesWon += 1
                break
            else:
                continue

    def reset_statistics(self):
        """This method resets all of the stats if an exit keyword is used, thereby preparing the stats in case a
        new game is started."""

        self.qAnswered = 0
        self.qNumber = 1
        self.correctAnswers = 0
        self.hintsRemaining = 3
        self.detailedHintsUsed = 0
        self.hangmanHintsUsed = 0
        self.hangmanGamesWon = 0
        self.totalPts = 0
        self.currentStreak = 0
        self.longestStreak = 0
        self.counter5 = 0
        self.counter10 = 0
        self.counter25 = 0
        self.counter50 = 0
        self.counter100 = 0
        self.counter250 = 0
        self.counter500 = 0
        self.counter1000 = 0

        for category in self.categoryDictCorrect and self.categoryDictTotal:
            self.categoryDictCorrect[category] = 0
            self.categoryDictTotal[category] = 0

        self.quiz_menu_categories()


while 1:
    quizMain = Main()
    quizMain.quiz_menu_categories()
