import requests
import argparse


def create_main_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='localhost')
    parser.add_argument('--port', default=8000, type=int)

    return parser


def graceful_exit():
    ack = input('Are you sure you want to leave (Y/N)?')
    if ack == 'Y':
        print('Goodbye!')
        exit()
    elif ack == 'N':
        print('OK, let\'s continue')
    else:
        print('Stupid input, but continue')


def ask_amount(product_name):
    user_input = input(f'How much {product_name} (press enter for no {product_name})?>')
    if not user_input:
        return 0
    else:
        try:
            return int(user_input)
        except ValueError:
            print('Incorrect input, assuming 0')
            return 0


def get_status(main_args):
    id = input('Print order ID:')

    try:
        id = str(id)
    except ValueError:
        print('Incorrect ID, bac to home')

    status = requests.get(f'http://{main_args.host}:{main_args.port}/get_status', params=dict(
        id=id
    )).text

    if status == 'queue':
        print('Order is queueing')
    elif status == 'cooking':
        print('Order is in kitchen')
    elif status == 'ready':
        print('Order is ready')
    elif status == 'absent':
        print('No such order')


def create_order(main_args):
    order_id = requests.post(f'http://{main_args.host}:{main_args.port}/create', data=dict(
        bigmacs=ask_amount('BigMacs'),
        cola=ask_amount('Cola'),
        fries=ask_amount('Fries')
    )).text
    print(f'Order ID: {order_id}')


def main():
    main_parser = create_main_parser()
    main_args = main_parser.parse_args()

    while True:
        try:
            cmd = input('Enter command>')
            if cmd == 'create':
                create_order(main_args)
            elif cmd == 'get_status':
                get_status(main_args)
            elif cmd == 'exit':
                graceful_exit()
            else:
                print(f'Unknown command: {cmd}')
        except KeyboardInterrupt:
            graceful_exit()


if __name__ == '__main__':
    main()
