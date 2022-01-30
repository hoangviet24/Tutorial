'''
list comprehensions
'''
'''
List comprehensions giúp bạn viết code ngắn gọn hơn(đặc biệt khi đang trong vòng lặp đã có)
và dễ đọc, nhìn code hơn
'''

# New_list[<action> for <items> in <iterator> if <some condition>]

word = "hello word"
#print([char for char in word])
Numbers= [i for i in range(2000,3001) if i % 5 ==0 and i % 7 != 0]
#print(Numbers)
transactions = [100,200,300,340,350,220,230,450]
thuế = 0.08 # thuế
dịch_vụ = 0.07 # Phí phục vụ
def get_price_tax_service(bill):
    return bill*(1 + thuế + dịch_vụ)

#print(get_price_tax_service(100))
final_price = [get_price_tax_service(bill) for bill in transactions]
#print(final_price)

#Advanced Functions: hàm nâng cao

#list() --> convert stings => list

my_string = "welcome to hoangviet"
list_of_chars = list(my_string)
#print(list_of_chars)

#sum(): cộng giá trị

#print(sum([1,2,3,4,5,6,7,8,9]))

#zip(): looping through two list simultaneously: lặp 2 list cùng lúc với nhau

# satthu = ["Ling", "Fanny", "Saber"]
# vukhi = ['Blade','Dual sword','mega sword']
# for index,(satthu,vukhi) in enumerate(zip(satthu,vukhi)):
#     print(f"{index + 1}.{satthu} has {vukhi}")

#sorted
a = sorted(["ironman","hello","you","super"],key = lambda el:el[0])
print(a)

b=sorted([{'name':'hoangviet', 'age':17},
 {'name': 'Andy','age': 18}], key = lambda el:el['name'])
print(b)

'''
5. 2D Array/list = Matrix: Mảng hai chiều
'''
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
# print(matrix[2][1])
# for row in range(len(matrix)):
#     for col in range(len(matrix)):
#         print(matrix[row][col])


#Transform Matrix in list

list = [matrix[row][col] for row in range(len(matrix)) for col in range(len(matrix))]
#print(list)

#Combine columns with zip and *:
#print([x for x in zip(*matrix)]) 


print("YESYES                  YES           YESYESYESYES  ")
print("YES   YES               YES         YES           YES ")
print("YES      YES            YES       YES              YES")
print("YES         YES         YES      YES                YES")
print("YES            YES      YES       YES             YES")
print("YES               YES   YES         YES         YES")
print("YES                  YESYES            YESYESYEs")