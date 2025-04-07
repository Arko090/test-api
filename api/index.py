from flask import Flask, Blueprint, jsonify
import logging

# Configure Logging
logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.ERROR)
logging.basicConfig(level=logging.WARNING)

class ClassTemplate_1:
    def run(self) -> str:
        try:
            return "<h1>This Route is Reflecting ClassTemplate_1</h1>"
        except Exception as e:
            logging.error('An error occurred: ', exc_info=e)
            raise e

class ClassTemplate_2:
    def run(self) -> str:
        try:
            return "<h1>This Route is Reflecting ClassTemplate_2</h1>"
        except Exception as e:
            logging.error('An error occurred: ', exc_info=e)
            raise e

def create_app():
    app = Flask(__name__)
    main_blueprint = Blueprint('main', __name__)

    @main_blueprint.route('/', methods=['GET'])
    def RootMethod():
        try:
            return "<h1>Welcome to Velorra Root</h1>"
        except Exception as e:
            logging.error('An error occurred: ', exc_info=e)
            raise e

    @main_blueprint.route('/template_1', methods=['GET'])
    def Template_1():
        try:
            return ClassTemplate_1().run()
        except Exception as e:
            logging.error('An error occurred: ', exc_info=e)
            return jsonify({'Error': str(e)}), 400

    @main_blueprint.route('/template_2', methods=['GET'])
    def Template_2():
        try:
            return ClassTemplate_2().run()
        except Exception as e:
            logging.error('An error occurred: ', exc_info=e)
            return jsonify({'Error': str(e)}), 400

    app.register_blueprint(main_blueprint)
    return app

app = create_app()
