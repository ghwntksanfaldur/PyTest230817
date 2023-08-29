from collections import deque
deque_list = deque()

# deque_list = deque()
# for i in range(5):
#     deque_list.append(i)
#     print(f"deque_list 의출력: {deque_list}")

# test_deque_reverse =deque(reversed(deque_list))
# print(f"test_deque_reverse의출력:{test_deque_reverse}")

deque_list.extend([5, 6, 7])
print(f"deque_list extend([5,6,7]) 의출력: {deque_list}")

deque_list.extendleft([8, 9, 10])
print(f"deque_list extendleft([8,9,10]) 의출력: {deque_list}")
