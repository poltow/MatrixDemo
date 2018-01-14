###############################################
# Variables

#####
# Set Midi Channel that you will use to move red box and launch clips.
# Midi channels 1-16 are numbered 0 through 15

CHANNEL = 0 

#####
# Set Midi Notes that you will use for left,right,up,down navigation buttons 
  
control_A = [77,87,88,86] 
control_B = [107,117,118,116] 
  
left_button_note = 2 
right_button_note = 3 
up_button_note = 0 
down_button_note = 1 

#####
# Set size of red box.  Box will be X Tracks wide by X Scenes tall.  
# If you change the box size, you will need to change the clip launch 
# note assignments below.  

num_tracks = 2 # columns
num_scenes = 2 # rows

#####
# Set Offset of red box position to start off on a specific track or scene.  
   
old_offset_tracks = 0 # use 0 for first track / column
old_offset_scenes = 0 # use 0 for first scene / row

#####
# Clip launch note assignments.  If you change the size of the red box, 
# you will need to change these lines.  Remove or add values in the [] 
# brackets for different numbers of tracks / columns.  Remove or add 
# new lines for different numbers of scenes / rows (And you must remove 
# or add them in the next section too!).  

clip_A_launch_row_1_notes = [69,70]
clip_A_launch_row_2_notes = [79,80]

clip_B_launch_row_1_notes = [99,100]
clip_B_launch_row_2_notes = [109,110]

clip_A_notes = [clip_A_launch_row_1_notes, clip_A_launch_row_2_notes]
clip_B_notes = [clip_B_launch_row_1_notes, clip_B_launch_row_2_notes]

clip_launch_row_1_notes = [24,25,26,27,28] #row 1 note assignments
clip_launch_row_2_notes = [29,30,31,32,33] #row 2 note assignments       
clip_launch_row_3_notes = [34,35,36,37,38] #row 3 note assignments       
clip_launch_row_4_notes = [39,40,41,42,43] #row 3 note assignments       
clip_launch_row_5_notes = [44,45,46,47,48] #row 3 note assignments       

#####
# Combine the clip launch note rows into one variable.  You will need 
# to modify this line if you want to change the number of scenes / rows 
# in the red box. Make sure that this matches the number of lines that 
# you have in the section above). 

old_clip_notes = [clip_launch_row_1_notes, 
              clip_launch_row_2_notes, 
              clip_launch_row_3_notes,
              clip_launch_row_4_notes,
              clip_launch_row_5_notes]