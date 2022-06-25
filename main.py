from hashlib import new
from create_blank_audio import create_blank_audio

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtCore import *


app = QApplication([])
app.setQuitOnLastWindowClosed(False)

# Create the icon
icon = QIcon("icon.png")

# Create the tray
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)


def show_tray_message(tray: QSystemTrayIcon):
    notificationTitle = self.notification_title.text()
    notificationMessage = self.notification_message.toPlainText()
    icon = QIcon(":/icons/feather/info.svg")
    duration = 3 * 1000  # 3 seconds

    if len(notificationTitle) == 0 or len(notificationMessage) == 0:
        tray.showMessage(
            "Input Something",
            "Enter your notification tittle and message",
            icon,
            duration,
        )
    else:
        tray.showMessage(notificationTitle, notificationMessage, icon, duration)


menu = QMenu()


# def set_duration(duration):
#     player.stop()
#     playlist.clear()
#     out_sound = create_blank_audio(sound, duration)

#     # playlist = QMediaPlaylist()
#     qUrl = QUrl.fromLocalFile(out_sound)
#     playlist.addMedia(QMediaContent(qUrl))
#     playlist.setPlaybackMode(QMediaPlaylist.Loop)
#     player.play()


# actionArr = []
# # Create the menu
# for idx, value in enumerate(
#     [
#         [500, "500ms"],
#         [1000, "1s"],
#         [1000 * 5, "5s"],
#         [1000 * 10, "10s"],
#         [1000 * 60, "1min"],
#         [1000 * 60 * 3, "3min"],
#         [1000 * 60 * 5, "5min"],
#         [1000 * 60 * 10, "10min"],
#         # [1000 * 60 * 15, "15min"],
#         # [1000 * 60 * 30, "30min"],
#         # [1000 * 60 * 60 * 1, "1h"],
#         # [1000 * 60 * 60 * 3, "3h"],
#         # [1000 * 60 * 60 * 6, "6h"],
#         # [1000 * 60 * 60 * 12, "12h"],
#         # [1000 * 60 * 60 * 24, "24h"],
#     ],
# ):
#     [time, text] = value
#     actionArr.append(QAction(f"set time interval {text}"))
#     actionArr[idx].triggered.connect(lambda: set_duration(1000))
#     menu.addAction(actionArr[idx])


# Add a Quit option to the menu.
quit = QAction("Quit")
quit.triggered.connect(app.quit)
menu.addAction(quit)

# Add the menu to the tray
tray.setContextMenu(menu)


sound = "./Silent white noise.wav"
sound = "./武士刀摆动_爱给网_aigei_com.wav"
out_sound = create_blank_audio(sound, 1000 * 60 * 3)

playlist = QMediaPlaylist()
qUrl = QUrl.fromLocalFile(out_sound)
playlist.addMedia(QMediaContent(qUrl))
playlist.setPlaybackMode(QMediaPlaylist.Loop)


player = QMediaPlayer()
player.setPlaylist(playlist)
player.play()

app.exec_()
