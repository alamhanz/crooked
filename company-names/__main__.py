from .fun import Solution

solve = Solution()
lst = []
if __name__ == "__main__":
    print("example of the input : 0 1 0 0 OR 0 1 -1 0")
    n = input("\nEnter the points : ")
    allx = [int(i) for i in n.split(" ")]
    solve = Solution()
    print(solve.diamondProb(*allx))
