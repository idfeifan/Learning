# coding=utf-8
import unittest
from Python从入门到实践.测试类.survey import AnonymousSurvey


class TestAnonmyousSurvey(unittest.TestCase):
    '''针对AnonymousSurvey类的测试'''

    def test_store_single_response(self):
        '''测试单个答案会被妥善地存储'''
        question = 'What language did you first learn to speak ?'
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')

        self.assertIn('English',my_survey.responses)
if __name__ == '__main__':
    unittest.main()