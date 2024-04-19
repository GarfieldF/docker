'''
@Description: test cuda and pytorch
@Author: zifei yang
@Date: 2020-12-17 21:04:22
@Email: iyangzifei@gmail.com
'''
import torch
import torch.nn as nn
import torch.nn.functional as F
from copy import deepcopy
print(f'PyTorch available: {torch.cuda.is_available()}')
print(f'PyTorch version: {torch.__version__}')
print('*'*10)
print(f'CUDA version: ')
print(torch.version.cuda)
print('*'*10)
print(f'CUDNN version: {torch.backends.cudnn.version()}')
# print(torch.cuda.nccl.version())
print(f'Available GPU devices: {torch.cuda.device_count()}')
print(f'Device Name: {torch.cuda.get_device_name()}')
class Net(nn.Module):
	def __init__(self):
		super(Net,self).__init__()
		self.conv1=nn.Conv2d(1,6,3)
		self.conv2=nn.Conv2d(6,16,3)
		self.fc1=nn.Linear(16*6*6,120)
		self.fc2=nn.Linear(120,84)
		self.fc3=nn.Linear(84,10)
	def forward(self,x):
		x=F.max_pool2d(F.relu(self.conv1(x)),(2,2))
		print(x.size())
		x=F.max_pool2d(F.relu(self.conv2(x)),2)
		print(x.size())
		x=x.view(x.size()[0],-1)
		print(x.size())
		x=F.relu(self.fc1(x))
		print(x.size())
		x=F.relu(self.fc2(x))
		print(x.size())
		x=self.fc3(x)
		return x
	def num_flat_features(self, x):
		size = x.size()[1:]  # all dimensions except the batch dimension
		num_features = 1
		for s in size:
		    num_features *= s
		return num_features
	def test(self,x):
		print('i have try',x.size())
device=torch.device('cuda')
net = Net().to(device)
for name,parameters in net.named_parameters():
	print(name,":",parameters.size())
print('net:',net)
input=torch.randn(1,1,32,32).to(device)



import torch.optim as optim

optimizer=optim.SGD(net.parameters(),lr=1)

output=net(input)
target=torch.randn(1,10).to(device)
criterion=nn.MSELoss()
loss=criterion(output,target)
print(loss)
loss=torch.clamp(loss,0,0.5)
loss.backward()

print("1:",net.fc3.bias)

optimizer.step()
print(net.fc3.bias.grad)
print("3:",net.fc3.bias)
print("TEST FINISH!")
