# # solving hackerrank problems
# 1.Nested list
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
