class Robot:
    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.pos = 0
        self.perimeter = 2 * (width + height - 2)
        self.moved = False

    def step(self, num: int) -> None:
        self.moved = True
        self.pos = (self.pos + num) % self.perimeter

    def getPos(self) -> list[int]:
        p = self.pos
        w, h = self.w, self.h
        
        if p < w:
            return [p, 0]
        if p < w + h - 1:
            return [w - 1, p - (w - 1)]
        if p < 2 * w + h - 2:
            return [w - 1 - (p - (w + h - 2)), h - 1]
        return [0, h - 1 - (p - (2 * w + h - 3))]

    def getDir(self) -> str:
        p = self.pos
        w, h = self.w, self.h
        
        if p == 0 and self.moved:
            return "South"
        
        if 0 < p < w:
            return "East"
        elif w <= p < w + h - 1:
            return "North"
        elif w + h - 1 <= p < 2 * w + h - 2:
            return "West"
        else:
            return "South" if self.moved else "East"


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
