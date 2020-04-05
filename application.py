from flask import Flask, request
from flask_restful import Resource, Api

application = app = Flask(__name__)
api = Api(app)

@app.route('/')
def hello_name():
   return "Hello world...."

class HelloWorld(Resource):
    def get(self):
        return {"about": "Hello World"}
    
api.add_resource(HelloWorld, '/api')

if __name__ == "__main__":
    app.run(debug=True)
