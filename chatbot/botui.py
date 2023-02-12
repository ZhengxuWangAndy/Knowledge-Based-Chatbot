
import os
import sys
import tensorflow as tf
import nltk

sys.path.append(os.pardir)

from settings import PROJECT_ROOT
from chatbot.botpredictor import BotPredictor

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

def bot_ui():
    corp_dir = os.path.join(PROJECT_ROOT, 'Data', 'Corpus')
    knbs_dir = os.path.join(PROJECT_ROOT, 'Data', 'KnowledgeBase')
    res_dir = os.path.join(PROJECT_ROOT, 'Data', 'Result_med')

    with tf.Session() as sess:
        predictor = BotPredictor(sess, corpus_dir=corp_dir, knbase_dir=knbs_dir,
                                 result_dir=res_dir, result_file='basic-101880')
        # This command UI has a single chat session only
        session_id = predictor.session_data.add_session()

        print("Welcome to Chat with ChatLearner!")
        print("===Made by 朱文钊、王正旭、徐聪宇、黄远===")
        print("Type exit and press enter to end the conversation.")
        # Waiting from standard input.
        sys.stdout.write("> ")
        sys.stdout.flush()
        question = sys.stdin.readline()
        while question:
            if question.strip() == 'exit':
                print("Thank you for using ChatLearner. Goodbye.")
                break

            print(predictor.predict(session_id, question))
            print("> ", end="")
            sys.stdout.flush()
            question = sys.stdin.readline()

if __name__ == "__main__":
    bot_ui()
