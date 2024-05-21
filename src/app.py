from flask import Flask, request
from flask_restx import Resource, Api, fields
from fib import fib

app = Flask(__name__)
api = Api(app)

fib_model = api.model('Fib', {
    'result': fields.Integer(description='Fibonacci result')
})

@api.route('/fib')
class Fib(Resource):
    @api.doc(params={'n': 'The Fibonacci sequence index'})
    @api.response(200, 'Success', fib_model)
    @api.response(400, 'Bad Request')
    @api.response(500, 'Internal Server Error')
    def get(self):
        try:
            n = request.args.get('n')
            if n is None:
                return {'status': 400, 'message': 'Parameter n is missing'}, 400

            if not n.isdigit():
                return {'status': 400, 'message': 'Parameter n must be a number.'}, 400

            n = int(n)

            if n <= 0:
                return {'status': 400, 'message': 'Parameter n must be a positive integer.'}, 400

            fib_number = fib(n)
            return {'result': fib_number}, 200

        except ValueError as e:
            return {'status': 400, 'message': str(e)}, 400
        except Exception as e:
            return {'status': 500, 'message': 'An unexpected error occurred.', 'error': str(e)}, 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

