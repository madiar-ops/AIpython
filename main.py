import numpy as np




# # # 1
# # nums = [3, -1, 0, 7, -5, 0, 12, -8]
# # nums_2 = [j for j in nums if j != 0]

# # nums_2.sort()

# # print(nums_2)

# # #2

# # scores = [50, 70, 90, 40, 100, 65]

# # scores_2 = scores.copy()

# # scores_2.remove(min(scores_2))
# # scores_2.remove(max(scores_2))

# # print(scores_2)
# # print(scores)


# # #3

# # items = ["apple", "banana", "apple", "orange", "banana", "apple"]


# # most_item = None
# # most_count = 0

# # for i in set(items):
# #     a = items.count(i)
# #     if a > most_count:
# #         most_count = a
# #         most_item = i


# # print(most_item, most_count)



# # #4

# # nums = [10, 3, 25, 7, 14, 9, 2] 

# # chetki_num = []
# # nechetki_num = []

# # for i in nums:
# #     if i % 2 == 0:
# #         chetki_num.append(i)
# #     else:
# #         nechetki_num.append(i)

# # chetki_num.sort()
# # nechetki_num.sort()

# # print(chetki_num)
# # print(nechetki_num)


# # #5

# # queue = ["Alex", "Bob", "Kate"]

# # queue.append("Madiyar")
# # queue.pop(0)

# # print(queue)

# # #6


# # nums = [4, 7, 1, 9, 7, 3]

# # pos=nums.index(7)
# # nums[pos]=0

# # print(nums)


# # #7

# # nums = [1, 2, 3, 4, 5]

# # nums.reverse()

# # print(nums)




# # #1_1

# # student = {
# #     "name": "Alex",
# #     "age": 18,
# #     "grade": 85
# # }

# # student["grade"] += 5

# # if student["grade"]>=90:
# #     print("Отличник")
# # else:
# #     print("Есть куда расти")



# # items = ["a@gmail.com", "b@gmail.com","a@gmail.com", "c@gmail.com", "b@gmail.com" ]

# # unique = set(items)
# # duplicates_count = len(items) - len(unique)
# # print("unique: " , unique)
# # print("duplicates: ", duplicates_count)



# # items = ["a@gmail.com", "b@gmail.com","a@gmail.com", "c@gmail.com", "b@gmail.com" ]
# # unique = set(items)
# # seen = set()
# # dups = set()

# # for i in items:
# #     if i in seen:
# #         dups.add(1)
# #     else:
# #         seen.add(1)
# # print("unique: ", seen)
# # print("duplicates_count: ", len(items) - len(seen))
# # print("duplicated_values: ", dups)


# # text = "AI is cool and AI is useful"
# # words = text.lower().split()

# # freq = {}
# # for i  in words:
# #     freq[i] = freq.get(i,0) + 1

# # print("freq: ", freq)


# # products = [
# #     {"title": "Iphone", "category":"mobile", "price":500000},
# #     {"title": "Pixel", "category":"mobile", "price":400000},
# #     {"title": "Mackbook", "category":"laptop", "price":6500000},
# #     {"title": "Lenovo", "category":"laptop", "price":4500000},
# #     {"title": "Ipad", "category":"tablet", "price":2500000},
# # ]

# # group = {}

# # for i in products:
# #     cat = i["category"]
# #     price = i["price"]


# #     if cat not in group:
# #         group[cat] = []
# #     group[cat].append(price)
# # print(group)


# # person1 = {"python", "sql", "ml", "react"}
# # person2 = {"react", "design", "python", "figma"}

# # common = person1 & person2
# # only = person1 - person2
# # only2 = person2 - person1
# # all_interests = person1 | person2

# # print("Common: ", common)
# # print("only person1: ", person1)
# # print("only person2: ", person2)
# # print("All interests: ", all_interests)



# class Student:
#     def __init__(self, name, grades):
#         self.name = name
#         self.grades = grades

#     def info(self):
#         print(f"Студент: {self.name}, Оценки: {self.grades}")

#     def avg(self):
#         return sum(self.grades) / len(self.grades)
    

# s1 = Student("Mansur", [90,100,86])
# s2 = Student("Aisha", [95,80,76])

# print(s1.name)
# print(s1.avg())
# print(s1.info())
# print(s2.name)
# print(s2.avg())
# print(s2.info())




# x = np.arange(0,10,2)
# z = np.ones((2,2))
# print(z)
# print(x)



# a = np.array([[1,2.5,3,4],
#              [5,6,7,8]])
# print("dtype: ", a.dtype)
# print("shape: ", a.shape)
# print("ndim: ", a.ndim)
# print("size: ", a.size)

# z = np.zeros((2, 3))
# o = np.ones((2, 3))
# f = np.full((2, 3), 7)
# print(z)
# print(o)
# print(f)


# b = np.arange(5,21,5)
# print(b)


img = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print(img)
print(img[1,1])