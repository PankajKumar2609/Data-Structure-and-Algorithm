def matrixRotation(matrix, r):
    
    for k in range(int(min(m,n)/2)):
        l=[]
        
        for j in range(n-k-1,-1+k,-1):
            l.append(matrix[k][j])
        
        for j in range(k+1,m-k-1):
            l.append(matrix[j][k])

        for j in range(k,n-k):
            l.append(matrix[m-k-1][j])

        for j in range(m-k-2,k,-1):
            l.append(matrix[j][n-1-k])
        length = (n-2*k)*2+(m-2-2*k)*2
        if length==0:
            break
        rot = r%length
        l=l[-rot:]+l[:-rot]
        ini = 0
        for j in range(n-k-1,-1+k,-1):
            matrix[k][j]=str(l[ini])
            ini+=1
        
        for j in range(k+1,m-k-1):
            matrix[j][k]=str(l[ini])
            ini+=1

        for j in range(k,n-k):
            matrix[m-k-1][j]=str(l[ini])
            ini+=1

        for j in range(m-k-2,k,-1):
            matrix[j][n-1-k]=str(l[ini])
            ini+=1
    for i in range(m):
        print(' '.join(matrix[i]))
  #m is number of rows and n is number of columns
  #r times rotate matrix
