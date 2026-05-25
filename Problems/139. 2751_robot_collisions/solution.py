class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        robots = []
        for i in range(n):
            robots.append([positions[i], healths[i], directions[i], i])
        robots.sort(key=lambda x: x[0])
        
        stack = [] 
        survivors = [] 
        
        for robot in robots:
            pos, health, direction, original_idx = robot
            
            if direction == 'R':
                stack.append(robot)
            else:
                while stack and stack[-1][2] == 'R' and health > 0:
                    top_robot = stack[-1]
                    
                    if top_robot[1] > health:
                        top_robot[1] -= 1
                        health = 0   
                    elif top_robot[1] < health:
                        stack.pop()      
                        health -= 1       
                    else:
                        stack.pop()       
                        health = 0   
                if health > 0:
                    survivors.append([pos, health, direction, original_idx])
        survivors.extend(stack)
        survivors.sort(key=lambda x: x[3])
        return [r[1] for r in survivors]
