def print_val(index):
    if(shift):
        if(arr_shift[index]=="space"):
            print(" ",end="")
        elif (arr_shift[index]=="newline"):
            print("\n",end="")
        else:
            print(arr_shift[index],end="")
    else:
        if(arr[index]=="space"):
            print(" ",end="")
        elif (arr[index]=="newline"):
            print("\n",end="")
        else:
            print(arr[index],end="")
    return 0
        
arr=["RESERVED","Esc","1","2","3","4","5","6","7","8","9","0","-","=","b_space","Tab","q","w","e","r","t","y","u","i","o","p","[","]","\n","L_CTRL","a","s","d","f","g","h","j","k","l",";","'","`","l_SHIFT","\\","z","x","c","v","b","n","m",",",".","/","R_SHIFT","KPASTERISK","L_ALT"," ","CAPSLOCK","F1","F2","F3","F4","F5","F6","F7","F8","F9","F10","NUMLOCK","SCROLLLOCK","KP7","KP8","KP9","-","KP4","KP5","KP6","+","KP1","KP2","KP3","KP0","KPDOT","UNKNOWN","ZENKAKUHANKAKU","102ND","F11","F12","RO","KATAKANA","HIRAGANA","HENKAN","KATAKANAHIRAGANA","MUHENKAN","KPJPCOMMA","KPENTER","RIGHTCTRL","KPSLASH","SYSRQ","RIGHTALT","LINEFEED","HOME","UP","PAGEUP","LEFT","RIGHT","END","DOWN","PAGEDOWN","INSERT","DELETE","MACRO","MUTE","VOLUMEDOWN","VOLUMEUP","POWER","KPEQUAL","KPPLUSMINUS","PAUSE","SCALE","KPCOMMA","HANGEUL","HANJA","YEN","LEFTMETA","RIGHTMETA","COMPOSE","STOP","AGAIN","PROPS","UNDO","FRONT","COPY","OPEN","PASTE","FIND","CUT","HELP","MENU","CALC","SETUP","SLEEP","WAKEUP","FILE","SENDFILE","DELETEFILE","XFER","PROG1","PROG2","WWW","MSDOS","COFFEE","DIRECTION","CYCLEWINDOWS","MAIL","BOOKMARKS","COMPUTER","BACK","FORWARD","CLOSECD","EJECTCD","EJECTCLOSECD","NEXTSONG","PLAYPAUSE","PREVIOUSSONG","STOPCD","RECORD","REWIND","PHONE","ISO","CONFIG","HOMEPAGE","REFRESH","EXIT","MOVE","EDIT","SCROLLUP","SCROLLDOWN","KPLEFTPAREN","KPRIGHTPAREN","NEW","REDO","F13","F14","F15","F16","F17","F18","F19","F20","F21","F22","F23","F24","UNKNOWN","UNKNOWN","UNKNOWN","UNKNOWN","UNKNOWN","PLAYCD","PAUSECD","PROG3","PROG4","DASHBOARD","SUSPEND","CLOSE","PLAY","FASTFORWARD","BASSBOOST","PRINT","HP","CAMERA","SOUND","QUESTION","EMAIL","CHAT","SEARCH","CONNECT","FINANCE","SPORT","SHOP","ALTERASE","CANCEL","BRIGHTNESSDOWN","BRIGHTNESSUP","MEDIA","SWITCHVIDEOMODE","KBDILLUMTOGGLE","KBDILLUMDOWN","KBDILLUMUP","SEND","REPLY","FORWARDMAIL","SAVE","DOCUMENTS","BATTERY","BLUETOOTH","WLAN","UWB","UNKNOWN","VIDEO_NEXT","VIDEO_PREV","BRIGHTNESS_CYCLE","BRIGHTNESS_ZERO","DISPLAY_OFF","WIMAX"]
arr_shift=["⇧RESERVED⇩","⇧Esc⇩","!","@","#","$","%","^","&","*","(",")","_","+","⇧b_space⇩","⇧Tab⇩","Q","W","E","R","T","Y","U","I","O","P","{","}","newline","⇧L_CTRL⇩","A","S","D","F","G","H","J","K","L",":","\"","~","⇧l_SHIFT⇩","|","Z","X","C","V","B","N","M","<",">","?","⇧R_SHIFT⇩","⇧KPASTERISK⇩","⇧L_ALT⇩","space","⇧CAPSLOCK⇩","⇧F1⇩","⇧F2⇩","⇧F3⇩","⇧F4⇩","⇧F5⇩","⇧F6⇩","⇧F7⇩","⇧F8⇩","⇧F9⇩","⇧F10⇩","⇧NUMLOCK⇩","⇧SCROLLLOCK⇩","⇧KP7⇩","⇧KP8⇩","⇧KP9⇩","⇧-⇩","⇧KP4⇩","⇧KP5⇩","⇧KP6⇩","⇧+⇩","⇧KP1⇩","⇧KP2⇩","⇧KP3⇩","⇧KP0⇩","⇧KPDOT⇩","⇧UNKNOWN⇩","⇧ZENKAKUHANKAKU⇩","⇧102ND⇩","⇧F11⇩","⇧F12⇩","⇧RO⇩","⇧KATAKANA⇩","⇧HIRAGANA⇩","⇧HENKAN⇩","⇧KATAKANAHIRAGANA⇩","⇧MUHENKAN⇩","⇧KPJPCOMMA⇩","⇧KPENTER⇩","⇧RIGHTCTRL⇩","⇧KPSLASH⇩","⇧SYSRQ⇩","⇧RIGHTALT⇩","⇧LINEFEED⇩","⇧HOME⇩","⇧UP⇩","⇧PAGEUP⇩","⇧LEFT⇩","⇧RIGHT⇩","⇧END⇩","⇧DOWN⇩","⇧PAGEDOWN⇩","⇧INSERT⇩","⇧DELETE⇩","⇧MACRO⇩","⇧MUTE⇩","⇧VOLUMEDOWN⇩","⇧VOLUMEUP⇩","⇧POWER⇩","⇧KPEQUAL⇩","⇧KPPLUSMINUS⇩","⇧PAUSE⇩","⇧SCALE⇩","⇧KPCOMMA⇩","⇧HANGEUL⇩","⇧HANJA⇩","⇧YEN⇩","⇧LEFTMETA⇩","⇧RIGHTMETA⇩","⇧COMPOSE⇩","⇧STOP⇩","⇧AGAIN⇩","⇧PROPS⇩","⇧UNDO⇩","⇧FRONT⇩","⇧COPY⇩","⇧OPEN⇩","⇧PASTE⇩","⇧FIND⇩","⇧CUT⇩","⇧HELP⇩","⇧MENU⇩","⇧CALC⇩","⇧SETUP⇩","⇧SLEEP⇩","⇧WAKEUP⇩","⇧FILE⇩","⇧SENDFILE⇩","⇧DELETEFILE⇩","⇧XFER⇩","⇧PROG1⇩","⇧PROG2⇩","⇧WWW⇩","⇧MSDOS⇩","⇧COFFEE⇩","⇧DIRECTION⇩","⇧CYCLEWINDOWS⇩","⇧MAIL⇩","⇧BOOKMARKS⇩","⇧COMPUTER⇩","⇧BACK⇩","⇧FORWARD⇩","⇧CLOSECD⇩","⇧EJECTCD⇩","⇧EJECTCLOSECD⇩","⇧NEXTSONG⇩","⇧PLAYPAUSE⇩","⇧PREVIOUSSONG⇩","⇧STOPCD⇩","⇧RECORD⇩","⇧REWIND⇩","⇧PHONE⇩","⇧ISO⇩","⇧CONFIG⇩","⇧HOMEPAGE⇩","⇧REFRESH⇩","⇧EXIT⇩","⇧MOVE⇩","⇧EDIT⇩","⇧SCROLLUP⇩","⇧SCROLLDOWN⇩","⇧KPLEFTPAREN⇩","⇧KPRIGHTPAREN⇩","⇧NEW⇩","⇧REDO⇩","⇧F13⇩","⇧F14⇩","⇧F15⇩","⇧F16⇩","⇧F17⇩","⇧F18⇩","⇧F19⇩","⇧F20⇩","⇧F21⇩","⇧F22⇩","⇧F23⇩","⇧F24⇩","⇧UNKNOWN⇩","⇧UNKNOWN⇩","⇧UNKNOWN⇩","⇧UNKNOWN⇩","⇧UNKNOWN⇩","⇧PLAYCD⇩","⇧PAUSECD⇩","⇧PROG3⇩","⇧PROG4⇩","⇧DASHBOARD⇩","⇧SUSPEND⇩","⇧CLOSE⇩","⇧PLAY⇩","⇧FASTFORWARD⇩","⇧BASSBOOST⇩","⇧PRINT⇩","⇧HP⇩","⇧CAMERA⇩","⇧SOUND⇩","⇧QUESTION⇩","⇧EMAIL⇩","⇧CHAT⇩","⇧SEARCH⇩","⇧CONNECT⇩","⇧FINANCE⇩","⇧SPORT⇩","⇧SHOP⇩","⇧ALTERASE⇩","⇧CANCEL⇩","⇧BRIGHTNESSDOWN⇩","⇧BRIGHTNESSUP⇩","⇧MEDIA⇩","⇧SWITCHVIDEOMODE⇩","⇧KBDILLUMTOGGLE⇩","⇧KBDILLUMDOWN⇩","⇧KBDILLUMUP⇩","⇧SEND⇩","⇧REPLY⇩","⇧FORWARDMAIL⇩","⇧SAVE⇩","⇧DOCUMENTS⇩","⇧BATTERY⇩","⇧BLUETOOTH⇩","⇧WLAN⇩","⇧UWB⇩","⇧UNKNOWN⇩","⇧VIDEO_NEXT⇩","⇧VIDEO_PREV⇩","⇧BRIGHTNESS_CYCLE⇩","⇧BRIGHTNESS_ZERO⇩","⇧DISPLAY_OFF⇩","⇧WIMAX⇩"]
shift=0
file=open("./Log.txt","r")
for items in file:
    new_lst=items.split(" ")[:-1]
for index in new_lst:
    index=int(index)
    if(index==42 or index==54):
        if(shift):
            shift=0
            continue
        else:
            shift=1
            continue
    if(shift):
        print_val(index)
    else:
        print_val(index)
