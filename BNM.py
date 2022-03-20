# BNM is represented by 3D Numpy Array => row, column and bipolar number with 6 tuples for
# BNM Checking
#A1.shape and A2.shape returns (3, 3, 6) the dimension of A. (row, column, numbers of element
# (Bipolar Neutrosophic Number, 6 elements) )
# A.shape[0] = 3 rows
# A.shape[1] = 3 columns
# A.shape[2] = Each bipolar neutrosophic number has 6 tuple as usual
#One can use any matrices having arbitrary dimension
import numpy as np
#A1 is a BNM
# A1= np.array([ [[0.000, 0.001, 0.002, -0.003, -0.004, -0.005], [0.010, 0.011, 0.012, -0.013, -0.014, -
# 0.015] , [0.020, 0.021, 0.022, -0.023, -0.024, -0.025] ],
# [[0.100,0.101,0.102,-0.103,-0.104, -0.105], [0.110,0.111,0.112,-0.113,-0.114,-0.115], [0.120,0.121,0.122,-
# 0.123,-0.124,-0.125] ],
# [[0.200,0.201,0.202,-0.203,-0.204,-0.205], [0.210, 0.211,0.212,-0.213,-0.214,-0.215], [0.220,0.221,0.222,-
# 0.223,-0.224,-0.225] ] ])
#A2 is not BNM
# A2= np.array([ [[0.000, 0.001, 0.002, -0.003, -0.004, -0.005], [0.010, 0.011, 0.012, -0.013, -0.014, -
# 0.015] , [0.020, 0.021, 0.022, -0.023, -0.024, -0.025] ],
# [[0.100,0.101,0.102,-0.103,-0.104, -0.105], [0.110,0.111,0.112,-0.113,-0.114,-0.115],
# [0.120,0.121,0.122,-0.123,-0.124,-0.125] ],
# [[0.200,0.201,0.202,-0.203, 0.204,-0.205], [0.210, 0.211,0.212,-0.213,-0.214,-0.215],
# [0.220,0.221,0.222,-0.223,-0.224,-0.225] ] ])
def BNMChecking (A):
    dimA=A.shape
    control=0
    counter = 0
    for i in range (0,dimA[0]):
        if counter == 1:
            break
        for j in range (0,dimA[0]):
            if counter == 1:
                break
            for d in range (0, dimA[2]):
                if counter ==0: 
                    if (d==0 or d==1 or d==2) :
                        if not (0 <= A[i][j][d] <= 1):
                            counter=1
                            print (A[i][j],' is not a bipolar neutrosophic number, so the matrix is not a BNM')
                            control=1
                            break
                    if (d==3 or d==4 or d==5) :
                        if not (-1 <= A[i][j][d] <= 0) :
                            counter=1
                            print (A[i][j], ' is not a bipolar neutrosophic number, so the matrix is not a BNM')
                            control=1
                            break
                else:
                    print (A[i][j], ' is not a bipolar neutrosophic number, so the matrix is not a BNM')
                    break
    if control==0:
        print (A, 'The matrix is a BNM')

# BNMChecking(A2)

# A= np.array([ [ [0.3,0.6,1,-0.2,-0.54,-0.4], [0.1,0.2,0.8,-0.5,-0.34,-0.7]],
#  [ [0.1,0.12,0,-0.27,-0.44,-0.92], [0.5,0.33,0.58,-0.33,-0.24,-0.22]],
#  [ [0.11,0.22,0.6,-0.29,-0.24,-0.52],[0.22,0.63,0.88,-0.28,-0.54,-0.32] ]
#  ])
#A.shape gives (3, 2, 6) the dimension of A. (row, column, numbers of element (BipolarNeutrosophic Number, 6 elements) )
# A.shape[0] = 3 rows
# A.shape[1] = 2 columns
# A.shape[2] = each bipolar neutrosophic number with 6 tuple as usual
def BNMCompelementOf(A):
    global Ac
    dimA=A.shape # Dimension of the matrix
    Ac= [] # Empty matrix with dimension of A to create complement of A
    for i in range (0,dimA[0]): # for rows, here 3
        H=[]
        for j in range (0,dimA[1]): # for columns, here 2
            H.extend([ [ 1-A[i][j][0], 1-A[i][j][1], 1-A[i][j][2], -1-(-A[i][j][3]), -1-(-A[i][j][4]), -1-(-A[i][j][5]) ] ])
            Ac.append(H)
    print ('A= ', A)
    print ('*********************************************************************')
    print('Ac= ', np.array(Ac))

