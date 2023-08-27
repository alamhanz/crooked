from .fun import Solution

solve = Solution()
lst = []
if __name__ == "__main__":
    print("Put the list of integers such as 1 2 23 -3")
    print("number is between -10000 and 10000")
    num = input("\nEnter the list of int : ")
    num = [int(i) for i in num.split(" ")]

    k = input("sub array size: ")
    k = int(k)
    solve = Solution()
    print(solve.findMaxAverage(nums=num, k=k))
