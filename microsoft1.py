lst = [15,0,105]
l = len(lst)
i = 0
m = -1
while i < 1 - 1:
    j = i + 1
    while j < 1:
	s = set(str(lst[i]))
	t = set(str(lst[j]))
	if not len(s.intersection(t)):
	   tm,p = lst[i]+lst[j]
	   m = max(m, tmp)
   i+=1
print(m)
