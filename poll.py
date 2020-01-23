# poll.py 

if __name__ == "__main__":
    # functions
    def command_input():
        text = "Enter selected command: show polls, create poll, quit: "
        user_in = input(text)
        return user_in

    # procedure
    polls = [
        {
            'question':'Example poll',
            'answers': [
                'Answer 1',
                'Answer 2'
            ]
        }
    ]
    user_in = command_input()
    
    while user_in != 'quit':
        if user_in == 'create poll':
            # create new poll 
            question = input("# Creating new poll\nEnter new poll question:\n") 

            new_poll = {
                'question': question,
                'answers': []
            }

            while(True):
                possible_answer = input("# Add available answer no. " 
                                        + str(len(new_poll['answers']) + 1) 
                                        + " \n( enter 'stop' to quit creating answers ):")
                if possible_answer == 'stop':
                    break
                # append the answer
                new_poll['answers'].append(possible_answer)
            # append the poll
            polls.append(new_poll)

        elif user_in == 'show polls':
            p = 1
            for poll in polls:
                print(str(p) + " poll: " + poll['question'])
                print("Available (" + str(len(poll['answers'])) + ") answers:")
                
                # show answers
                i = 1
                for ans in poll['answers']:
                    print("\t" + str(i) + ". " + ans)
                    i += 1;

                p += 1

        else:
            # command unknown
            print("Command unknown!")
        
        # show the input again
        user_in = command_input()

    print("Have a nice day!")
