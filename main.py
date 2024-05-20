from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/fib', methods=['GET'])
def get_fib():
    try:
        n = request.args.get('n')
        if n is None:
            return jsonify({'error': 'Parameter n is missing'}), 400

        if not n.isdigit():
            return jsonify({'error': 'Parameter n must be a non-negative integer.'}), 400

        n = int(n)

        if n <= 0:
            return jsonify({'error': 'Parameter n must be a positive integer.'}), 400

        fib_number = return_fib(n)
        return jsonify({'n': n, 'fib': fib_number}), 200

    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred.', 'message': str(e)}), 500

def return_fib(n):
    if n == 1 or n == 2:
        return 1

    a, b = 1, 1
    for _ in range(2, n):
        a, b = b, a + b
    return b

if __name__ == '__main__':
    app.run(debug=True)
