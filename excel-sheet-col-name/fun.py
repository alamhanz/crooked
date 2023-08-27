class Solution:
    """_summary_"""

    def convertToTitle0(self, columnNumber: int) -> str:
        """_summary_

        Args:
            columnNumber (int): _description_

        Returns:
            str: _description_
        """

        new_colnumb, curr_numb = divmod(columnNumber, 26)
        new_colnumb = new_colnumb - 1 if curr_numb == 0 else new_colnumb
        curr_numb = curr_numb if curr_numb > 0 else 26
        title = chr(64 + curr_numb)

        while new_colnumb > 0:
            columnNumber = new_colnumb
            new_colnumb, curr_numb = divmod(columnNumber, 26)
            new_colnumb = new_colnumb - 1 if curr_numb == 0 else new_colnumb
            curr_numb = curr_numb if curr_numb > 0 else 26
            title0 = chr(64 + curr_numb)
            title = title0 + title

        return title

    def convertToTitle1(self, columnNumber: int) -> str:
        """_summary_

        Args:
            columnNumber (int): _description_

        Returns:
            str: _description_
        """

        charopt = []
        for i in range(26):
            charopt.append(chr(65 + i))

        title = ""
        while columnNumber > 0:
            columnNumber, curr_numb = divmod(columnNumber - 1, 26)
            title = charopt[curr_numb] + title

        return title

    def convertToTitle2(self, columnNumber: int) -> str:
        """_summary_

        Args:
            columnNumber (int): _description_

        Returns:
            str: _description_
        """

        title = ""
        while columnNumber > 0:
            columnNumber, curr_numb = divmod(columnNumber - 1, 26)
            title = chr(65 + curr_numb) + title

        return title

    def convertToTitle3(self, columnNumber: int) -> str:
        """_summary_

        Args:
            columnNumber (int): _description_

        Returns:
            str: _description_
        """

        charopt = ["Z"]
        for i in range(25):
            charopt.append(chr(65 + i))

        new_colnumb, curr_numb = divmod(columnNumber, 26)
        new_colnumb = new_colnumb - 1 if curr_numb == 0 else new_colnumb
        title = charopt[curr_numb]

        while new_colnumb > 0:
            columnNumber = new_colnumb
            new_colnumb, curr_numb = divmod(columnNumber, 26)
            new_colnumb = new_colnumb - 1 if curr_numb == 0 else new_colnumb
            title = charopt[curr_numb] + title

        return title

    def convertToTitle4(self, columnNumber: int) -> str:
        """_summary_

        Args:
            columnNumber (int): _description_

        Returns:
            str: _description_
        """

        new_colnumb, curr_numb = divmod(columnNumber - 1, 26)
        title = chr(65 + curr_numb)

        while new_colnumb > 0:
            columnNumber = new_colnumb
            new_colnumb, curr_numb = divmod(columnNumber - 1, 26)
            title = chr(65 + curr_numb) + title

        return title

    def convertToTitle(self, columnNumber: int) -> str:
        """_summary_

        Args:
            columnNumber (int): _description_

        Returns:
            str: _description_
        """

        new_colnumb, curr_numb = divmod(columnNumber, 26)
        new_colnumb = new_colnumb - 1 if curr_numb == 0 else new_colnumb
        curr_numb = curr_numb if curr_numb > 0 else 26
        title = [chr(64 + curr_numb)]

        while new_colnumb > 0:
            columnNumber = new_colnumb
            new_colnumb, curr_numb = divmod(columnNumber, 26)
            new_colnumb = new_colnumb - 1 if curr_numb == 0 else new_colnumb
            curr_numb = curr_numb if curr_numb > 0 else 26
            title.append(chr(64 + curr_numb))

        title.reverse()
        return "".join(title)
