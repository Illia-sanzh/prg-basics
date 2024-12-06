heights = [10,6,8,5,11,9]

def f(heights):
    n = len(heights)
    stack, ans = [], [0] * n
    for i in range(n):
        while stack and stack[-1] < heights[i]:
            stack.append()
            ans[i] += 1
        print(ans)

print(f(heights))




