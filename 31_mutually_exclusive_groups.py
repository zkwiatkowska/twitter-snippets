from argparse import ArgumentParser

parser = ArgumentParser()

group = parser.add_mutually_exclusive_group()
group.add_argument("--shuffle", action="store_true")
group.add_argument("--use_sampler", action="store_true")

print(parser.parse_args(["--shuffle"]))                   # Namespace(shuffle=True, use_sampler=False)
print(parser.parse_args(["--use_sampler"]))               # Namespace(shuffle=False, use_sampler=True)
print(parser.parse_args(["--shuffle", "--use_sampler"]))  # error: argument --use_sampler: not allowed with argument --shuffle
