class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        exploreList = []
        explored = set()
        answer = 0
        counter = 0
        numberOfNodes  = len(grid[0])
        for i in range(len(grid)):
            for j in range(numberOfNodes):
                if i*numberOfNodes + j in explored:
                    continue
                if grid[i][j] == 1:
                    exploreList.append([i,j])
                    counter = 0
            
                while(exploreList):
                    Node = exploreList.pop(0)
                    if(Node[0] * numberOfNodes + Node[1] in explored or grid[Node[0]][Node[1]] == 0):
                        explored.add(Node[0] * numberOfNodes + Node[1])
                        continue
                    counter+=1
                    explored.add(Node[0] * numberOfNodes + Node[1])
                    if(Node[0]-1 >=0):
                        exploreList.append([Node[0]-1,Node[1]])
                    if(Node[0]+1 < len(grid)):
                        exploreList.append([Node[0]+1,Node[1]])
                    if(Node[1]-1 >= 0):
                        exploreList.append([Node[0],Node[1]-1])
                    if(Node[1]+1 < numberOfNodes):
                        exploreList.append([Node[0],Node[1]+1])
                    answer = max(answer , counter)
        return answer