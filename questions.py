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

        def group_by_phone_number(value):
            return value.phone_number

        for phone_number, questions in itertools.groupby(query.fetch(limit=40),
                                                 group_by_phone_number):
            most_recent = datetime.min
            count = 0
            for question in questions:
                count += 1
                if not question.time is None and question.time > most_recent:
                    most_recent = question.time
            
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
        list_questions = []
        for question_object in query.fetch(limit=20):
            list_questions.append({'question': question_object.question,
                                   'time': str(question_object.time),
                                   'answer': question_object.answer})

        output = json.dumps(list_questions)
        self.render_json(output)
