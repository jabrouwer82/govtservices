import itertools
import json
import utils

from datetime import datetime
from models.stats import Stats
from utils import authenticate


class GetQuestions(utils.Handler):
    '''Returns list of up to 20 questions.'''

    @authenticate
    def get(self):
        query = Stats.query()
        stats = []
        
        for stat in query.fetch():
            stats.append({'phone_number': stat.phone_number,
                          'last_call_date': str(stat.most_recent_question),
                          'number_of_questions': stat.number_of_questions
                         })
            
        
        output = json.dumps(stats)
        self.render_json(output)


class GetQuestionsForPhoneNumber(utils.Handler):
    '''Returns list of up to 20 questions for the given phone number.'''

    @authenticate
    def get(self):
        phone_number = int(self.request.get('p'))
        query = Question.query()
        query = query.filter(Question.phone_number == phone_number)
        
        questions = []
        most_recent = datetime.min
        count = 0
        
        for question in query.fetch():
            count += 1
            if not question.time is None and question.time > most_recent:
                most_recent = question.time
            questions.append({'question': question.question,
                              'time': str(question.time),
                              'answer': question.answer})
        response = {'questions': questions,
                    'phone_number': phone_number,
                    'number_of_questions': count,
                    'most_recent_question': str(most_recent)}
        output = json.dumps(response)
        self.render_json(output)
