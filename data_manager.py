import connection

question = "./static/question.csv"
answer = "./static/answer.csv"


def question_list():
    table = connection.get_table_from_file(question)
    table.remove(table[0])
    table.reverse()
    return table


def answer_list():
    table = connection.get_table_from_file(answer)
    return table


def save_question(saved_question):
    write = []
    table = connection.get_table_from_file(question)
    write.append(int(table[len(table)-1][0])+1)
    for i in range(3):
        write.append("WOP")
    write.append(saved_question[0])
    write.append(saved_question[1])
    connection.write_table_to_file(question, write)


def save_answer(saved_answer):
    write = []
    table = connection.get_table_from_file(answer)
    write.append(int(table[len(table)-1][0])+1)
    for i in range(2):
        write.append("WOP")
    write.append()
    write.append(saved_answer[0])
    connection.write_table_to_file(answer, write)
