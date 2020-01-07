###Usable on F1 Challenge VB - http://valpaso75.altervista.org/
###runs on Python 2.7.15, maybe others
###requires ffmpeg - https://www.ffmpeg.org/download.html
###requires voice - https://www.elifulkerson.com/projects/commandline-text-to-speech.php
###requires Windows text-to-speech packages - https://support.office.com/en-us/article/how-to-download-text-to-speech-languages-for-windows-10-d5a6b612-b3ae-423f-afa5-4f6caf1ec5d3
###if you want to have better pronunciations, install suitable package and add it to voices_nationalities dictionary

import os
voices_nationalities = {"-": "Zira"," Argentinean": "Helena","Americain": "Zira","American": "Zira","Argentina": "Helena","Argentinean": "Helena","Argentinian": "Helena","Austia": "Hedda","Australia": "Zira","Australian": "Zira","Austria": "Hedda","Austrian": "Hedda","Autrian": "Hedda","Autrichien": "Hedda","Belge": "Hortense","Belgian": "Hortense","Brazil": "Helena","Brazilian": "Helena","Bresilien": "Helena","Britannique": "Zira","British": "Zira","Canadian": "Zira","Chilean": "Helena","Colombian": "Helena","Czech": "Hedda","Danemark": "Hedda","Danish": "Hedda","Dutch": "Hedda","English": "Zira","Espagnol": "Zira","Finland": "Hedda","Finnish": "Hedda","Francais": "Hortense","France": "Hortense","Français": "Hortense","French": "Hortense","German": "Hedda","Germany": "Hedda","Great Britain": "Zira","Holland": "Hedda","Hungarian": "Hedda","Indian": "Zira","Indonesian": "Zira","Irish": "Zira","Italia": "Elsa","Italian": "Elsa","Italien": "Elsa","Italy": "Elsa","Japan": "Zira","Japanese": "Zira","Japonais": "Zira","Japonese": "Zira","Liechtenstein": "Hedda","Malaysian": "Zira","Mexican": "Helena","Monacon": "Hortense","Netherlands": "Hedda","New Zealand": "Zira","New Zealander": "Zira","New Zelander": "Zira","Northern Ireland": "Zira","Polish": "Hedda","Portuguese": "Helena","Rhodesian": "Zira","Russian": "Zira","Scottish": "Zira","South Africa": "Hedda","South African": "Hedda","South-Africa": "Hedda","Spain": "Helena","Spanish": "Helena","Suedois": "Hedda","Sweden": "Hedda","Swedish": "Hedda","Swiss": "Hedda","Switzerland": "Hedda","Thai": "Zira","Ukrainian": "Zira","United Kingdom": "Zira","United States": "Zira","United-Kingdom": "Zira","Unites States": "Zira","unknown": "Zira","Uruguayan": "Helena","USA": "Zira","Welsh": "Zira","Venezuela": "Helena","Venezuelan": "Helena"}
drivers_voices = {}
prefix = "\\tmp\\soundpack" #use this if you don't want to overwrite stuff every time

f = open("temporary_file",'w')
f.write("mkdir temporary_sound_files")
f.write("\nmkdir \""+prefix+"\\Formula1\Audio\Commentary\"")

cdir = "\\Formula1\\Drivers Ability" #get driver nationalities to match voices
for root, dirs, files in os.walk(cdir):
    [dirs.remove(d) for d in list(dirs) if d == "ignore"]
    for file in files:

        if file.upper().endswith(".RCD"):

            with open(os.path.join(root, file),'r') as fx:
                filecontents = fx.readlines()
                for fileline in filecontents:
                    if fileline.upper().strip().startswith("NAT"):
                        try:
                            voice = voices_nationalities [fileline.strip().split("=")[1]]
                            drivers_voices[filecontents[0].strip()] = voice
                        except:
                            voice = "Zira"

                        
                        




