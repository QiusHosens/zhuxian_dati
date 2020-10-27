from Appkit import NSEvent

pressID = [None, kCGEventLeftMouseDown, kCGEventRightMouseDown, kCGEventOtherMouseDown]
releaseID = [None, kCGEventLeftMouseUp, kCGEventRightMouseUp, kCGEventOtherMouseUp]

class PyMouse():
    def press(self, x, y, button = 1):
        event = CGEventCreateMouseEvent(None, pressID[button], (x, y), button - 1)
        CGEventPost(KCGHIDEventTap, event)

    def release(self, x, y, button = 1):
        event = CGEventCreateMouseEvent(None, releaseID[button], (x, y), button - 1)
        CGEventPost(KCGHIDEventTap, event)

    def move(self, x, y):
        move = CGEventCreateMouseEvent(None, kCGEventMouseMoved, (x, y), 0)
        CGEventPost(kCGHIDEventTap, move)

    def position(self):
        loc = NSEvent.mouseLocation()
        return loc.x, CGDisplayPixelsHigh(0) - loc.y

    def screen_size(self):
        return CGDisplayPixelsWide(0), CGDisplayPixelsHigh(0)

    def click(self, x, y, button = 1):
        self.press(x, y, button)
        self.release(x, y, button)