class Clock:
    id = None
    price = None
    def ring (self):
        import winsound
        winsound.Beep(2000, 3000)   # 让电脑闹钟响起来
clock1 = Clock()
clock1.ring()