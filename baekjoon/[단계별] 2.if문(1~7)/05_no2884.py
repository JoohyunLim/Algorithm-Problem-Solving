h, m = map(int, input().split())
if m<45:
	if h==0:
		h=23
		m+=15	#m=60+m-45
	else:
		h-=1
		m+=15	
else:
	m-=45
print(h,m)