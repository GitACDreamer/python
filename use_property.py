'使用@property' 

class Screen(object):
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self , width):
        self.__width = width
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self , height):
        self.__height = height
    @property
    def resolution(self):
        return self.__width * self.__height

def main():
    screen = Screen()
    screen.width = 1024
    screen.height = 1080
    print('width*height=',screen.resolution)

if __name__ == '__main__':
    main()