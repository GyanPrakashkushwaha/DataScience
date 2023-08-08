import re
import random


class baseBot:
    # negative responses
    negative_responses = ('no','nope','nah','naw','not a chance','sorry')

    # Exit conversation keywords
    exit_responses = ('quit','pause','exit','goodbye','bye','later')

    # random starter questions
    random_questions = (
        'why are you here? ',
        'are there many humans like you? ',
        'How do I learn NLP explain me in detail. ',
        'Is there intelligent life on this planet?',
        'does dearth have a leader?' ,
        'what planets have you visited?' ,
        'what technology do you have on this planet? '
    )


    def __init__(self):
        self.alien = {
            'describe_planet_intent':r'.*\syou planet.*',
            'answer_why_intent':r'why\sare.*',
            'about_me':r'.*\s*me'
        }

    
    def greet(self):
        self.name = input('what is your name?\n')
        will_help = input(
            f'Hi {self.name}, I am a baseBot. will you help me to learn about NLP? \n'
        )

        if will_help in self.negative_responses:
            print('ok , Happly learning')
            return
        self.chat()

    
    def make_exit(self , reply):
        for i in self.exit_responses:
            if reply == i:
                print('okk , Happly learning')
                return True
            
        
    def chat(self):
        reply = input(random.choice(self.random_questions)).lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply))

    
    def match_reply(self , reply):
        for key , value in self.alien.items():
            intent = key
            regex_pattern = value
            found_match = re.match(regex_pattern,reply)
            if found_match and intent == 'describe_planet_intent':
                return self.describe_planet_intent()
            elif found_match and intent == 'answer_why_intent':
                return self.answer_why_intent()
            elif found_match and intent == 'about_me':
                return self.about_me()
                
            if not found_match:
                return self.not_match()
        
    
    def describe_planet_intent(self):
        responses = ('my planet is a utopia of diverse organisms and species.\n',
                     'I am from ospidipus , the capital of the warward galaxies.\n')
        return random.choice(responses)
    
    def answer_why_intent(self):
        resp = ('I come in  peace \n ',
                'i am here to collect data on your planet and its inhabitants \n',
                'i heard the coffee is good\n')
        return random.choice(resp)
    
    def about_me(self):
        resp = ('I am Gyan Prakash Kushwaha\n',
                'Gyan Prakash Kushwaha is a Data Scientist.')
    
    def not_match(self):
        resp = (
            'please tell me more.\n',
            'tell me more\n',
            'why do you say that?\n',
            'I see. can you elaborate?\n'
            'Interesting can you tell me more?\n',
            'I see. how do think?\n',
            'why\n')
        return random.choice(resp)
   

bot = baseBot()
print(bot.greet())