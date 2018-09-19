import torch
import numpy as np
# outputs=torch.FloatTensor([[1],[3],[3]])
# targets=torch.FloatTensor([[1],[2],[3]])
# print(targets.ne(outputs.data))
#
#
a=torch.FloatTensor([[[4],[9],[8]]])
print(a)
print(a[:,0])
b =torch.eq(a[:,:],8)
print(b)
print(a[b])
# a = np.arange(4).reshape(2,2)
# print(a[0])