def ip_to_num(ip):

    def step_1(s):
        lst = s.split('.')
        ans = []
        for el in lst:
            q = bin(int(el))[2:]
            if len(q) < 8:
                q = '0' * (8 - len(q)) + q
            ans.append(q)
        return ans

    step_1 = step_1(ip)
    print(step_1)
    step_2 = ''.join(step_1)
    print(step_2)
    step_3 = int(step_2, 2)
    return step_3


def num_to_ip(num):
    step_1 = bin(num)[2:]
    print(step_1)
    if len(step_1) < 32:
        step_1 = '0' * (32 - len(step_1)) + step_1
    print(step_1)
    step_2 = list(map(''.join, zip(*[iter(step_1)] * 8)))
    print(step_2)
    step_3 = '.'.join([str(int(x, 2)) for x in step_2])
    return step_3


# print(ip_to_num('192.168.1.1'))
# print(ip_to_num('255.255.255.255'))
print(ip_to_num('10.0.0.0'))

# print(num_to_ip(3232235777))
print(num_to_ip(167772160))
# print(num_to_ip(2953838593))
# print(num_to_ip(0))
# print(num_to_ip(2 ** 32 - 1))
# print(num_to_ip(9964972))


"""
var1
from ipaddress import IPv4Address

def ip_to_num(ip):
    return int(IPv4Address(ip))

def num_to_ip(num):
    return str(IPv4Address(num))
    
var2  
def ip_to_num(ip):
    nums = list(map(int, ip.split('.')))
    return (nums[0] << 24) + (nums[1] << 16) + (nums[2] << 8) + nums[3]

def num_to_ip(num):
    return f"{num >> 24 & 255}.{num >> 16 & 255}.{num >> 8 & 255}.{num & 255}"

"""