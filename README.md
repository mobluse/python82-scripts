# python82-scripts
Scripts for the Python82 App in the TI-82 Advanced Edition Python graphing calculator. They have been tested with V5.6.3.0017 of the Python82 App.

In the Python82 App "\x1B[%d;%dm"%(fg,bg) for changing color doesn't follow the standard for ANSI/VT100/xterm escape codes since the color codes 
are 0-15 in TI-82 Python, and in the standard they are different and have different codes for foreground and background, respectively, and then 
you don't need to place them in order, and can change foreground and background independently. I also discovered that "\x1B[%d;%dH"%(row,col) 
works for positioning the cursor, but that is standard ANSI/VT100/xterm. In TI-82 home is at (0, 0), but in the standard, at (1, 1). Also 
"\x1B[2J" works for clearing the screen, but it also moves the cursor to home, which is non-standard; it should stay where it was. "\x1B[0J" 
and "\x1B[1J" are ignored. I also discovered that "\x1B[0K" and "\x1B[K" works as they should; they clear from cursor to end of line, but 
"\x1B[1K" and "\x1B[2K" do the same as "\x1B[0K", which is non-standard. Do you know what terminal standard TI follows?

It would be better if the CSI codes followed the standard because then students would learn useful and true things and it would be easier to 
get the programs to run in Python or Micropython on other platforms. I don't mean you have to implement ANSI/VT100/xterm escape codes fully, 
but those that work should work according to standard. But if you don't have time to update them, it's better to keep them as now than to 
remove them completely, because that would make the calculator less useful. Does Python82 support more escape codes?
