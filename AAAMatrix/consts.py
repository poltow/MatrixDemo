###############################################
# Variables

#####
# Set Midi Channel that you will use to move red box and launch clips.
# Midi channels 1-16 are numbered 0 through 15

CHANNEL = 0 

#####
# Set Midi Notes that you will use for left,right,up,down navigation buttons 
  
left_button_NOTE = 2 
right_button_NOTE = 3 
up_button_NOTE = 0 
down_button_NOTE = 1 

#####
# Set size of red box.  Box will be X Tracks wide by X Scenes tall.  
# If you change the box size, you will need to change the clip launch 
# note assignments below.  

num_tracks = 5 # columns
num_scenes = 5 # rows

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

clip_launch_row_1_CCs = [24,25,26,27,28] #row 1 note assignments
clip_launch_row_2_CCs = [29,30,31,32,33] #row 2 note assignments       
clip_launch_row_3_CCs = [34,35,36,37,38] #row 3 note assignments       
clip_launch_row_4_CCs = [39,40,41,42,43] #row 3 note assignments       
clip_launch_row_5_CCs = [44,45,46,47,48] #row 3 note assignments       

#####
# Combine the clip launch note rows into one variable.  You will need 
# to modify this line if you want to change the number of scenes / rows 
# in the red box. Make sure that this matches the number of lines that 
# you have in the section above). 

clip_CCs = [clip_launch_row_1_CCs, 
              clip_launch_row_2_CCs, 
              clip_launch_row_3_CCs,
              clip_launch_row_4_CCs,
              clip_launch_row_5_CCs]