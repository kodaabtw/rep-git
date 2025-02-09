import os
import pickle

availableClasses = {
    "dummyClassifier": ["strategy", "constant"],
    "dummyRegressor": ["strategy"]
}

class ModelsManager:
    models = {}

    def init(self):
        self.models_folder = "storage"
        if not os.path.exists(self.models_folder):
            os.makedirs(self.models_folder)
        self.models = {}
        
    def save(self, name, model):
        model_path = os.path.join(self.models_folder, f"{name}.pkl")
        with open(model_path, "wb") as f:
            pickle.dump(model, f)
        self.models[name] = {"model": model}
    
    def load(self, name):
        model_path = os.path.join(self.models_folder, f"{name}.pkl")
        with open(model_path, "rb") as f:
            model = pickle.load(f)
        loadedModels[name] = model
        return model
    
    def load_all(self):
        for model_name in os.listdir(self.models_folder):
            model_name = model_name.split(".")[0]
            self.load(model_name)
    
    def getTrainedModels(self):
        return list(self.models.keys())
