from .fun import Solution

solve = Solution()
lst = []
if __name__ == "__main__":
    print("Put the integers")
    n = input("\nEnter the integers : ")
    n = int(n)
    solve = Solution()
    print(solve.isPowerOfTwo(n))
