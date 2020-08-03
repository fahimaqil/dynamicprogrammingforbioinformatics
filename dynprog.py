import numpy as np
import time
#put ALL your code here
#compare both sequence
def countScore(newSeq1,newSeq2,input1,matrix):
    answerArray=[]
    seq1=newSeq1
    seq2=newSeq2

    count1=0
    count2=0
    maxAlignment=0
    global arrayCount
    arrayCount=[]
    global backTrack
    mat=np.zeros(shape=(len(newSeq2)+1,len(newSeq1)+1,)).astype(int)
    backTrack=np.zeros(shape=(len(newSeq2)+1,len(newSeq1)+1)).astype(int).astype(str)
    for let2 in seq2:
        count2+=1
        for let1 in seq1:
            count1+=1

            mat[count2][count1]=putScore(count2,count1,mat,matrix,let2,let1,input1)
            if maxAlignment<= mat[count2][count1]:
                maxAlignment=mat[count2][count1]
                arrayCount=[count2,count1]
        count1=0
    global array1
    array1=[]
    global array2
    array2=[]
    answerArray.append(maxAlignment)
    #print("arrayCount ",arrayCount)
    x=arrayCount[0]
    y=arrayCount[1]
    recurse=True
    while (recurse):
        x,y,recurse=backTracking(x,y)
        

    answerArray=[maxAlignment, array2[::-1],array1[::-1]]
    return answerArray
#scan the input and then compare it with the equal letter
def subsMatrix(matrix,let1,let2,input1):
   
    count=-1
    count1=0
    count2=0
    
    if let1==let2:
        for i in input1:
            count+=1
            if i==let1:
                return matrix[count][count]
    else:
        for i in input1:
            count+=1
            if i==let1:
                count1=count
            if i==let2:
                count2=count 
        return(matrix[count2][count1])
            
        
        
        
            
def putScore(count2,count1,mat,matrix,let2,let1,input1):
    
    arrayScore=[0]
    scoreXY=0
    scoreX=0
    scoreY=0
    scoreXY=subsMatrix(matrix,let1,let2,input1)+mat[count2-1][count1-1]
    scoreY=subsMatrix(matrix,let2," ",input1)+mat[count2-1][count1]
    #horizontalrow
    scoreX=subsMatrix(matrix," ",let1,input1)+mat[count2][count1-1]
    arrayScore.append(scoreXY)
    arrayScore.append(scoreY)
    arrayScore.append(scoreX)
    highest=max(arrayScore)
 
    
    if scoreY==highest:
        backTrack[count2][count1]="U"
    if scoreX==highest: 
        backTrack[count2][count1]="L"
    if scoreXY==highest:
        backTrack[count2][count1]="D"
    if highest==0:
        backTrack[count2][count1]="0"

        
    return highest
def backTracking(count1,count2):
    x=count1
    y=count2
    if backTrack[x][y]=="D":
        x=x-1
        y=y-1
        array1.append(x)
        array2.append(y)
        return x,y,True

    elif backTrack[x][y]=="L":
        y=y-1
        return x,y,True


    elif backTrack[x][y]=="U":
        x=x-1
        return x,y,True

    else:
        return x,y,False
    ##backTracking(x,y)

                                                                                                                                                                                                                               
    
def dynprog(a,b,c,d):
    start = time.time()

    newScore= a+" "
    newSeq1=c
    newSeq2=d
    scoreMatrix=b
    new=countScore(newSeq1,newSeq2,newScore,scoreMatrix)
    end = time.time()
    time_taken = end - start
    print(time_taken)
    return new

a = dynprog ("ABCD", [

[ 1,-5,-5,-5,-1],

[-5, 1,-5,-5,-1],

[-5,-5, 5,-5,-4],

[-5,-5,-5, 6,-4],

[-1,-1,-4,-4,-9]],"DDCDDCCCDCAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCCCDDDCDADCDCDCDCD", "DDCDDCCCDCBCCCCDDDCDBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBDCDCDCDCD"
)

   #your code

print(a)
