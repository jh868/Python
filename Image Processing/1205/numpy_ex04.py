import numpy as np
array = np.array([[5, 2, 7, 6], [2, 3, 10, 15]])
print('각 열을 기준으로 정렬 전 \n', array)

# np.sort(array, axis=0)  # 이렇게 사용 하면 값 반영 안함
array.sort(axis=0)
print('각 열을 기준으로 정렬 후 \n', array)

array.sort(axis=1)
print('각 행을 기준으로 정렬 후 \n', array)
