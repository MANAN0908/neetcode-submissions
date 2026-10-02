class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        cars=sorted(zip(position,speed),reverse=True)
        fleet=0
        for i in range(len(cars)):
            pos,spd=cars[i]
            time=((target-pos)/spd)
            if stack and time<=stack[-1]:
                pass
            
            else:
                stack.append(time)
                fleet+=1
        return len(stack)