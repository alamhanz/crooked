from .fun import Solution

solve = Solution()
lst = []
if __name__ == "__main__":
    print("The digits must between 0 and 9")
    print("example of the input : 2 4 5 6 OR 3 4 6 8 6 1")
    n = input("\nEnter the digits elements : ")
    n = n.strip()

    lst = [int(i) for i in n.split(" ")]

    print("input: ", lst)
    print("output: ", solve.plusOne(lst))
