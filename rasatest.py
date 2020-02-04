import os
import json
import copy
import pprint
from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_nlu.model import Interpreter
from rasa_nlu.test import run_evaluation

class RaSaEngine():

    def __init__(self):
        self.training_file = "C:/Users/Harpreet/rasaproject/SmallTalkdata/data/nlu.md"
        self.config_file = "C:/Users/Harpreet/rasaproject/SmallTalk/config.yml"
        self.model_directory = "C:/Users/Harpreet/rasaproject/SmallTalk/models"
        self.interpreter = None

    def train_nlu(self, data_path, configs, model_path):

        training_data = load_data(data_path)
        trainer = Trainer(config.load(configs))
        trainer.train(training_data)
        model_directory = trainer.persist(model_path, project_name='rasaproject', fixed_model_name='SmallTalk')
        run_evaluation(data_path, model_directory)

    def load_interpreter(self, nlu_path):
        self.interpreter = Interpreter.load(nlu_path)

    def run_nlu(self, query):
        # interpreter = Interpreter.load(nlu_path)
        return self.interpreter.parse(query)
        # pprint.pprint(interpreter.parse("What is going on in technology?"))
        # pprint.pprint(interpreter.parse("What is going on in education?"))

    def read_json(self, file_path):
        with open(file_path) as json_file:
            data = json.load(json_file)
            return data

    def write_json(self,file_path, payload):
        with open(file_path, 'w') as outfile:
            json.dump(payload, outfile, indent=2)

    def write_md(self, file_path, payload):
        with open(file_path, 'w') as f:
            for item in payload:
                f.write("%s\n" % item)

if __name__ == '__main__':
    rasa = RaSaEngine()
    # rasa.train_nlu(rasa.training_file, rasa.config_file, rasa.model_directory)
    model_path = "C:/Users/Harpreet/rasaproject/SmallTalk"
    rasa.load_interpreter(model_path)
    print("Input:")
    q = input()
    while(q):
        response = rasa.run_nlu(q)
        print(json.dumps(response.get('intent'), indent=2))
        print("Input: ")
        q= input()