import subprocess

#subprocess.run("getEpg.bat",shell=True)
subprocess.run("xcopy epg/guides/hu/musor.tv.xml musor.tv.xml",shell=True)


def getEPG():
    channels = ['channel="DiscoveryChannelHungary.hu"',
            'channel="TLCHungary.hu"',
            'channel="M4sport.hu"',
            'channel="ComedyCentralHungary.hu"',
            'channel="ComedyCentralFamilyHungary.hu"',
            'channel="FilmPlusHungary.hu"',
            'channel="RTLKETTO.hu"',
            'channel="TV4.hu"',
            'channel="Viasat3.hu"',
            'channel="Viasat6.hu"',
            'channel="AXNHungary.hu"',
            'channel="TV2.hu"',
            'channel="CoolTV.hu"',]

    # Define the word you want to search for
    channel = open(f'epg.xml','w',encoding="utf-8")
    # Specify the file path you want to search in
    file_path = "musor.tv.xml"  # Replace with the path to your file

    channel.write(f'''<?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE tv SYSTEM "xmltv.dtd">
    <tv>
       <channel id="M4sport.hu">
    <display-name lang="en">M4 Sport</display-name>
    <icon src="logo/m4.png"/>
  </channel>

  <channel id="CoolTV.hu">
    <display-name lang="en">Cool Tv</display-name>
    <icon src="logo/cool.png"/>
  </channel>
  

  <channel id="ComedyCentralHungary.hu">
    <display-name lang="en">Comedy Central</display-name>
    <icon src="logo/comdeyC.png"/>
  </channel>
  
<channel id="ComedyCentralFamilyHungary.hu">
    <display-name lang="en">Comedy Central Family</display-name>
    <icon src='logo/comedyF.png'/>
  </channel>
  
<channel id="FilmPlusHungary.hu">
    <display-name lang="en">Film+</display-name>
    <icon src="logo/filmplus.png"/>
  </channel>
  
  <channel id="RTLKETTO.hu">
    <display-name lang="en">RTL 2</display-name>
    <icon src="logo/rtlketto.png"/>
  </channel>
  
  <channel id="TV4.hu">
    <display-name lang="en">TV4</display-name>
    <icon src="logo/tv4.png"/>
  </channel>
  
  <channel id="Viasat3.hu">
    <display-name lang="en">Viasat 3</display-name>
    <icon src="logo/viasat3.png"/>
  </channel>

    <channel id="Viasat6.hu">
    <display-name lang="en">Viasat 6</display-name>
    <icon src="logo/Viasat6.png"/>
  </channel>

    <channel id="AXNHungary.hu">
    <display-name lang="en">AXN</display-name>
    <icon src="logo/axn.png"/>
  </channel>

    <channel id="TV2.hu">
    <display-name lang="en">TV2</display-name>
    <icon src="logo/tv2.png"/>
  </channel>

    <channel id="DiscoveryChannelHungary.hu">
    <display-name lang="en">Discovery Channel</display-name>
    <icon src="logo/dc.png"/>
  </channel>

    <channel id="TLCHungary.hu">
    <display-name lang="en">TLC</display-name>
    <icon src="logo/tlc.png"/>
  </channel>\n

    ''')

    # Open the file for reading
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            # Iterate through each line in the file  
            
            for line in file:
                for chanel in channels:
                # Check if the target word is present in the line
                    if chanel in line:
                    # Print the line if the word is found
                        channel.writelines(f"{line}\n")    
          
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    channel.write("</tv>")
    print("Sekeres Programfutás")
getEPG()