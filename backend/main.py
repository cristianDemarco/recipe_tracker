from flask import Flask
from flask_restx import Api, Resource, fields
from config import DevConfig
from models import Recipe
from exts import db

app = Flask(__name__)
app.config.from_object(DevConfig)

db.init_app(app)

api = Api(app, doc='/docs')

# Model Serializer

"""
Serialiazing refers to the process of converting a model object
or data structure into a format that can be easily rendered into JSON
or another format suitable for transmission over the network. 
"""

recipe_model = api.model(
    "Recipe",
    {
        "id" : fields.Integer(),
        "title" : fields.String(),
        "description" : fields.String(),
    }
)

@api.route('/hello')
class HelloResource(Resource):
    def get(self):
        return {"message" : "Hello World!"}

@app.shell_context_processor
def make_shell_context():
    return {
        "db" : db,
        "Recipe" : Recipe,
    }
    
if __name__ == '__main__':
    app.run()