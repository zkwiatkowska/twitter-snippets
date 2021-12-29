from argparse import ArgumentParser

parser = ArgumentParser()
subparsers = parser.add_subparsers()

parser_train = subparsers.add_parser('train')
parser_train.add_argument("--num_epochs", default=100, type=int)
parser_train.add_argument("--model_name", required=True, type=str)
parser_train.add_argument("--learning_rate", default=1e-4, type=float)

parser_eval = subparsers.add_parser('evaluate')
parser_eval.add_argument("--path_to_model", required=True, type=str)

args = parser.parse_args()
