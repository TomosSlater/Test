class FizzBuzzOutput:
    def __init__(self, num):
        self.num = num
        self.output = ''

    def apply_fizz(self):
        if self.num % 3 == 0:
            self.output += 'Fizz'

    def apply_buzz(self):
        if self.num % 5 == 0:
            self.output += 'Buzz'

    def apply_bang(self):
        if self.num % 7 == 0:
            self.output += 'Bang'

    def apply_bong(self, is_fezz_included = False):
        is_fezz = is_fezz_included and self.num % 13 == 0
        if self.num % 11 == 0:
            if is_fezz:
                self.output = 'FezzBong'
            else:
                self.output = 'Bong'

    def apply_fezz(self):
        if self.num % 13 == 0:
            self.output += 'Fezz'

    # helper function for apply_reverse
    def get_word_from_output(self, word_index):
        start_index = word_index * 4
        return self.output[start_index:start_index + 4]

    # here, we make the assumption that all words are 4 characters
    def apply_reverse(self):
        if self.num % 17 == 0 and self.output != '':
            number_of_words_left = round(len(self.output) / 4)
            new_output = ''

            while number_of_words_left >= 0:
                new_output += self.get_word_from_output(number_of_words_left)
                number_of_words_left -= 1

            self.output = new_output

    def get_final_output(self):
        if self.output == '':
            self.output = str(self.num)
        return self.output

class FizzBuzzBangEtc:
    
    def __init__(self, use_custom_rules = False):
        self.max_num = self.ask_max_num_question()

        if (use_custom_rules):
            self.apply_rule_3 = self.ask_yes_or_no_answer_question('Include rule 3 (replace number with Fizz if divisible by 3)? > ')
            self.apply_rule_5 = self.ask_yes_or_no_answer_question('Include rule 5 (replace number with Buzz if divisible by 5 - Appended to Fizz if applicable)? > ')
            self.apply_rule_7 = self.ask_yes_or_no_answer_question('Include rule 7 (replace number with Bang if divisible by 7 - Appended to Fizz / Buzz if applicable)? > ')
            self.apply_rule_11 = self.ask_yes_or_no_answer_question('Include rule 11 (replace everything with Bong if divisible by 11)? > ')
            self.apply_rule_13 = self.ask_yes_or_no_answer_question('Include rule 13 (replace number with Fezz if divisible by 13 - Inserted after Fizz if applicable, and is shown even if Bong is present)? > ')
            self.apply_rule_17 = self.ask_yes_or_no_answer_question('Include rule 17 (Reverse all words if divisible by 17)? > ')

    
    def ask_max_num_question(self):
        while(True):
            try:
                max_num = int(input('Please input maximum number > '))
                break
            except ValueError:
                print('\nInvalid value entered...')
        return max_num 

    def ask_yes_or_no_answer_question(self, question):
        print('\n')
        while True:
            answer = input(question).lower()
            if answer == 'yes':
                return True
            elif answer == 'no':
                return False
            else:
                print('\nInput \'Yes\' or \'No\' only, please...')

    def fizz_buzz(self):
        for i in range(1, self.max_num):
            output = FizzBuzzOutput(i)

            output.apply_fizz()
            output.apply_buzz()

            print(output.get_final_output())

    def fizz_buzz_bang(self):
        for i in range(1, self.max_num + 1):
            output = FizzBuzzOutput(i)

            output.apply_fizz()
            output.apply_buzz()
            output.apply_bang()

            print(output.get_final_output())

    def fizz_buzz_bang_bong(self):
        for i in range(1, self.max_num + 1):
            output = FizzBuzzOutput(i)

            output.apply_fizz()
            output.apply_buzz()
            output.apply_bang()
            output.apply_bong()

            print(output.get_final_output())

    def fizz_buzz_bang_bong_fezz(self):
        for i in range(1, self.max_num + 1):
            output = FizzBuzzOutput(i)

            output.apply_fizz()
            output.apply_fezz()
            output.apply_buzz()
            output.apply_bang(True)
            output.apply_bong()

            print(output.get_final_output())

    def fizz_buzz_bang_bong_fezz_reverse(self):
        for i in range(1, self.max_num + 1):
            output = FizzBuzzOutput(i)

            output.apply_fizz()
            output.apply_fezz()
            output.apply_buzz()
            output.apply_bang()
            output.apply_bong(True)
            output.apply_reverse()

            print(output.get_final_output())

    def custom_fizz_buzz(self):
        for i in range(1, self.max_num + 1):
            output = FizzBuzzOutput(i)

            if self.apply_rule_3:
                output.apply_fizz()
            if self.apply_rule_13:
                output.apply_fezz()
            if self.apply_rule_5:
                output.apply_buzz()
            if self.apply_rule_7:
                output.apply_bang()
            if self.apply_rule_11:
                if self.apply_rule_13:
                    output.apply_bong(True)
                else: 
                    output.apply_bong()
            if self.apply_rule_17:
                output.apply_reverse()

            print(output.get_final_output())

fizzBuzzBangEtc = FizzBuzzBangEtc(True)
fizzBuzzBangEtc.custom_fizz_buzz()

