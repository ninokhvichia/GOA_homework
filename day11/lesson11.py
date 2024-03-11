for i in range(1,51):
    if i % 5 ==0:
        print(i)


for i in range(2,21):
    if i % 2 ==0:
        print(i)

for i in range(2,21,2):
    print(i)

# 1*
#5*
#6*
#7*
#8*
#9*
#10
final_product=1

for i in range(5,11):
    final_product=final_product*i
    print("ამ ეტაპზე ნამრავლი უდრის:",final_product,
        "ხოლო final product გავამრავლეთ", i,"ზე")