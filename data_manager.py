from connection import *

question = "./static/question.csv"
answer = "./static/answer.csv"


def question_list():
    table = get_table_from_file(question)
    table.remove(table[0])
    table.reverse()
    return table


def answer_list():
    table = get_table_from_file(answer)
    return table
