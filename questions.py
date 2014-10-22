import json
import utils

from models.question import Question
from utils import authenticate

class GetQuestions(utils.Handler):
    '''Returns list of up to 20 questions.'''
    # TODO(jabrouwer82): Change this to merge questions by phone number.

    @authenticate
    def get(self):
        query = Question.query()
        list_questions = []
        for question_object in query.fetch(limit=20):
            list_questions.append({'phone_number': question_object.phone_number,
                                   'time': str(question_object.time)})

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
