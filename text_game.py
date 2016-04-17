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

    entered_states_list = []
    second_entr_start_lst = []
    wrong_states_lst = []
    correct_state = True
    letter_flag = True
    already_entered_flag = False
    win = 0

    print 'Interactive game - "US States"'
    print "Official rules: \n" \
          "1. The goal of the game is checking your knowledge of US state names.\n" \
          "2. Fisrt of all, you enter name of US state. \n" \
          "Then enter name of US state where first letter is the last letter of previous successfully entered name of US state.\n" \
          "3. You have only one possibility to make mistake.\n" \
          "4. You can\'t repeat name of US states. One mistake allowed\n" \
          "5. Each successfully entered name of US state is 10 points to your score.\n" \
          "6. Every 50 points brings you double points to your score.\n" \
          "7. If you enter wrong name of US state your game is over.\n" \
          "8. If your first letter of US state name does not meet the last letter of the previous name of US state your game is over. One mistake allowed\n" \
          "9. You win in case when you guess all US state."

    def check_state(self, new_state, last_symbol_prev_us_state):
        if new_state in self.second_entr_start_lst:
            
            # when we already entered that state twice
            check = self.check_states_with_letter(last_symbol_prev_us_state)
            if check:
                print 'You have already chosen this state twice. \n Game Over! \n Your score is - %r' % self.win
                self.correct_state = False
            else:
                print 'You already entered all US states which start with letter - \'%s\'' % last_symbol_prev_us_state
                new_state = self.already_entered_state(new_state)

        elif new_state in self.entered_states_list:
            
            # when we already entered that state
            print'You have already chosen this state.'
            self.second_entr_start_lst.append(new_state)
            check = self.check_states_with_letter(last_symbol_prev_us_state)
            if check:
                new_state = raw_input(
                    "Please enter correct state which is start with letter \'%s\'. It\'s your last chance - " % last_symbol_prev_us_state).lower()
                self.check_state(new_state, last_symbol_prev_us_state)
            else:
                print 'You already entered all US states which start with letter - \'%s\'' % last_symbol_prev_us_state
                new_state = self.already_entered_state(new_state)

        elif last_symbol_prev_us_state:
            
            # check last symbol of state name
            if new_state[0].lower() != last_symbol_prev_us_state:
                if new_state not in self.states_list:
                    print 'No way! It\'s incorrect name of US states. \n Game Over! \n Your score is - %r' % self.win
                    self.correct_state = False
                elif not self.letter_flag:
                    print 'You should to enter US state which is start with letter \'%s\'. ' \
                          '\n Game Over! \n Your score is - %r' % (last_symbol_prev_us_state, self.win)
                    self.correct_state = False
                else:
                    print 'You should enter name of US state which is start with letter \'%s\'' % last_symbol_prev_us_state
                    self.wrong_states_lst.append(new_state)
                    new_state = raw_input(
                        "Please enter correct state which is start with letter \'%s\'. It\'s your last chance - " % last_symbol_prev_us_state).lower()
                    self.letter_flag = False
                    self.check_state(new_state, last_symbol_prev_us_state)

            elif new_state in self.states_list and new_state not in self.entered_states_list:
                self.win += 10
                self.entered_states_list.append(new_state)
                print 'Great! It\'s correct name of US states. \n Your score is - %r' % self.win
                self.get_your_win()

            else:
                print 'No way! It\'s incorrect name of US states. \n Game Over! \n Your score is - %r' % self.win
                self.correct_state = False

        elif new_state in self.states_list and new_state not in self.entered_states_list:
            
            # correct state, not entered yet
            self.win += 10
            self.entered_states_list.append(new_state)
            print 'Great! It\'s correct name of US states. \n Your score is - %r' % self.win
            self.get_your_win()

        else:
            
            # inccorect state
            print 'No way! It\'s incorrect name of US states'
            new_state = raw_input(
                "You have one more chance to enter correct name of US states. \nPlease, enter new correct US state - ").lower()
            if new_state in self.states_list and new_state not in self.entered_states_list:
                self.win += 10
                self.entered_states_list.append(new_state)
                print 'Great! It\'s correct name of US states.\n Your score is - %r' % self.win
                self.get_your_win()

            else:
                print 'No way! It\'s incorrect name of US states. \n Game Over! \n Your score is - %r' % self.win
                self.correct_state = False
        return new_state
    
    # when already entered state twice or ones
    def already_entered_state(self, new_state):
        if self.check_full_success() is True:
            print 'Congratulations! You Win!.\n Your score is - %r' % self.win
            self.correct_state = False
        if self.already_entered_flag:
            print 'You should entered correct state which is not entered yet ' \
                    '\n Game Over! \n Your score is - %r' % self.win
            self.correct_state = False
        new_state = raw_input(
            "Please enter correct state which is not entered yet. - ").lower()
        self.already_entered_flag = True
                
        if new_state in self.states_list and new_state not in self.entered_states_list:
            self.check_state(new_state, None)
        elif new_state in self.states_list:
            self.check_state(new_state, new_state[0])
        else:
            print 'Wrong state. \n Game Over! \n Your score is - %r' % self.win
            self.correct_state = False
        return new_state 

    # to get new score value
    def get_your_win(self):
        if self.win % 50 == 0:
            self.win = self.win + 50
            print 'Now Your score is doubling - %r' % self.win
        self.correct_state = True
        if self.check_full_success() is True:
            print 'Congratulations! You Win!.\n Your score is - %r' % self.win
            self.correct_state = False 

    # to find last correct letter in tne name of US states
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

    # case when we doesn't have another name of state with the same first letter
    def check_states_with_letter(self, last_symbol):
        check = False
        for state in self.states_list:
            if state[0] != last_symbol:
                continue
            elif state not in self.entered_states_list:
                check = True
                break
            else:
                continue
        return check

    # check if you guess all US states
    def check_full_success(self):
        for state in self.states_list:
            if state not in self.entered_states_list:
                return False
        return True

    # start our interactive game
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
