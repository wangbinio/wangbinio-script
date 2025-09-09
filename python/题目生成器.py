import random

def generate_subtractions(z, total, delta=0):
    prev1, prev2 = None, None
    output = ''
    z += delta
    for i in range(total):
        while True:
            # 生成x: 1到z之间的随机数
            x = random.randint(3+delta, z)
            if random.random() < 0.2 and x < z:
                 x += 1
            # 生成y: 0到x之间的随机数
            y_rand = random.random()
            if y_rand < 0.02:
                y = 0
            elif y_rand < 0.03:
                y = x
            else:
                y = random.randint(2, x-1)
            current = (x, y)
            if current != prev1 and current != prev2:
                break
                
        prev2, prev1 = prev1, current
        
        output += f"{x:<2}-{y:>2}=(   )\t"
        if (i+1) % 5 == 0:
            output = output[:-1] + '\n'
            f.write(output)
            output = ''
        if (i+1) % 60 == 0 and (i+1) % 120 != 0:
            f.write('\n')
            

def generate_equations(z, total, delta=0):
    prev1, prev2 = None, None
    output = ''
    z += delta
    for i in range(total):
        while True:
            # 生成x: 1/40概率为0，1/40概率为z，其余均匀分布在[1, z-1]
            x_rand = random.random()
            if x_rand < 0.01:
                x = 0
            # elif x_rand < 0.02:
                # x = z
            else:
                x = random.randint(2, z-3)
                
            if x < z // 3:
                x = random.randint(z // 3, z-5)
            
            
            # 计算y的最大可能值
            y_max = z - x if x < z else z - x - 1
            
            # 生成y: 1/40概率为0，其余均匀分布在[1, y_max]
            y = 0 if (y_max > 0 and random.random() < 0.01) else random.randint(1, y_max) if y_max > 0 else 0
            # x += delta // 2
            # y += delta // 2
            current = (x, y)
            if current != prev1 and current != prev2:
                break
                
        prev2, prev1 = prev1, current
        
            
        output += f"{x:<2}+{y:>2}=(   )\t"
        if (i+1) % 5 == 0:
            output = output[:-1] + '\n'
            f.write(output)
            output = ''
        if (i+1) % 60 == 0 and (i+1) % 120 != 0:
            f.write('\n')

if __name__ == "__main__":
    # z = int(input("请输入数字z: "))
    total = 600
    with open("subject.txt", "w+") as f:
        generate_equations(20, total, 20)
        generate_subtractions(15, total, 15)
