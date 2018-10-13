# class Stack():
# 	def __init__(self):
# 		self.items = []
 
# 	def isEmpty(self):
# 		return self.items == []
# 	def push(self, item):
# 		self.items.append(item)
# 	def pop(self):
# 		return self.items.pop()
# 	def peek(self):
# 		return self.items[len(self.items)-1]
# 	def size(self):
# 		return len(self.items)
 
# while True:
# 	n = int(input())
# 	if n == 0:
# 		break
# 	a = list(map(int, input().split()))
	
# street = 1
# st = Stack()
# while len(a) != 0 or st.size() != 0:
#     if len(a)!=0 and a[0]== street:
#         a.pop(0)
#         street += 1
#     elif st.size()!=0 and st.peek()==street:
#         st.pop()
#         street += 1
#     elif len(a)!=0:
#         st.push(a[0])
#         a.pop(0)
#     else:
#         print("no")
#         break
#     if street == n+1:
#         print("yes")
#         break
