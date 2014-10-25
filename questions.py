import itertools
import json
import utils

from datetime import datetime
from models.question import Question
from utils import authenticate


class GetQuestions(utils.Handler):
    '''Returns list of up to 20 questions.'''

    @authenticate
    def get(self):
        query = Question.query()
        query.order(Question.phone_number)
        list_questions = []
        dict_questions = {}

        # This is nasty and I like the old itertools way better (commit
        # 3d48b788384b530b279443bb115e51180f3a9165), but it didn't do
        # the grouping correctly, so this will have to do until someone
        # decides to look into what the old way did wrong.
        for question in query.fetch():
            entry = dict_questions.get(question.phone_number, {})
            entry['count'] = entry.get('count', 0) + 1
            if (not question.time is None
                  and question.time > entry.get('most_recent', datetime.min)):
                entry['most_recent'] = question.time
            dict_questions[question.phone_number] = entry

        for phone_number, entry in dict_questions.iteritems():
            most_recent = str(entry['most_recent'])
            count = entry['count']
            list_questions.append({'phone_number': phone_number,
                                   'last_call_date': str(most_recent),
                                   'number_of_questions': count
                                  })
            
        
        output = json.dumps(list_questions)
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
