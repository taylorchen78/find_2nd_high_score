"""
寫一個function來印出誰的成績是第二高，如果超過一個人分數都是第二高，請把人名一行一行印出來。

function的參數：
    students：一個二維清單，例如 [['Jerry', 88], ['Justin', 84], ['Tom', 90], ['Akriti', 92], ['Harsh', 90]] 

function的回傳：
    不須回傳

期望的執行結果：
    例如 有個清單是 students = [['Jerry', 88], ['Justin', 84], ['Tom', 90], ['Akriti', 92], ['Harsh', 90]]  
    second_highest(students)  的執行結果應該要印出：
    Tom
    Harsh

重要提示：
不一定要，但可以使用sorted這個function來排列清單，

例如 
x = [3, 1, 4, 5, 2]
x = sorted(x) # 排列x (由小到大)
print(x) # 印出 [1, 2, 3, 4, 5]

如果要顛倒排列也可以，只要多加reverse=True

x = [3, 1, 4, 5, 2]
x = sorted(x, reverse=True) # 排列x (由大到小)
print(x) # 印出 [5, 4, 3, 2, 1]
"""


def second_highest(students):
	name = []
	score = []
	for i in range(len(students)):
		#name.append(students[i][0])
		score.append(students[i][1])

	score = sorted(score, reverse=True)

	for i in range(len(students)):
		if students[i][1] == score[1]:
			print(students[i][0])


students = [['Jerry', 88], ['Justin', 84], ['Tom', 90], ['Akriti', 92], ['Harsh', 90]]
second_highest(students)
