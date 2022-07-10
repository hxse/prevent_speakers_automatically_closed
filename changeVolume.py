#!/usr/bin/env python3
# coding: utf-8
from pycaw.pycaw import AudioUtilities


def setVolume(num: float = 1):
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session.SimpleAudioVolume
        if session.Process and session.Process.name() == "prevent_auto_closed.exe":
            # volume.SetMasterVolume(volume.GetMasterVolume() + 0.01, None)
            volume.SetMasterVolume(num, None)
            # volume.SetMute(1, None)
        else:
            # volume.SetMute(1, None)
            pass


if __name__ == "__main__":
    setVolume()
