import os


def hello(event, context):
    TEST_ENV = os.environ.get('TEST_ENV')
    return TEST_ENV
