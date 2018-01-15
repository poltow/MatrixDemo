###############################################
# Variables

#####
# Set Midi Channel that you will use to move red box and launch clips.
# Midi channels 1-16 are numbered 0 through 15

CHANNEL = 0 

#####
# Set Midi Notes that you will use for left,right,up,down navigation buttons 
  
left_button_CC = 86 
right_button_CC = 88 
up_button_CC = 77 
down_button_CC = 87 

left_select_CC = 75 
right_select_CC = 85 

#####
# Set size of red box.  Box will be X Tracks wide by X Scenes tall.  
# If you change the box size, you will need to change the clip launch 
# note assignments below.  

num_tracks = 4 # columns
num_scenes = 4 # rows

#####
# Set Offset of red box position to start off on a specific track or scene.  
   
offset_tracks = 0 # use 0 for first track / column
offset_scenes = 0 # use 0 for first scene / row

#####
# Clip launch note assignments.  If you change the size of the red box, 
# you will need to change these lines.  Remove or add values in the [] 
# brackets for different numbers of tracks / columns.  Remove or add 
# new lines for different numbers of scenes / rows (And you must remove 
# or add them in the next section too!).  

clip_launch_row_1_CCs = [69,70,71,72] #row 1 note assignments
clip_launch_row_2_CCs = [79,80,81,82] #row 2 note assignments       
clip_launch_row_3_CCs = [89,90,91,92]#row 3 note assignments       
clip_launch_row_4_CCs = [99,100,101,102] #row 4 note assignments       


clip_stop_row_CCs = [109,110,111,112] #row 3 note assignments     
stop_all_clips_CC = 113

scene_launch_column_CCs = [73,83,93,103] #row 3 note assignments   

#####
# Combine the clip launch note rows into one variable.  You will need 
# to modify this line if you want to change the number of scenes / rows 
# in the red box. Make sure that this matches the number of lines that 
# you have in the section above). 

clip_CCs = [clip_launch_row_1_CCs, 
              clip_launch_row_2_CCs, 
              clip_launch_row_3_CCs,
              clip_launch_row_4_CCs]
