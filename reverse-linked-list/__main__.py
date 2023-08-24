from .fun import Solution, ListNode

solve = Solution()
lst = []
if __name__ == "__main__":
    print("The digits must between -5000 and 5000")
    print("example of the input : 2 4 5 6 OR 3 4 6 8 6 1")
    n = input("\nEnter the digits elements : ")
    n = n.strip()

    if len(n) > 0:
        lst = [ListNode(int(i)) for i in n.split(" ")]

        for i in range(len(lst) - 1):
            lst[i].next = lst[i + 1]

        head = lst[0]
    else:
        lst = []
        head = None

    print("input: ", head)
    solve = Solution()
    head_reverse = solve.reverseList(head)

    curr_node = head_reverse
    while curr_node is not None:
        print(curr_node.val)
        curr_node = curr_node.next
