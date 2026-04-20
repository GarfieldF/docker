
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
#print(torch.cuda.nccl.version())
print(f'Available GPU devices: {torch.cuda.device_count()}')
print(f'Current GPU devices: {torch.cuda.current_device()}')
print(f'Device Name: {torch.cuda.get_device_name()}')

import torch
import ctypes
import os

def get_gpu_pci_bus_id(cuda_index):
    try:
        # 在 Windows 上加载 CUDA 运行时库
        cuda = ctypes.windll.LoadLibrary('nvcuda.dll')
        cuda.cuInit(0)
        
        device = ctypes.c_int()
        cuda.cuDeviceGet(ctypes.byref(device), cuda_index)
        
        # 分配缓冲区来存储 PCI 总线 ID
        buf = b' ' * 100
        buf_p = ctypes.c_char_p(buf)
        cuda.cuDeviceGetPCIBusId(buf_p, 100, device)
        
        return buf_p.value.decode().strip()
    except Exception as e:
        return f"无法获取 PCI 总线 ID: {str(e)}"

print("CUDA 设备与 PCI 总线 ID 对应关系:")
for i in range(torch.cuda.device_count()):
    device = torch.device(f'cuda:{i}')
    device_name = torch.cuda.get_device_name(device.index)
    pci_bus_id = get_gpu_pci_bus_id(i)
    print(f"cuda:{i} - 设备名称: {device_name} - PCI 总线 ID: {pci_bus_id}")
    
