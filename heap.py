import heapq 

heap = []

heapq.heapify(heap)

heapq.heappush(heap, ("white" , 0))

print(heap)

heapq.heappush(heap, ("blue", 3))

print(heap)

v, dist  = heapq.heappop(heap)

print(v)
print(dist)


heap1= []
heapq.heappush(heap1, 0)

print(heap1)

heapq.heappush(heap1,  2)
heapq.heappush(heap1,  1)
heapq.heappush(heap1,  3)
heapq.heappush(heap1,  7)

print(heap1)

v  = heapq.heappop(heap1)
v1 = heapq.heappop(heap1)

print(v)
print(v1)

a_traiter = [("white", 0)]
print(a_traiter)
a_traiter.append(("blue", 2))
a_traiter.append(("grey", 4))
print(a_traiter)
a_traiter.sort(reverse=True)
print(a_traiter)
v, dist = a_traiter.pop()
print(v)
print(dist)

