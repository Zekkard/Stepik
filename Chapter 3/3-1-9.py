# �������� ������� modify_list(l), ������� ��������� �� ���� ������ ����� �����, 
# ������� �� ���� ��� �������� ��������, � ������ ������ ����� �� ���. 
# ������� �� ������ ������ ����������, ��������� ������ ��������� ����������� ������, ��������:
# lst = [1, 2, 3, 4, 5, 6]
# print(modify_list(lst))  # None
# print(lst)               # [1, 2, 3]
# modify_list(lst)
# print(lst)               # [1]
# lst = [10, 5, 8, 3]
# modify_list(lst)
# print(lst)               # [5, 4]
# ������� �� ������ ������������ ����/����� ����������.

def modify_list(lst):
    lst2 = []
    for i in lst:
        if i % 2 == 0:
            lst2.append(int(i//2))
    lst.clear()
    for j in lst2:
        lst.append(j)