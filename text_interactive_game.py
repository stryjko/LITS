
_author_ = 'maryan_partyka'

class TextInteractiveGame:
    states_list = ['alabama', 'alaska', 'arizona', 'arkansas', 'california', 'colorado', 'connecticut',
              'delaware', 'florida', 'georgia', 'hawaii', 'idaho', 'illinois', 'indiana', 'iowa', 'kansas',
              'kentucky', 'louisiana', 'maine', 'maryland', 'massachusetts', 'michigan', 'minnesota', 'mississippi',
              'missouri', 'montana', 'nebraska', 'nevada', 'new hampshire', 'new jersey', 'new mexico',
              'new york', 'north carolina', 'north dakota', 'ohio', 'oklahoma', 'oregon', 'pennsylvania',
              'rhode island', 'south carolina', 'south dakota', 'tennessee', 'texas', 'utah', 'vermont',
              'virginia', 'washington', 'west virginia', 'wisconsin', 'wyoming']
    first_letter_list = ['a', 'c', 'd', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'w']
    correct_state = True
    entered_states_list = []
    second_entr_start_lst = []
    win = 0

    print 'Interactive game - "US States"'
    print "Official rules: \n" \
          "1. The goal of the game is checking your knowledge of US state names.\n" \
          "2. Fisrt of all, you enter name of US state. \n" \
          "Then enter name of US state where first letter is the last letter of previous successfully entered name of US state.\n" \
          "3. You have only one possibility to make mistake on the start of the game.\n" \
          "4. You can\'t repeat name of US states.\n" \
          "5. Each successfully entered name of US state is 10 points to your score.\n" \
          "6. If you enter wrong name of US state your game is over.\n" \
          "7. If your first letter of US state name does not meet the last letter of the previous name of US state your game is over."


    def check_state(self, new_state, last_symbol_prev_us_state):
        if new_state in self.second_entr_start_lst:
            print 'You have already chosen this state twice. \n Game Over! \n Your score is - %r' % self.win
            self.correct_state = False
        elif new_state in self.entered_states_list:
            print'You have already chosen this state.' 
            self.second_entr_start_lst.append(new_state)
            new_state = raw_input(
                "Please enter correct state which is start with letter \'%s\'. It\'s your last chance - " % last_symbol_prev_us_state).lower()
            if new_state[0].lower() != last_symbol_prev_us_state:
                print 'You had to enter enter name of US state which is start with letter \'%s\'' % last_symbol_prev_us_state 
                print 'You have broken rules of the game. \n Game Over! \n Your score is - %r' % self.win
                self.correct_state = False
            elif new_state in self.states_list and new_state not in self.entered_states_list:
                self.win += 10
                self.entered_states_list.append(new_state)
                print 'Great! It\'s correct name of US states. \n Your score is - %r' % self.win
                self.correct_state = True
            elif new_state in self.entered_states_list:
                print 'You have already chosen this state. \n Game Over! \n Your score is - %r' % self.win
                self.correct_state = False
            else:
                print 'No way! It\'s incorrect name of US states. \n Game Over! \n Your score is - %r' % self.win
                self.correct_state = False
        elif last_symbol_prev_us_state:
            if new_state[0].lower() != last_symbol_prev_us_state:
                print 'You should enter name of US state which is start with letter \'%s\'' % last_symbol_prev_us_state 
                new_state = raw_input(
                    "Please enter correct state which is start with letter \'%s\'. It\'s your last chance - " % last_symbol_prev_us_state).lower()
                if new_state[0].lower() != last_symbol_prev_us_state:
                    print 'You had to enter enter name of US state which is start with letter \'%s\'' % last_symbol_prev_us_state 
                    print 'You have broken rules of the game. \n Game Over! \n Your score is - %r' % self.win
                    self.correct_state = False
                elif new_state in self.states_list and new_state not in self.entered_states_list:
                    self.win += 10
                    self.entered_states_list.append(new_state)
                    print 'Great! It\'s correct name of US states. \n Your score is - %r' % self.win
                    self.correct_state = True
                elif new_state in self.entered_states_list:
                    print 'You have already chosen this state. \n Game Over! \n Your score is - %r' % self.win
                    self.correct_state = False
                else:
                    print 'No way! It\'s incorrect name of US states. \n Game Over! \n Your score is - %r' % self.win
                    self.correct_state = False

            elif new_state in self.states_list and new_state not in self.entered_states_list:
                self.win += 10
                self.entered_states_list.append(new_state)
                print 'Great! It\'s correct name of US states. \n Your score is - %r' % self.win
                self.correct_state = True
            else:
                print 'No way! It\'s incorrect name of US states. \n Game Over! \n Your score is - %r' % self.win
                self.correct_state = False

        elif new_state in self.states_list and new_state not in self.entered_states_list:
            self.win += 10
            self.entered_states_list.append(new_state)
            print 'Great! It\'s correct name of US states. \n Your score is - %r' % self.win
            self.correct_state = True
        else:
            print 'No way! It\'s incorrect name of US states'
            new_state = raw_input(
                "You have one more chance to enter correct name of US states. \nPlease, enter new correct US state - ").lower()
            if new_state in self.states_list and new_state not in self.entered_states_list:
                self.win += 10
                self.entered_states_list.append(new_state)
                print 'Great! It\'s correct name of US states.\n Your score is - %r' % self.win
                self.correct_state = True
            else:
                print 'No way! It\'s incorrect name of US states. \n Game Over! \n Your score is - %r' % self.win
                self.correct_state = False
        return new_state


    def find_last_symbol(self, new_state):
        letter = None
        all_letter = [ch for ch in new_state]
        for i in range(len(all_letter)-1, 0, -1):
            if all_letter[i] not in self.first_letter_list:
                print "There is no exist name of US states which start with letter  - %s" % all_letter[i]
                continue
            else:
                letter = all_letter[i]
                break
        return letter

    def start_game(self):
        
        # start game, type first US state name
        new_state = raw_input("\nPlease, enter some US state - ").lower()

        # checking US states and your win score
        new_state = self.check_state(new_state, None)

        while self.correct_state:
            last_symbol = new_state[-1:]
            if last_symbol in self.first_letter_list:
                print "Great! Now, please enter new US state, which start with letter \'%s\' - " % last_symbol
            else:
                last_symbol = self.find_last_symbol(new_state)
                if last_symbol:
                    print "Now, please enter new US state, which start with symbol \'%s\' - " % last_symbol
                else:
                    print "There is no another name of US states which start with letters in word - %s" % new_state
                    print "Game Over! \n Your score is - %r" % self.win
                    break
            new_state = raw_input().lower()
            new_state = self.check_state(new_state, last_symbol)

TextInteractiveGame().start_game()
