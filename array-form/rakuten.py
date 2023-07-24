
def solution(A,K):
    width = max(3,len(str(max(A))))
    n_col = min(K,len(A))
    n_row,n_col_last_row = divmod(len(A),n_col)

    base_edges = '+'+('-'*width)
    top = (base_edges*n_col)+'+'

    A_string = [str(i) for i in A]
    A_in_array = ['|'+' '*(width-len(i))+i for i in A_string]

    if (n_row,n_col_last_row) == (1,0):
        array = top + '\n' + ''.join(A_in_array) + '|\n' + top 
    else:
        array = top + '\n'

        for i in range(n_row):
            A_temp = A_in_array[n_col*i:n_col*(i+1)]
            array_mid = ''.join(A_temp)+ '|\n'+ top + '\n'
            array += array_mid
        
        if n_col_last_row>0:
            bottom = (base_edges*n_col_last_row)+'+'
            A_temp = A_in_array[-n_col_last_row:]
            array_mid = ''.join(A_temp)+ '|\n'+ bottom + '\n'
            array += array_mid

    # sys.stdout.write(array)
    return array
