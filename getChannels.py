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
channel = open(f'screpped/epg.xml','w',encoding="utf-8")
# Specify the file path you want to search in
file_path = "musor.tv.xml"  # Replace with the path to your file

channel.write(f'''
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE tv SYSTEM "xmltv.dtd">
<tv>
  <!-- Channel Information -->
  <channel id="M4sport.hu">
    <display-name lang="en">M4 Sport</display-name>
    <icon src="https://upload.wikimedia.org/wikipedia/hu/thumb/f/fd/M4_logo.png/1200px-M4_logo.png"/>
  </channel>

  <channel id="CoolTV.hu">
    <display-name lang="en">Cool Tv</display-name>
    <icon src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Cool_TV_logo_2004.svg/1024px-Cool_TV_logo_2004.svg.png"/>
  </channel>
  

  <channel id="ComedyCentralHungary.hu">
    <display-name lang="en">Comedy Central</display-name>
    <icon src="https://logodownload.org/wp-content/uploads/2021/05/comedy-central-logo-1.png"/>
  </channel>
  
<channel id="ComedyCentralFamilyHungary.hu">
    <display-name lang="en">Comedy Central Family</display-name>
    <icon src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTXsk2MsVFr5GQ470UmgydRWHZLd_w18Sr-v2vJPDfcm3uQbJ0L7fFcWWJSs2NccjBG0Bo&usqp=CAU"/>
  </channel>
  
<channel id="FilmPlusHungary.hu">
    <display-name lang="en">Film+</display-name>
    <icon src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/FILM%2B_logo_2014_Hungary.png/800px-FILM%2B_logo_2014_Hungary.png"/>
  </channel>
  
  <channel id="RTLKETTO.hu">
    <display-name lang="en">RTL 2</display-name>
    <icon src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/RTL_II_Hungary_logo.svg/1280px-RTL_II_Hungary_logo.svg.png"/>
  </channel>
  
  <channel id="TV4.hu">
    <display-name lang="en">TV4</display-name>
    <icon src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRug9sSn-sRBq1oveTLdNz15DjWVs5Z_InqKN2h8gc&s"/>
  </channel>
  
  <channel id="Viasat3.hu">
    <display-name lang="en">Viasat 3</display-name>
    <icon src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Viasat3_%281%29.png/600px-Viasat3_%281%29.png"/>
  </channel>

    <channel id="Viasat6.hu">
    <display-name lang="en">Viasat 6</display-name>
    <icon src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/TV6_Viasat.svg/250px-TV6_Viasat.svg.png"/>
  </channel>

    <channel id="AXNHungary.hu">
    <display-name lang="en">AXN</display-name>
    <icon src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/AXN_logo.svg/263px-AXN_logo.svg.png"/>
  </channel>

    <channel id="TV2.hu">
    <display-name lang="en">TV2</display-name>
    <icon src="https://upload.wikimedia.org/wikipedia/commons/9/9e/TV2_logo.png"/>
  </channel>

    <channel id="DiscoveryChannelHungary.hu">
    <display-name lang="en">Discovery Channel</display-name>
    <icon src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/2019_Discovery_logo.svg/800px-2019_Discovery_logo.svg.png"/>
  </channel>

    <channel id="TLCHungary.hu">
    <display-name lang="en">TLC</display-name>
    <icon src="https://onlinestream.live/logos/6751.png"/>
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
            print(chanel)       
       
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")

channel.write("</tv>")