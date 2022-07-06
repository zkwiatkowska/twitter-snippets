import torch

x = torch.tensor([2.], requires_grad=True)
print(x.requires_grad)                         # TRUE

with torch.no_grad():
    y = x + 2

print(y.requires_grad)                         # FALSE

z = 3 * y

print(z.requires_grad)                         # FALSE
