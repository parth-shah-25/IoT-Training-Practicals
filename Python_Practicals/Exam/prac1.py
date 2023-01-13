str = "@le@rningpython$"
ans = str.replace('@','a')
ans_list = list(ans)
ans_list[0] = ''
ans_list[len(ans_list)-1]= ''
answer = "".join(ans_list)
print(answer)