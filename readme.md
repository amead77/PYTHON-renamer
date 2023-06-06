# renamer for mp3 files to correct filenames to my specification

this converts the files in a directory from the format: The [artist] - [track].[ext] to [artist], The - [track].[ext]
example: The Beatles - Hey Jude.mp3 --> Beatles, The - Hey Jude.mp3
it isn't perfect, but it works for my purposes
I used chatgpt for the regex, because I'm lazy.
should work on windows and linux, i tested it on windows
i made the directory hardcoded to make sure you know what you're doing, failure could result in corrupted file names on files you didn't want to rename

test first with --test, then run with --run

technobug 2023, no licence, do whatever you want with it, i don't care
