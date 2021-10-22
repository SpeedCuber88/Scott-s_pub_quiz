# Scott-s_pub_quiz
A repository for the development of my pub quiz program.

This repository contains the most up-to-date version of the quiz, Scott's Pub Quiz.

GAME MODES
There are two different game modes that can be selected that control for the content of the quiz:
- All categories (you're asked questions from any and all categories), and;
- Pick a topic (you choose a SINGLE category on which to answer questions).

There are two different game modes that can be selected that control for the length of the quiz:
- The infinite quiz (the program keeps asking you randomly-selected questions until you submit 'exit' in the answer field), and;
- Pick a length (you choose how many questions you want to answer and the quiz ends brings you to the main menu once all the questions have been asked).

ANSWER VERIFICATION
The code has been written in such a way that tries to account for different spellings (e.g. 'Stewart'/'Stuart'), alternate (and acceptable) answers (e.g. 'Edward I'/'Edward Longshanks'), permutations of answers (e.g. 'Venus and Uranus'/'Uranus and Venus'), partial answers (e.g. 'Pablo Picasso'/'Picasso'), use of digits or words for numbers (e.g. '1'/'one') and other issues surrounding answer submission.  This was done to remove the necessity for players to remember exact acceptable answers and generally improve playability of the quiz.

KEYWORDS
Keywords for different kinds of hints, different kinds of player stats and other quiz functions are typed directly into the answer submission field.  The code accounts for these keywords and does not mark them as incorrect answers to whichever question has been selected.
Explaining the individual ingame functions would ruin the game, so the player can type the keyword 'commandlist' to get a list of keywords.
