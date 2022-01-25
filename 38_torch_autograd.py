import torch


class WeirdFunc(torch.autograd.Function):

    @staticmethod
    def forward(ctx, inp):
        ctx.save_for_backward(inp)
        return 2 * inp ** 3 + 15 - inp

    @staticmethod
    def backward(ctx, grad_outputs):
        inp, = ctx.saved_tensors
        return grad_outputs * (6 * inp ** 2 - 1)


x = torch.tensor([1.], requires_grad=True)
y = WeirdFunc.apply(x)
print(y)                              # output: 16
z = WeirdFunc.apply(y)
print(z)                              # output: 8191
z.backward()
print(x.grad)                         # output: 7675
