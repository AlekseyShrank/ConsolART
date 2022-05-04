
import cv2
import time
import os





class draw_console:

    def __init__(self, path = r"full\path\to\the\file"):
        self.path = path
        self.text_pixel = [" ", "▂", "▃", "▄", "▅", "▆", "▇", "█"]
        self.text_frame = []

    def video_to_frames(self):
        videoCapture = cv2.VideoCapture()
        print(self.path)
        videoCapture.open(self.path)
        fps = videoCapture.get(cv2.CAP_PROP_FPS)
        frames = videoCapture.get(cv2.CAP_PROP_FRAME_COUNT)
        print("fps=", int(fps), "frames=", int(frames))
        for i in range(10):
            os.system('cls')
            print(int(i/int(frames))*100,"%")
            ret, frame = videoCapture.read()
            frame = cv2.resize(frame, (384,54))
            self.frame_to_text(frame)

    def frame_to_text(self, frame):
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        height, width = img.shape
        textframe = [" " for i in range(height)]
        for y in range(height):
            s = ''
            for x in range(width):
                p = img[y, x]//32
                s = s + self.text_pixel[p]
            textframe[y] = s
        self.text_frame.append(textframe)

    def print_text(self):
        for tf in self.text_frame:
            os.system('cls')
            for y in range(54):
                print(tf[y])
            time.sleep(1/50)

    def save_text(self):
        i=1
        for tf in self.text_frame:
            f = open("textframe/%d.txt"%(i), "w+", encoding='utf-8')
            i+=1
            for y in range(54):
                f.write(tf[y] + '\n')
            f.close()







if __name__ == '__main__':
    test = draw_console()
    test.video_to_frames()
    test.save_text()





