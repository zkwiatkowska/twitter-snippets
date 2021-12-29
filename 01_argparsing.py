from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("--batch-size", default=32, type=int)
parser.add_argument("--model-name", default="my_model", type=str)
parser.add_argument("--learning-rate", default=1e-4, type=float)
args = parser.parse_args()

print(args.batch_size) # this will print: 32
print(args.model_name) # this will print: my_model
print(args.learning_rate) # this will print: 0.0001