# BNMCompelementOf(A)

# A= np.array([ [ [0.3,0.6,1,-0.2,-0.54,-0.4], [0.1,0.2,0.8,-0.5,-0.34,-0.7] ],
#  [ [0.1,0.12,0,-0.27,-0.44,-0.92], [0.5,0.33,0.58,-0.33,-0.24,-0.22] ],
#  [ [0.11,0.22,0.6,-0.29,-0.24,-0.52],[0.22,0.63,0.88,-0.28,-0.54,-0.32] ]])
def scoreMatrix(A):
    score=[]
    dimA=A.shape # Dimension of the matrix
    for i in range (0,dimA[0]): # for rows, here 3
        H=[]
        for j in range (0,dimA[1]): # for columns, here 2
            H.extend([ [ ( A[i][j][0] + 1 - A[i][j][1] + 1 - A[i][j][2] + 1 + A[i][j][3] - A[i][j][4] - A[i][j][5] )/6 ] ])
        score.append(H)
    print('Score Matrix= ', np.array(score))

def accuracyMatrix (A):
    accuracy=[]
    dimA=A.shape # Dimension of the matrix
    for i in range (0,dimA[0]): # for rows, here 3
        H=[]
        for j in range (0,dimA[1]): # for columns, here 2
            H.extend([ [ A[i][j][0] - A[i][j][2] + A[i][j][3] - A[i][j][5] ] ])
        accuracy.append(H)
    print('Accuracy Matrix= ', np.array(accuracy))

def certaintyMatrix (A):
    certainty = []
    dimA=A.shape # Dimension of the matrix
    for i in range (0,dimA[0]): # for rows, here 3
        H=[]
        for j in range (0,dimA[1]): # for columns, here 2
            H.extend([ [ A[i][j][0] - A[i][j][5] ] ])
        certainty.append(H)
    print('Certainty Matrix= ', np.array(certainty))

# scoreMatrix(A)
# accuracyMatrix(A)
# certaintyMatrix(A)

A= np.array([ [[0.3,0.6,1,-0.2,-0.54,-0.4], [0.1,0.2,0.8,-0.5,-0.34,-0.7] ],
 [[0.1,0.12,0,-0.27,-0.44,-0.92], [0.5,0.33,0.58,-0.33,-0.24,-0.22]],
 [ [0.11,0.22,0.6,-0.29,-0.24,-0.52],[0.22,0.63,0.88,-0.28,-0.54,-0.32] ]])
B= np.array([ [[0.32,0.4,0.1,-0.25,-0.54,-0.4], [0.13,0.2,0.11,-0.55,-0.35,-0.72] ],
 [[0.17,0.19,0.66,-0.87,-0.64,-0.92], [0.25,0.36,0.88,-0.33,-0.54,-0.22] ],
 [[0.15,0.28,0.67,-0.39,-0.27,-0.55],[0.24,0.73,0.28,-0.26,-0.53,-0.52] ]])
#A.shape gives (3, 2, 6) the dimension of A. (row, column, numbers of element (Bipolar Neutrosophic Number, 6 elements) )
# A.shape[0] = 3 rows
# A.shape[1] = 2 columns
# A.shape[2] = each bipolar neutrosophic number with 6 tuples as usual
sum=[]

def addition( A, B ):
 if A.shape == B.shape:
    dimA=A.shape
    for i in range (0,dimA[0]): # for rows, here 3
        H=[]
        for j in range (0,dimA[1]): # for columns, here 2
            H.extend([[A[i][j][0]+B[i][j][0]-A[i][j][0]*B[i][j][0], A[i][j][1]* B[i][j][1],A[i][j][2]* B[i][j][2] -(-A[i][j][3]*B[i][j][3]), -(-A[i][j][4]-B[i][j][4] -A[i][j][4]*B[i][j][4] ), -(-A[i][j][5]-B[i][j][5]-A[i][j][5]*B[i][j][5]) ]])
            sum.append(H)
 print('Sum= ', np.array(sum))

addition(A,B)