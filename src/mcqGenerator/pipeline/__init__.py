from mcqGenerator.components.quiz_generator import QuizGeneratorEvaluator

def initialization_of_quiz():
    quiz_generate = QuizGeneratorEvaluator()

    quize_table = quiz_generate.generating_mcq()

    return quize_table

