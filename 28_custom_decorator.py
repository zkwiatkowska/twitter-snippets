# WE DEFINE OUR DECORATOR FOR REPETITIVE STUFF

def log_outputs(func):

    def output_logging(*args, **kwargs):
        print(f"Those inputs were given: {args}, {kwargs}")
        outputs = func(*args, **kwargs)
        print(f"Those outputs were obtained: {outputs}")

    return output_logging


# WE WRAP OUR FUNCTION WITH IT

@log_outputs
def training_step(inputs, epochs=10):
    loss = 0.5  # magical ML procedure :D
    return loss


# WE EXECUTE IT

training_step([1, 2, 3], epochs=5)
# Those inputs were given: ([1, 2, 3],), {'epochs': 5}
# Those outputs were obtained: 0.5
