s = {100, 200, 300, 400}
s_list = list(s)
s_list[0], s_list[2] = s_list[2], s_list[0]
s = set(s_list)
print("Set after swapping:", s)
