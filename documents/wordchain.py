l = input()
n = input()
old_word = raw_input()
ans = None
for i in range(1,n):
	word = raw_input()
	k = 0
	for j in range(0,l):
		if old_word[j] != word[j]:
			k+=1
	if k > 2 and ans == None:
		ans = old_word
	old_word = word

print ans