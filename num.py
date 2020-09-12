import random

#變數
start = 1
end = 100
r = random.randint(1, 101)
count = 0
num = int(random.randint(1, 101))


while True:
	count += 1
	print('你的數字是 ', num, '，')
	print('你猜了 ', str(count), ' 次。')
	if r == num:
		print('答案是 ', r)
		print('恭喜你猜中了！')
		break
	elif r > num:
		print('你的數字比答案小。')
		start = num + 1
	elif r < num:
		print('你的數字比答案大。')
		end = num
	num = start + round((end - start) / 2)