class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        digits = {}
        for i in range(10):
            digits[i] = 0
        dec = ["1","2","3","4","5","6","7","8","9"]
        #add values to hashmap for each row
        for i in board:
            for j in i:
                if j in dec:
                    digits[int(j)] +=1
            #check if rows are valid
            for a in digits:
                if digits[a]>1:
                    return False
            #reset hashmap
            for b in digits:
                digits[b]=0
        

        #new hashmap for columns
        col = {}
        for i in range (10):
            col[i] = []
        
        #add values to hashmap that contains all col arrays
        for i in range(len(board)):
            for j in range(len(board[i])):
                col[j].append(board[i][j])
        
       
        #go through each col array and add to digit hashmap
        for i in range(len(col)):
            for j in col[i]:
                if j in dec:
                    digits[int(j)]+=1
            
            #check if rows are valid
            for a in digits:
                if digits[a]>1:
                    return False
            #reset hashmap
            for b in digits:
                digits[b]=0

           
            #new hashmap to store the subboxes arrays (from left to right its 1 2 3 then 4 5 6 then 7 8 9)
            subboxes = {}
            for i in range(9):
                subboxes[i]=[]

            
            #make a new array with each set of 3 x 3 so filter by 

            for i in range(len(board)):
                for j in range(len(board[i])):
                    if i<3 and j<3:
                        subboxes[0].append(board[i][j])
                    elif i<3 and j<6:
                        subboxes[1].append(board[i][j])
                    elif i<3 and j<9:
                        subboxes[2].append(board[i][j])
                    elif i<6 and j<3:
                        subboxes[3].append(board[i][j])
                    elif i<6 and j<6:
                        subboxes[4].append(board[i][j])
                    elif i<6 and j<9:
                        subboxes[5].append(board[i][j])
                    elif i<6 and j<9:
                        subboxes[5].append(board[i][j])
                    elif i<9 and j<3:
                        subboxes[6].append(board[i][j])
                    elif i<9 and j<6:
                        subboxes[7].append(board[i][j])
                    else:
                        subboxes[8].append(board[i][j])
            print(subboxes)
            #construct sub hashmap for each subbox and check
                    #go through each col array and add to digit hashmap
           
            for i in range(len(subboxes)):
                for j in subboxes[i]:
                    if j in dec:
                        digits[int(j)]+=1
                
                #check if rows are valid
                for a in digits:
                    if digits[a]>1:
                        return False
                #reset hashmap
                for b in digits:
                    digits[b]=0

                    


            

            

            

    
        
        return True





#create hashmap of keys 1-9 and if value is seen then we increase from 0 to 1 and if its more than 1 we return False

#