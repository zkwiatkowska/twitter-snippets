import torch

x = torch.tensor([1.], requires_grad=True)

y1 = x ** 2 + x - 1
y1.backward()
print(x.grad)                                   # <-- this results in 3.

x = torch.tensor([1.], requires_grad=True)

y2 = x ** 2 + x.detach() - 1
y2.backward()
print(x.grad)                                   # <-- this results in 2.
