"""
Tired of manually changing parameters like batch size or learning rate?

🚀 Try Python argparse!

You can then change them by running for example

"python experiment.py --batch-size 16"

and reproduce your experiments easily.
"""

from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("--batch-size", default=32, type=int)
parser.add_argument("--model-name", default="my_model", type=str)
parser.add_argument("--learning-rate", default=1e-4, type=float)
args = parser.parse_args()

print(args.batch_size)      # this will print: 32
print(args.model_name)      # this will print: my_model
print(args.learning_rate)   # this will print: 0.0001
