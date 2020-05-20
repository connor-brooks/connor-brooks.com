title: play_stdin.sh
importance: 3

![alt text](/static/images/projects/play_stdin.sh.png)

This simple set of bash scripts allows streaming audio between two Linux machines, for example a laptop and a Raspberry Pi. No audio backends such as Pulseaudio or JACK are required, the list of dependencies is very small.

It was born from frustration after discovering how difficult it was to stream music from a Pulseaudio-free laptop to my Raspberry Pi.

The scripts currently provide the following features:

* Streaming of any audio format supported by FFmpeg: wav, ogg, mp3, etc
* Pausing and stopping of audio from the client, which can be bound to media keys via xbindkeys

## Links
* [GitHub](https://github.com/connor-brooks/play_stdin.sh)
* [Hackaday](https://hackaday.com/2019/05/02/raspberry-pi-streams-music-using-only-the-default-linux-tools/)
