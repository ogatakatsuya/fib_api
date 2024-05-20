from flask import Flask, request, jsonify
from fib import fib

app = Flask(__name__)

@app.route('/fib', methods=['GET'])
def get_fib():
    try:
        n = request.args.get('n')
        if n is None:
            return jsonify({'status': 400, 'message': 'Parameter n is missing'}), 400

        if not n.isdigit():
            return jsonify({'status': 400, 'message': 'Parameter n must be a number.'}), 400

        n = int(n)

        if n <= 0:
            return jsonify({'status': 400, 'message': 'Parameter n must be a positive integer.'}), 400

        fib_number = fib(n)
        return jsonify({'result': fib_number}), 200

    except ValueError as e:
        return jsonify({'status': 400, 'message': str(e)}), 400
    except Exception as e:
        return jsonify({'status': 400, 'message': 'An unexpected error occurred.', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
