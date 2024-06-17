# python82-scripts
Here are scripts for the Python82 App in the *TI-82 Advanced Edition Python* graphing calculator. They have been tested with V5.6.3.0017 of the Python82 App. 
The Python82 programs have uppercase names with a maximum of 8 characters, because that is a limitation in the calculator. For some programs there are also
versions for CPython (i.e. ordinary Python3) and [Snek](https://sneklang.org/doc/snek.html). They have been tested with Python 3.6.9, Python 3.11.2, and Snek 1.9. 
The CPython program name ends in _C, and the Snek, ends in _s. Sometimes the same program works in both CPython and Snek and then the name ends with _Cs.

I have made a library, AtCo, for each python-type language that contains the differences between the pythons so that the main program can be the same.

In the Python82 App "\x1B[%d;%dm"%(fg,bg) for changing color doesn't follow the standard for
[ANSI](https://en.wikipedia.org/wiki/ANSI_escape_code)/[VT100/xterm](https://learn.microsoft.com/en-us/windows/console/console-virtual-terminal-sequences)
escape codes since the color codes are 0-15 in TI-82 Python, and in the standard they are different and have different codes for foreground and 
background, respectively, and then you don't need to place them in order, and can change foreground and background independently. Color 8 in Python82, 
brightest gray, doesn't exist as a one number colorcode in ANSI/VT100/xterm and for that I used the remaining colorcode: bright green. 
I also discovered that "\x1B[%d;%dH"%(row,col) works for positioning the cursor, but that is standard ANSI/VT100/xterm. In Python82 home is at (0, 0), 
but in the standard, at (1, 1). Also "\x1B[2J" works for clearing the screen, but it also moves the cursor to home, which is non-standard; it should 
stay where it was. "\x1B[J", "\x1B[0J", and "\x1B[1J" are ignored. I also discovered that "\x1B[K" and "\x1B[0K" work as they should; they clear from cursor 
to end of line, but "\x1B[1K" and "\x1B[2K" do the same as "\x1B[0K", which is non-standard. In the ANSI/VT100/xterm standard "\x1B[2J" and "\x1B[K" use
the current foreground and background colors, but in Python82 they first change the current colors to black on bright white. "\n" and "\b" work as in the Python3
shell, but "\t" only types two spaces and doesn't jump to tab stops. "\r" is ignored, but in the Python3 shell move the cursor to the beginning of the 
current line. Do you know what terminal standard TI follows?

It would be better if the escape codes followed the standard because then students would learn useful and true things and it would be easier to 
get the programs to run in Python or Micropython on other platforms. I don't mean Texas Instruments have to implement all ANSI/VT100/xterm escape codes fully, 
but those that work should work according to the standard (xterm). But if TI doesn't have time to update them, it's better to keep them as now than to 
remove them completely, because that would make the calculator less useful. Does Python82 support more escape codes? The program COLORS.py can be used to
discover working Escape codes and Control codes.

One script, FLAPPBAT.py (i.e. Flappy Bat), is an arcade game where you control the height of a bat using Enter/Entrer several times to eat moths. 
This game could be improved to have several moths on screen at the same time.
