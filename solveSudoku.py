class Sudoku:
    def __init__(self,data):
        self.data=data
    def output(self):
        print('--------------------------------')
        for i in range(len(self.data)):
            if (i%3==0 and i!=0) or i==9:
                print('--------------------------------')
            for j in range (len(self.data[i])):
                if (j%3==0) or j==9:
                    print('|',end=' ')
                print(f"{self.data[i][j]} ",end=" ")
            print()
    def findnull(self):
        for i in range(0,len(self.data)):
            for j in range(0,len(self.data[i])):
                if self.data[i][j]==0:
                    return i,j
        return None
    def isValid(self,number,pos):
        #check row
        for i in range(0,len(self.data[pos[0]])):
            if self.data[pos[0]][i]==number and pos[1]!=i:
                return False
        #check column
        for i in range(0,len(self.data)):
            if self.data[i][pos[1]]==number and pos[0]!=i:
                return False
        #check box
        box_x=pos[1]//3
        box_y=pos[0]//3
        for i in range(box_y*3,box_y*3+3):
            for j in range(box_x*3,box_x*3+3):
                if self.data[i][j]==number and (i,j)!=pos:
                    return False
        return True
    def solve(self):
        find=self.findnull() 
        if not find:
            return True
        else:
            row,col=find
        count=0
        for i in range(1,10):
            if self.isValid(number=i,pos=(row,col)):
                self.data[row][col]=i
                if self.solve():
                    return True
                self.data[row][col]=0
            count+=1
            if count==10:
                raise Exception("No solution")
                
        return False
if __name__ == "__main__":
    data=[ 
    [ 7 , 8 , 0 , 4 , 0 , 0 , 1 , 2 , 0 ], 
    [ 6 , 0 , 0 , 0 , 7 , 5 , 0 , 0 , 9 ], 
    [ 0 , 0 , 0 , 6 , 0 , 1 , 0 , 7 , 8 ],
    [ 0 , 0 , 7 , 0 , 4 , 0 , 2 , 6 , 0 ], 
    [ 0 , 0 , 1 , 0 , 5 , 0 , 9 , 3 , 0 ], 
    [ 9 , 0 , 4 , 0 , 6 , 0 , 0 , 0 , 5 ], 
    [ 0 , 7, 0 , 3 , 0 , 0 , 0 , 1 , 2 ], 
    [ 1 , 2 , 0 , 0 , 0 , 7 , 4 , 0 , 0 ], 
    [ 0 , 4 , 9 , 2 , 0 , 6 , 0 , 0 , 7 ] 
]
    sodoku=Sudoku(data)
    sodoku.solve()
    sodoku.output()