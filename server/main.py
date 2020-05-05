import flask
import lib

app = flask.Flask('mcdonalds-server')
order_storage = lib.OrderStorage()


@app.route('/create', methods=['POST'])
def create_order():
    args = {
        item: int(flask.request.args[item])
        for item in order_storage.POSSIBLE_ITEMS
        if item in flask.request.args
    }

    id = order_storage.create_order(**args)
    return str(id)


@app.route('/get_status', methods=['GET'])
def get_status():
    id = int(flask.request.args['id'])
    state = order_storage.get_status(id)
    return str(state)


def main():
    app.run('::', port=8000, debug=True)


if __name__ == '__main__':
    main()
