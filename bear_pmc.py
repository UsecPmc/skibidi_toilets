text = input()
answer = ""
for i in text:
    if i.isupper():
        answer += i
    print(answer)