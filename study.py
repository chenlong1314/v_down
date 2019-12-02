import sys
from PyQt5.Qt import QUrl, QVideoWidget
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist
from PyQt5.QtWidgets import QApplication, QWidget


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.playlist = QMediaPlaylist(self)
        self.video_widget = QVideoWidget(self)              # 1
        self.video_widget.resize(self.width(), self.height())

        self.player = QMediaPlayer(self)
        self.player.setPlaylist(self.playlist)
        self.player.setVideoOutput(self.video_widget)       # 2

        self.playlist.addMedia(QMediaContent(QUrl.fromLocalFile('/Users/leif/PycharmProjects/v_down/images/mp4.mp4')))  # 3
        self.playlist.setPlaybackMode(QMediaPlaylist.Loop)
        self.playlist.setCurrentIndex(2)

        self.player.setVolume(80)
        self.player.play()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())