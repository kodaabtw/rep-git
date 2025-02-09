from flask import Flask
from flask_restx import Api, Resource, fields, reqparse
from sklearn.dummy import DummyClassifier
import numpy as np
from werkzeug.datastructures import FileStorage
from api import modelsManager
app = Flask("ML-OPS")
api = Api(app)
manager = modelsManager.ModelsManager()

# /getAvailableModels
get_ready_to_train_models_parser = reqparse.RequestParser()

# /train
train_parser = reqparse.RequestParser()
train_parser.add_argument('parameters', type=dict, location='application/json', required=True, help="No json")
train_parser.add_argument('data', type=dict, location='application/json', required=True, help="No data")

# /getTrainedModelsList
get_trained_models_list_parser = reqparse.RequestParser()

# /predict
predictParser = reqparse.RequestParser()
predictParser.add_argument('input', type=dict, location='json')
predictParser.add_argument('model', type=str, location='json')

# /deleteModel
deleteModelParser = reqparse.RequestParser()
deleteModelParser.add_argument('input', type=dict, location='json')
deleteModelParser.add_argument('model', type=str, location='json')

# Create a resource class for the /getReadyToTrainModels endpoint
class GetReadyToTrainModelsResource(Resource):
    @api.expect(get_ready_to_train_models_parser)
    def get(self):
        return availableClasses, 200

# Create a resource class for the /getTrainedModelsList endpoint
class GetTrainedModelsListResource(Resource):
    @api.expect(get_trained_models_list_parser)
    def get(self):
        return manager.getTrainedModels(), 200

# Create a resource class for the /train/<modelName> endpoint
class TrainResource(Resource):
    @api.expect(train_parser)
    def post(self, modelName):
        # Check if the model is invalid
        input_data = train_parser.parse_args()['data']
        if modelName not in trainedModels.keys():
            return f"{input_data} не найдена в списке обученных моделей", 404


        # Get the model from the trained models list
        model = trainedModels[modelName]

        # Predict using the model
        prediction = model.predict(data)

        return prediction, 200

class PredictResource(Resource):
    @api.expect(predictParser)
    def post(self):
        # Get the input and model parameters from the request
        model = predict_parser.parse_args()['model']

        # Check if the model is invalid
        if model not in trainedModels:
            return f"{model} не найдена в списке обученных моделей", 404

        # Get the model from the trained models list
        model = next(m for m in trainedModels if m.name == model)

        # Predict using the model
        prediction = model.predict(input_data)

        return prediction, 200

# Create a resource class for the /deleteModel endpoint
class DeleteResource(Resource):
    @api.expect(deleteModelParser)
    def post(self):
        # Get the input and model parameters from the request
        input_data = deleteModelParser.parse_args()['input']
        model = deleteModelParser.parse_args()['model']

        # Check if the model is invalid
        if model not in trainedModels:
            return f"{model} не найдена в списке обученных моделей", 404

        # Remove the model from the trained models list
        trainedModels.remove(next(m for m in trainedModels if m.name == model))

        return f"Модель {model} удалена", 200

#Add the resource classes to the API
api.add_resource(GetReadyToTrainModelsResource, '/getReadyToTrainModels')
api.add_resource(GetTrainedModelsListResource, '/getTrainedModelsList')
api.add_resource(TrainResource, '/train/<modelName>')
api.add_resource(PredictResource, '/predict')
api.add_resource(DeleteResource, '/deleteModel')

def trainDummy():
    dummy_clf = DummyClassifier(strategy="most_frequent")
    dummy_clf.fit(X, y)
    trainedModels.append(dummy_clf)