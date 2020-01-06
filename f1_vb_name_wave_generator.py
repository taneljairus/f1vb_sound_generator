###Usable on F1 Challenge VB - http://valpaso75.altervista.org/
###runs on Python 2.7.15, maybe others
###requires ffmpeg - https://www.ffmpeg.org/download.html
###requires voice - https://www.elifulkerson.com/projects/commandline-text-to-speech.php
###requires Windows text-to-speech packages - https://support.office.com/en-us/article/how-to-download-text-to-speech-languages-for-windows-10-d5a6b612-b3ae-423f-afa5-4f6caf1ec5d3
###if you want to have better pronunciations, install suitable package and add it to voices_nationalities dictionary

import os
voices_nationalities = {"-": "Zira"," Argentinean": "Helena","Americain": "Zira","American": "Zira","Argentina": "Helena","Argentinean": "Helena","Argentinian": "Helena","Austia": "Hedda","Australia": "Zira","Australian": "Zira","Austria": "Hedda","Austrian": "Hedda","Autrian": "Hedda","Autrichien": "Hedda","Belge": "Hortense","Belgian": "Hortense","Brazil": "Helena","Brazilian": "Helena","Bresilien": "Helena","Britannique": "Zira","British": "Zira","Canadian": "Zira","Chilean": "Helena","Colombian": "Helena","Czech": "Hedda","Danemark": "Hedda","Danish": "Hedda","Dutch": "Hedda","English": "Zira","Espagnol": "Zira","Finland": "Hedda","Finnish": "Hedda","Francais": "Hortense","France": "Hortense","Français": "Hortense","French": "Hortense","German": "Hedda","Germany": "Hedda","Great Britain": "Zira","Holland": "Hedda","Hungarian": "Hedda","Indian": "Zira","Indonesian": "Zira","Irish": "Zira","Italia": "Elsa","Italian": "Elsa","Italien": "Elsa","Italy": "Elsa","Japan": "Zira","Japanese": "Zira","Japonais": "Zira","Japonese": "Zira","Liechtenstein": "Hedda","Malaysian": "Zira","Mexican": "Helena","Monacon": "Hortense","Netherlands": "Hedda","New Zealand": "Zira","New Zealander": "Zira","New Zelander": "Zira","Northern Ireland": "Zira","Polish": "Hedda","Portuguese": "Helena","Rhodesian": "Zira","Russian": "Zira","Scottish": "Zira","South Africa": "Hedda","South African": "Hedda","South-Africa": "Hedda","Spain": "Helena","Spanish": "Helena","Suedois": "Hedda","Sweden": "Hedda","Swedish": "Hedda","Swiss": "Hedda","Switzerland": "Hedda","Thai": "Zira","Ukrainian": "Zira","United Kingdom": "Zira","United States": "Zira","United-Kingdom": "Zira","Unites States": "Zira","unknown": "Zira","Uruguayan": "Helena","USA": "Zira","Welsh": "Zira","Venezuela": "Helena","Venezuelan": "Helena"}
cdir = "\\Formula1\\SeasonData\\Vehicles"
f = open("generate_name_sounds.bat",'w')
f.write("mkdir temporary_sound_files")
for root, dirs, files in os.walk(cdir):
    [dirs.remove(d) for d in list(dirs) if d == "output" or d == "resource"]
    for file in files:
        if file.endswith(".veh") or file.endswith(".VEH")  or file.endswith(".TXT") or file.endswith(".txt"):
            with open(os.path.join(root, file),'r') as fx:
                filecontents = fx.readlines()
                for fileline in filecontents:
                    if fileline.startswith("Team="):
                        teamname = fileline.replace("Team=","").replace('"','').strip()
                        f.write("\nvoice --mono --8bit -v 100  -o \"temporary_sound_files\\pws"+teamname+"_TBx.wav\" " + teamname)
                        f.write("\nvoice --mono --8bit -v 100  -o \"temporary_sound_files\\pws"+teamname+"_TDBx.wav\" " + teamname + " driver")
                        f.write("\nvoice --mono --8bit -v 100  -o \"temporary_sound_files\\pws"+teamname+"_TDEx.wav\" " + teamname + " driver")
                        f.write("\nvoice --mono --8bit -v 100  -o \"temporary_sound_files\\pws"+teamname+"_TEx.wav\" " + teamname)
                        f.write("\nvoice --mono --8bit -v 100  -o \"temporary_sound_files\\tv"+teamname+"_TBx.wav\" " + teamname)
                        f.write("\nvoice --mono --8bit -v 100  -o \"temporary_sound_files\\tv"+teamname+"_TDBx.wav\" " + teamname + " driver")
                        f.write("\nvoice --mono --8bit -v 100  -o \"temporary_sound_files\\tv"+teamname+"_TDEx.wav\" " + teamname + " driver")
                        f.write("\nvoice --mono --8bit -v 100  -o \"temporary_sound_files\\tv"+teamname+"_TEx.wav\" " + teamname)
                        f.write("\nmkdir \""+root[0:34]+"\\" + teamname+"\"")
                        f.write("\nffmpeg -y -i \"temporary_sound_files\\pws"+teamname+"_TBx.wav\" -filter:a \"volume=12\" \""+root[0:34]+"\\" + teamname+"\\" + "pws"+teamname.replace(" ","-")+"_TB.wav\"")
                        f.write("\nffmpeg -y -i \"temporary_sound_files\\pws"+teamname+"_TDBx.wav\" -filter:a \"volume=12\" \""+root[0:34]+"\\" + teamname+"\\" + "pws"+teamname.replace(" ","-")+"_TDB.wav\"")
                        f.write("\nffmpeg -y -i \"temporary_sound_files\\pws"+teamname+"_TDEx.wav\" -filter:a \"volume=12\" \""+root[0:34]+"\\" + teamname+"\\" + "pws"+teamname.replace(" ","-")+"_TDE.wav\"")
                        f.write("\nffmpeg -y -i \"temporary_sound_files\\pws"+teamname+"_TEx.wav\" -filter:a \"volume=12\" \""+root[0:34]+"\\" + teamname+"\\" + "pws"+teamname.replace(" ","-")+"_TE.wav\"")
                        f.write("\nffmpeg -y -i \"temporary_sound_files\\tv"+teamname+"_TBx.wav\" -filter:a \"volume=12\" \""+root[0:34]+"\\" + teamname+"\\" + "tv"+teamname.replace(" ","-")+"_TB.wav\"")
                        f.write("\nffmpeg -y -i \"temporary_sound_files\\tv"+teamname+"_TDBx.wav\" -filter:a \"volume=12\" \""+root[0:34]+"\\" + teamname+"\\" + "tv"+teamname.replace(" ","-")+"_TDB.wav\"")
                        f.write("\nffmpeg -y -i \"temporary_sound_files\\tv"+teamname+"_TDEx.wav\" -filter:a \"volume=12\" \""+root[0:34]+"\\" + teamname+"\\" + "tv"+teamname.replace(" ","-")+"_TDE.wav\"")
                        f.write("\nffmpeg -y -i \"temporary_sound_files\\tv"+teamname+"_TEx.wav\" -filter:a \"volume=12\" \""+root[0:34]+"\\" + teamname+"\\" + "tv"+teamname.replace(" ","-")+"_TE.wav\"")

