# solving hackerrank problems
# 1.List comprahension
# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())
#     result=[[i,j,k] for i in range(x+1) for j in range (y+1) for k in range (z+1) if i+j+k!=n]
# print(result)


# 2.find runner up
# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
#     # s=list(set(arr))
#     # s.sort()
#     # print(s[-2])
#     print(sorted(list(set(arr)))[-2])

# 3.finding percentage
# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
#     avg=sum(student_marks[query_name])/3
#     print("{:.2f}".format(avg))

# 4/nested list
# if __name__ == '__main__':
#     records=[]
#     s=set()
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         records.append([name,score])
#         s.add(score)
        
# sec_low_sco=sorted(s)[1]
# sec_low_names=[]

# for name,score in records:
#     if(score == sec_low_sco):
#         sec_low_names.append(name)
# for name in sorted(sec_low_names):
#     print(name)