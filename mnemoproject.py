import random




# The peg list I have from my old mnemotrainer attempt. Eventually I will write something that creates this list from a CSV
pegs = ["saw", "di", "wine", "Mao", "oar", "awl", "wedge", "key", "ivy", "pie", "hides", "toad", "dune", "dome", "otter", "dill", "ditch", "tick", "taffy", "type", "noose", "knot", "onion", "gnome", "Nero", "nail", "hinge", "ink", "knife", "knob", "mouse", "meat", "money", "mom", "mario", "mule", "match", "mug", "mafia", "map", "rose", "heart", "rhino", "ram", "arthur", "railway", "roach", "wreck", "wharf", "rope", "Eliza", "Walt", "lion", "lamb", "lure", "lily", "leech", "lock", "elf", "lube", "Joyce", "cheetah", "chain", "gem", "chair", "shell", "judge", "Jake", "chef", "jeep", "cows", "Quijote", "canoe", "comb", "choir", "eagle", "couch", "cock", "coffee", "cowboy", "vise", "fat", "oven", "foam", "ferry", "file", "fish", "fig", "fife", "VP", "bus", "bat", "bone", "puma", "bear", "bell", "peach", "bike", "pave", "pipe"]

results_file = open("output.txt", "r+")
quiz_numbers = []
quiz_pegs = []
quiz_answers = []
keep_playing = True

def get_number_quiz():
    """Create a quiz of length input by user."""
    quiz_numbers[:] = []
    quiz_answers[:] = []
    # Ask for how many terms to test. Write this as a function eventually
    number_of_pegs = int(input('How many terms do you want to train? '))
    # Add one random number to quiz_numbers for number_of_pegs
    for x in range(0, number_of_pegs):
        quiz_numbers.append(random.randint(0,99))
    # Get the correct answers for the pegs
    for x in quiz_numbers:
        quiz_pegs.append(pegs[x])
    print(quiz_numbers)
    for x in quiz_numbers:
        quiz_answers.append(input('What do you associate with {}? '.format(x)))

def check_answers(numbers, answers, peg_list):
    """Checks answers to peg list quiz."""
    i = 0
    num_right = 0
    num_wrong = 0
    # Iterates through numbers list, using its values as index of peg_list.
    # This is compared to provided answers from user raw input. Score is tallied. 
    for x in numbers:
        if peg_list[x] == answers[i]:
            print('Your answer for {} is correct: {}.'.format(x, answers[i]))
            i += 1
            num_right += 1
        else:
            print('Your answer for {} is incorrect: {}. The correct answer is: {}.'.format(x, answers[i], pegs[x]))
            i += 1
            num_wrong += 1
    results = 'You got {} numbers right and {} numbers wrong.'.format(num_right, num_wrong)
    results_file.write(results + '\n')
    print(results)

    

print('This script trains the MASTER TECHNIQUE memory system.')

while keep_playing:
    get_number_quiz()
    check_answers(quiz_numbers, quiz_answers, pegs)
    keep_playing_prompt = input('Play again? Y/N? ')
    if keep_playing_prompt != 'Y':
        keep_playing = False

results_file.close()

