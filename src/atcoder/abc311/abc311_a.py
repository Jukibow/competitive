
# param
n = int(input())
s = input()

# solve
stack = []
for i in range(n):
    if not "A" in stack and s[i] == "A":
        stack.append("A")
    elif not "B" in stack and s[i] == "B":
        stack.append("B")
    elif not "C" in stack and s[i] == "C":
        stack.append("C")

    if len(stack) == 3:
        print(i + 1)
        break