cdir = "\\Formula1\\SeasonData\\Vehicles"
for root, dirs, files in os.walk(cdir):
    [dirs.remove(d) for d in list(dirs) if d == "ignore"]
    for file in files:
        if file.upper().endswith(".VEH") or file.upper().endswith(".TXT"):
            with open(os.path.join(root, file),'r') as fx:
                filecontents = fx.readlines()
                for fileline in filecontents:
                    if fileline.strip().upper().startswith("TEAM="):
                        try:
                            teamname = fileline.split("\"")[1]
                        except:
                            teamname = fileline.split("=")[1]
                    if fileline.strip().upper().startswith("MANUFACTURER"):
                        manufacturer = fileline.split("\"")[1]
                    if fileline.strip().upper().startswith("DRIVER"):
                        drivername = fileline.split("\"")[1]
                f.write("\nvoice --mono --8bit -v 100  -o \"temporary_sound_files\\pws"+manufacturer+"_TBx.wav\" " + teamname)
                f.write("\nvoice --mono --8bit -v 100  -o \"temporary_sound_files\\pws"+manufacturer+"_TDBx.wav\" " + teamname + " driver")
                f.write("\nvoice --mono --8bit -v 100  -o \"temporary_sound_files\\pws"+manufacturer+"_TDEx.wav\" " + teamname + " driver")
                f.write("\nvoice --mono --8bit -v 100  -o \"temporary_sound_files\\pws"+manufacturer+"_TEx.wav\" " + teamname)
                f.write("\nvoice --mono --8bit -v 100  -o \"temporary_sound_files\\tv"+manufacturer+"_TBx.wav\" " + teamname)
                f.write("\nvoice --mono --8bit -v 100  -o \"temporary_sound_files\\tv"+manufacturer+"_TDBx.wav\" " + teamname + " driver")
                f.write("\nvoice --mono --8bit -v 100  -o \"temporary_sound_files\\tv"+manufacturer+"_TDEx.wav\" " + teamname + " driver")
                f.write("\nvoice --mono --8bit -v 100  -o \"temporary_sound_files\\tv"+manufacturer+"_TEx.wav\" " + teamname)
                
                f.write("\nffmpeg -y -i \"temporary_sound_files\\pws"+manufacturer+"_TBx.wav\" -filter:a \"volume=12\" \"temporary_sound_files\\pws"+manufacturer+"_TB.wav\"")
                f.write("\nffmpeg -y -i \"temporary_sound_files\\pws"+manufacturer+"_TDBx.wav\" -filter:a \"volume=12\" \"temporary_sound_files\\pws"+manufacturer+"_TDB.wav\"")
                f.write("\nffmpeg -y -i \"temporary_sound_files\\pws"+manufacturer+"_TDEx.wav\" -filter:a \"volume=12\" \"temporary_sound_files\\pws"+manufacturer+"_TDE.wav\"")
                f.write("\nffmpeg -y -i \"temporary_sound_files\\pws"+manufacturer+"_TEx.wav\" -filter:a \"volume=12\" \"temporary_sound_files\\pws"+manufacturer+"_TE.wav\"")
                f.write("\nffmpeg -y -i \"temporary_sound_files\\tv"+manufacturer+"_TBx.wav\" -filter:a \"volume=12\" \"temporary_sound_files\\tv"+manufacturer+"_TB.wav\"")
                f.write("\nffmpeg -y -i \"temporary_sound_files\\tv"+manufacturer+"_TDBx.wav\" -filter:a \"volume=12\" \"temporary_sound_files\\tv"+manufacturer+"_TDB.wav\"")
                f.write("\nffmpeg -y -i \"temporary_sound_files\\tv"+manufacturer+"_TDEx.wav\" -filter:a \"volume=12\" \"temporary_sound_files\\tv"+manufacturer+"_TDE.wav\"")
                f.write("\nffmpeg -y -i \"temporary_sound_files\\tv"+manufacturer+"_TEx.wav\" -filter:a \"volume=12\" \"temporary_sound_files\\tv"+manufacturer+"_TE.wav\"")

                f.write("\nmkdir \""+prefix+root[0:34]+"\\" + manufacturer+"\"")

                f.write("\ncopy /y  \"temporary_sound_files\\pws"+manufacturer+"_TB.wav\" \""+prefix+root[0:34]+"\\" + manufacturer+"\\" + "pws"+manufacturer+"_TB.wav\"")
                f.write("\ncopy /y  \"temporary_sound_files\\pws"+manufacturer+"_TDB.wav\" \""+prefix+root[0:34]+"\\" + manufacturer+"\\" + "pws"+manufacturer+"_TDB.wav\"")
                f.write("\ncopy /y  \"temporary_sound_files\\pws"+manufacturer+"_TDE.wav\"  \""+prefix+root[0:34]+"\\" + manufacturer+"\\" + "pws"+manufacturer+"_TDE.wav\"")
                f.write("\ncopy /y  \"temporary_sound_files\\pws"+manufacturer+"_TE.wav\"  \""+prefix+root[0:34]+"\\" + manufacturer+"\\" + "pws"+manufacturer+"_TE.wav\"")
                f.write("\ncopy /y  \"temporary_sound_files\\tv"+manufacturer+"_TB.wav\"  \""+prefix+root[0:34]+"\\" + manufacturer+"\\" + "tv"+manufacturer+"_TB.wav\"")
                f.write("\ncopy /y  \"temporary_sound_files\\tv"+manufacturer+"_TDB.wav\"  \""+prefix+root[0:34]+"\\" + manufacturer+"\\" + "tv"+manufacturer+"_TDB.wav\"")
                f.write("\ncopy /y  \"temporary_sound_files\\tv"+manufacturer+"_TDE.wav\"  \""+prefix+root[0:34]+"\\" + manufacturer+"\\" + "tv"+manufacturer+"_TDE.wav\"")
                f.write("\ncopy /y  \"temporary_sound_files\\tv"+manufacturer+"_TE.wav\"  \""+prefix+root[0:34]+"\\" + manufacturer+"\\" + "tv"+manufacturer+"_TE.wav\"")

                try:
                    voice = drivers_voices[drivername]
                except:
                    voice = "Zira"
                soundname = ("".join([i for i in drivername if not i.isdigit()])).replace("-"," ")

                f.write ("\nvoice -n \"Microsoft " + voice + " Desktop\"  --mono --8bit -v 100  -o \"temporary_sound_files\\tv"+drivername+"_xFB.wav\" " + soundname)
                f.write ("\nvoice -n \"Microsoft " + voice + " Desktop\"  --mono --8bit -v 100  -o \"temporary_sound_files\\tv"+drivername+"_xFE.wav\" " + soundname)
                f.write ("\nvoice -n \"Microsoft " + voice + " Desktop\"  --mono --8bit -v 100  -o \"temporary_sound_files\\pws"+drivername+"_xFB.wav\" " + soundname)
                f.write ("\nvoice -n \"Microsoft " + voice + " Desktop\"  --mono --8bit -v 100  -o \"temporary_sound_files\\pws"+drivername+"_xFE.wav\" " + soundname)
                f.write ("\nvoice -n \"Microsoft " + voice + " Desktop\"  --mono --8bit -v 100  -o \"temporary_sound_files\\tv"+drivername+"_xSB.wav\" " + soundname.split(" ")[-1]) 
                f.write ("\nvoice -n \"Microsoft " + voice + " Desktop\"  --mono --8bit -v 100  -o \"temporary_sound_files\\tv"+drivername+"_xSE.wav\" " + soundname.split(" ")[-1])
                f.write ("\nvoice -n \"Microsoft " + voice + " Desktop\"  --mono --8bit -v 100  -o \"temporary_sound_files\\pws"+drivername+"_xSB.wav\" " + soundname.split(" ")[-1])
                f.write ("\nvoice -n \"Microsoft " + voice + " Desktop\"  --mono --8bit -v 100  -o \"temporary_sound_files\\pws"+drivername+"_xSE.wav\" " + soundname.split(" ")[-1])

                f.write("\nffmpeg -y -i \"temporary_sound_files\\tv"+drivername+"_xFB.wav\" -filter:a \"volume=12\" \"temporary_sound_files\\tv"+drivername+"_FB.wav\"")
                f.write("\nffmpeg -y -i \"temporary_sound_files\\tv"+drivername+"_xFE.wav\" -filter:a \"volume=12\" \"temporary_sound_files\\tv"+drivername+"_FE.wav\"")
                f.write("\nffmpeg -y -i \"temporary_sound_files\\pws"+drivername+"_xFB.wav\" -filter:a \"volume=12\" \"temporary_sound_files\\pws"+drivername+"_FB.wav\"")
                f.write("\nffmpeg -y -i \"temporary_sound_files\\pws"+drivername+"_xFE.wav\" -filter:a \"volume=12\" \"temporary_sound_files\\pws"+drivername+"_FE.wav\"")
                f.write("\nffmpeg -y -i \"temporary_sound_files\\tv"+drivername+"_xSB.wav\" -filter:a \"volume=12\" \"temporary_sound_files\\tv"+drivername+"_SB.wav\"")
                f.write("\nffmpeg -y -i \"temporary_sound_files\\tv"+drivername+"_xSE.wav\" -filter:a \"volume=12\" \"temporary_sound_files\\tv"+drivername+"_SE.wav\"")
                f.write("\nffmpeg -y -i \"temporary_sound_files\\pws"+drivername+"_xSB.wav\" -filter:a \"volume=12\" \"temporary_sound_files\\pws"+drivername+"_SB.wav\"")
                f.write("\nffmpeg -y -i \"temporary_sound_files\\pws"+drivername+"_xSE.wav\" -filter:a \"volume=12\" \"temporary_sound_files\\pws"+drivername+"_SE.wav\"")

                f.write("\ncopy /y  \"temporary_sound_files\\tv"+drivername+"_FB.wav\" \""+prefix+"\\Formula1\Audio\Commentary\\tv"+drivername+"_FB.wav\"")
                f.write("\ncopy /y  \"temporary_sound_files\\tv"+drivername+"_FE.wav\" \""+prefix+"\\Formula1\Audio\Commentary\\tv"+drivername+"_FE.wav\"")
                f.write("\ncopy /y  \"temporary_sound_files\\pws"+drivername+"_FB.wav\" \""+prefix+"\\Formula1\Audio\Commentary\\pws"+drivername+"_FB.wav\"")
                f.write("\ncopy /y  \"temporary_sound_files\\pws"+drivername+"_FE.wav\" \""+prefix+"\\Formula1\Audio\Commentary\\pws"+drivername+"_FE.wav\"")
                f.write("\ncopy /y  \"temporary_sound_files\\tv"+drivername+"_SB.wav\" \""+prefix+"\\Formula1\Audio\Commentary\\tv"+drivername+"_SB.wav\"")
                f.write("\ncopy /y  \"temporary_sound_files\\tv"+drivername+"_SE.wav\" \""+prefix+"\\Formula1\Audio\Commentary\\tv"+drivername+"_SE.wav\"")
                f.write("\ncopy /y  \"temporary_sound_files\\pws"+drivername+"_SB.wav\" \""+prefix+"\\Formula1\Audio\Commentary\\pws"+drivername+"_SB.wav\"")
                f.write("\ncopy /y  \"temporary_sound_files\\pws"+drivername+"_SE.wav\" \""+prefix+"\\Formula1\Audio\Commentary\\pws"+drivername+"_SE.wav\"")

f.close()
w = open("generate_name_sounds.bat",'w')
duplicatefinder = set()
for line in open("temporary_file", "r"):
    if line not in duplicatefinder:
        w.write(line)
        duplicatefinder.add(line)
f.close()
os.unlink("temporary_file")
w.close()
