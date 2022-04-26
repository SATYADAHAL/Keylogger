# Introduction 
This is simple keylogger created for <b>Linux</b>. It was written in C++ and Python3. This is a very simple keylogger that gives idea about how keystrokes can be logged into a file.
# Table of Content
   1. [What is a Keylogger?](#keylogger)
   2. [Disclaimer](#disclaimer)
   3. [Installation](#installation)
   4. [Decoding](#decoding-the-log-file)
   5. [Working of Keylogger](#working-of-keylogger)
   6. [LISCENCE](https://github.com/SATYADAHAL/Keylogger/blob/main/LICENSE)
# Keylogger
A keylogger is software/hardware that logs/stores the consecutive keystrokes made by a computer user. Keylogger can be really dangerous because they can log the all the keystrokes like username,password,emails,credit card information etc. entered by user. Keylogger is considered to be computer malware, to be specific it is a [spyware](https://en.wikipedia.org/wiki/Spyware). I was curious how would keylogger actullay work. I did some research on linux input system and wrote my own keylogger.

# Disclaimer
<B>TO BE USED FOR EDUCATIONAL PUROPSES ONLY</B><BR><BR>
The purpose of creating this keylogger was for educational purpose and help people understand the working of keylogger. I am not responsible for any misuse or damage cause by this program.You cannot use this this software to test person or company without their permission.
# INSTALLATION
    git clone https://github.com/SATYADAHAL/Keylogger.git
    cd Keylogger
    g++ keylogger.cpp -o keylogger
    sudo ./keylogger
<b>  Note: You will need root permission to run this program.</b>
# Decoding the log file
  Althought the file is not encoded as in encoding but it has the keystorkes as their corresponding integer value. This python script is just to convert the integer value into human redable form.
  
  ````
  python3 decoder.py
  ````
  Above command will ouput keystrokes to stdout which might not be convienient. So yo can throw the ouput to a text file using the command below.
  ````
  python3 decoder.py > output.txt
  ````
  Note: "Log.txt" and "decoder.py" must be in a same directory. By default they are in same directory so better not change the directory.
  
# Working of Keylogger
  In linux the when the some key is pressed, the data is processed by device driver in the kernel space and then it is passed to Input Event Hanlders
  through input core subsystem. After the data reaches the input event handlers it is now passed to userspace. In userspace the input event is stored in "/dev/input/" folder as a character file. If use use ```ls -l /dev/input``` we get following output.
  ```
  drwxr-xr-x root root  100 B Mon Apr 25 12:10:06 2022  by-id
drwxr-xr-x root root  240 B Mon Apr 25 12:10:06 2022  by-path
crw-rw---- root input   0 B Sun Apr 24 15:23:09 2022  event0
crw-rw---- root input   0 B Sun Apr 24 15:23:09 2022  event1
crw-rw---- root input   0 B Sun Apr 24 15:23:12 2022  event10
crw-rw---- root input   0 B Sun Apr 24 15:23:12 2022  event11
crw-rw---- root input   0 B Sun Apr 24 15:23:13 2022  event12
crw-rw---- root input   0 B Sun Apr 24 15:23:14 2022  event13
crw-rw---- root input   0 B Sun Apr 24 15:23:14 2022  event14
crw-rw---- root input   0 B Sun Apr 24 15:23:14 2022  event15
crw-rw---- root input   0 B Sun Apr 24 15:23:14 2022  event16
crw-rw---- root input   0 B Sun Apr 24 15:23:09 2022  event2
crw-rw---- root input   0 B Sun Apr 24 15:23:10 2022  event3
crw-rw---- root input   0 B Sun Apr 24 15:23:10 2022  event4
crw-rw---- root input   0 B Mon Apr 25 12:10:06 2022  event5
crw-rw---- root input   0 B Sun Apr 24 15:23:13 2022  event6
crw-rw---- root input   0 B Sun Apr 24 15:23:13 2022  event7
crw-rw---- root input   0 B Sun Apr 24 15:23:12 2022  event8
crw-rw---- root input   0 B Sun Apr 24 15:23:12 2022  event9
crw-rw---- root input   0 B Sun Apr 24 15:23:12 2022  mice
crw-rw---- root input   0 B Mon Apr 25 12:10:06 2022  mouse0
crw-rw---- root input   0 B Sun Apr 24 15:23:13 2022  mouse1
crw-rw---- root input   0 B Sun Apr 24 15:23:13 2022  mouse2
```
As we can see that there are many events files but we only need event file of our keyboard. We can get this information in "/proc/bus/input/devices" file
  . If we do ```cat /proc/bus/input/devices``` we get following output: 
  ```
  I: Bus=0019 Vendor=0000 Product=0005 Version=0000
N: Name="Lid Switch"
P: Phys=PNP0C0D/button/input0
S: Sysfs=/devices/LNXSYSTM:00/LNXSYBUS:00/PNP0C0D:00/input/input0
U: Uniq=
H: Handlers=event0 
B: PROP=0
B: EV=21
B: SW=1

I: Bus=0019 Vendor=0000 Product=0001 Version=0000
N: Name="Power Button"
P: Phys=PNP0C0C/button/input0
S: Sysfs=/devices/LNXSYSTM:00/LNXSYBUS:00/PNP0C0C:00/input/input1
U: Uniq=
H: Handlers=kbd event1 
B: PROP=0
B: EV=3
B: KEY=10000000000000 0

I: Bus=0011 Vendor=0001 Product=0001 Version=ab41
N: Name="AT Translated Set 2 keyboard"
P: Phys=isa0060/serio0/input0
S: Sysfs=/devices/platform/i8042/serio0/input/input2
U: Uniq=
H: Handlers=sysrq kbd leds event2 
B: PROP=0
B: EV=120013
B: KEY=1100f02902000 8380307cf910f001 feffffdfffefffff fffffffffffffffe
B: MSC=10
B: LED=7
  .
  .
  . 
  and so on
```
  Now we need to look for line where ```H: Handlers=sysrq kdb``` and also check in same section check for line ```B: EV=120013```. If this condition is satisifed we can look at the end of  ```H: Handlers=sysrq kdb``` line to get the event name. In my case it is event2.
 <br> After this we can focus on our event file.<br>This is a character file and it cannot be read directly to get the keystrokes. So we need to put this data of this event file into a strcture called input_event which is defined in [<linux/input.h>](https://github.com/torvalds/linux/blob/master/include/uapi/linux/input.h). <br>For more information check [documentation](https://www.kernel.org/doc/Documentation/input/input.txt).<br>
  The input_event structure is shown below<br>
> struct input_event {<br>
>	struct timeval time;<br>
>	unsigned short type;<br>
>	unsigned short code;<br>
>	unsigned int value;<br>
> };<br>

  This strucutre is of 24 bytes. First 16 bytes is occpuied by timeval structure. And remaining is occuped by the 'type,code,value' variables.<br>
  Lets understand this structre:<br>
  1. timeval time is a structure that stores time when the keyevent occured.<br>
  2. type contians the value which deterimes the type of event(like EV_KEY,EV_REL).<br>
  3. code determines the keypress,keyrelease,keyrepeat etc.<br>
  4. value is the key value like KEY_A(for A,a)<br>
  For more information check out linux input-events [documentation](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/include/uapi/linux/input-event-codes.h)<br>

  Now when we finally have our data into the strcutre we can process the data and log it into the file.But we have to be careful not to log both keypress and keyrelease as this might cause problem. We can just store any of these. And we have to deal with shift-modifiers too.<br>
  
  
  
  
  