cdir = "\\Formula1\\Drivers Ability"

for root, dirs, files in os.walk(cdir):
    [dirs.remove(d) for d in list(dirs) if d == "output" or d == "resource"]
    for file in files:

        if file.endswith(".rcd") or file.endswith(".RCD"):

            with open(os.path.join(root, file),'r') as fx:
                filecontents = fx.readlines()
                for fileline in filecontents:
                    if fileline.strip().startswith("Natio") or fileline.strip().startswith("nat"):
                        try:
                            voice = voices_nationalities [fileline.strip().split("=")[1]]
                        except:
                            voice = "Zira"
                        f.write ("\nvoice -n \"Microsoft " + voice + " Desktop\"  --mono --8bit -v 100  -o \"temporary_sound_files\\tv"+filecontents[0].strip()+"_FB.wav\" " + filecontents[0].strip().replace("-"," "))
                        f.write ("\nvoice -n \"Microsoft " + voice + " Desktop\"  --mono --8bit -v 100  -o \"temporary_sound_files\\tv"+filecontents[0].strip()+"_FE.wav\" " + filecontents[0].strip().replace("-"," "))
                        f.write ("\nvoice -n \"Microsoft " + voice + " Desktop\"  --mono --8bit -v 100  -o \"temporary_sound_files\\pws"+filecontents[0].strip()+"_FB.wav\" " + filecontents[0].strip().replace("-"," "))
                        f.write ("\nvoice -n \"Microsoft " + voice + " Desktop\"  --mono --8bit -v 100  -o \"temporary_sound_files\\pws"+filecontents[0].strip()+"_FE.wav\" " + filecontents[0].strip().replace("-"," "))
                        f.write ("\nvoice -n \"Microsoft " + voice + " Desktop\"  --mono --8bit -v 100  -o \"temporary_sound_files\\tv"+filecontents[0].strip().replace(" ","-")+"_SB.wav\" " + filecontents[0].strip().replace("-"," ").split(" ")[-1]) 
                        f.write ("\nvoice -n \"Microsoft " + voice + " Desktop\"  --mono --8bit -v 100  -o \"temporary_sound_files\\tv"+filecontents[0].strip().replace(" ","-")+"_SE.wav\" " + filecontents[0].strip().replace("-"," ").split(" ")[-1])
                        f.write ("\nvoice -n \"Microsoft " + voice + " Desktop\"  --mono --8bit -v 100  -o \"temporary_sound_files\\pws"+filecontents[0].strip().replace(" ","-")+"_SB.wav\" " + filecontents[0].strip().replace("-"," ").split(" ")[-1])
                        f.write ("\nvoice -n \"Microsoft " + voice + " Desktop\"  --mono --8bit -v 100  -o \"temporary_sound_files\\pws"+filecontents[0].strip().replace(" ","-")+"_SE.wav\" " + filecontents[0].strip().replace("-"," ").split(" ")[-1])
                        f.write("\nffmpeg -y -i \"temporary_sound_files\\tv"+filecontents[0].strip().replace(" ","-")+"_FB.wav\" -filter:a \"volume=12\" \"\Formula1\Audio\Commentary\\" + "tv"+filecontents[0].strip().replace(" ","-")+"_FB.wav\"")
                        f.write("\nffmpeg -y -i \"temporary_sound_files\\tv"+filecontents[0].strip().replace(" ","-")+"_FE.wav\" -filter:a \"volume=12\" \"\Formula1\Audio\Commentary\\" + "tv"+filecontents[0].strip().replace(" ","-")+"_FE.wav\"")
                        f.write("\nffmpeg -y -i \"temporary_sound_files\\pws"+filecontents[0].strip().replace(" ","-")+"_FB.wav\" -filter:a \"volume=12\" \"\Formula1\Audio\Commentary\\" + "pws"+filecontents[0].strip().replace(" ","-")+"_FB.wav\"")
                        f.write("\nffmpeg -y -i \"temporary_sound_files\\pws"+filecontents[0].strip().replace(" ","-")+"_FE.wav\" -filter:a \"volume=12\" \"\Formula1\Audio\Commentary\\" + "pws"+filecontents[0].strip().replace(" ","-")+"_FE.wav\"")
                        f.write("\nffmpeg -y -i \"temporary_sound_files\\tv"+filecontents[0].strip().replace(" ","-")+"_SB.wav\" -filter:a \"volume=12\" \"\Formula1\Audio\Commentary\\" + "tv"+filecontents[0].strip().replace(" ","-")+"_SB.wav\"")
                        f.write("\nffmpeg -y -i \"temporary_sound_files\\tv"+filecontents[0].strip().replace(" ","-")+"_SE.wav\" -filter:a \"volume=12\" \"\Formula1\Audio\Commentary\\" + "tv"+filecontents[0].strip().replace(" ","-")+"_SE.wav\"")
                        f.write("\nffmpeg -y -i \"temporary_sound_files\\pws"+filecontents[0].strip().replace(" ","-")+"_SB.wav\" -filter:a \"volume=12\" \"\Formula1\Audio\Commentary\\" + "pws"+filecontents[0].strip().replace(" ","-")+"_SB.wav\"")
                        f.write("\nffmpeg -y -i \"temporary_sound_files\\pws"+filecontents[0].strip().replace(" ","-")+"_SE.wav\" -filter:a \"volume=12\" \"\Formula1\Audio\Commentary\\" + "pws"+filecontents[0].strip().replace(" ","-")+"_SE.wav\"")
f.close()
