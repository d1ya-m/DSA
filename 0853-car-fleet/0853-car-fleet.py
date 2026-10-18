class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:


        cars=[]

        n=len(speed)

        for i in range(n):
            cars.append([position[i], speed[i]])
        cars.sort(reverse=True) # L.sort() -> in place, no return value
                                # sorted(L) -> returns value, for immutable 

        stack=[]

        for pos, sp in cars:
            time=(target-pos)/sp
            if not stack or stack[-1]<time: 
                stack.append(time)
        return len(stack)
