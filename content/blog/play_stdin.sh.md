title: play_stdin.sh
date: 2019-04-19

This simple set of scripts allows streaming audio between two Linux machines, for example a laptop and a Raspberry Pi. No audio backends such as Pulseaudio or JACK are required, the list of dependencies is very small.

It was born from frustration after discovering how difficult it was to stream music from a Pulseaudio-free laptop to my Raspberry Pi.

The scripts currently provide the following features:

* Streaming of any audio format supported by FFmpeg: wav, ogg, mp3, etc
* Pausing and stopping of audio from the client, which can be bound to media keys via xbindkeys

To download the scripts:

`git clone https://github.com/connor-brooks/play_stdin.sh.git`

For more information, find the scripts and README on GitHub [here](https://github.com/connor-brooks/play_stdin.sh).
