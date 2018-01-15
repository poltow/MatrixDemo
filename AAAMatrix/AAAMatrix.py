###############################################
# Initialize Live API and Framework elements
from __future__ import with_statement
import Live 
from _Framework.ButtonElement import ButtonElement 
from _Framework.ButtonMatrixElement import ButtonMatrixElement
from _Framework.ControlSurface import ControlSurface
from _Framework.InputControlElement import MIDI_CC_TYPE
from consts import *
from CustomSessionComponent import CustomSessionComponent


###############################################
# Main Script to Configure Red Box and Buttons
# (Not Necessary to edit below here)


class AAAMatrix(ControlSurface):
    __module__ = __name__
    __doc__ = " AAAMatrix controller script "
    
    def __init__(self, c_instance):
        ControlSurface.__init__(self, c_instance)
        self.log_message("LOG: AAAMatrix __init__")
        with self.component_guard():
            self._set_suppress_features(True) 
            self._setup_session_control()        
            self._set_suppress_features(False) 
        
    def _set_suppress_features(self, state):
        self.log_message("LOG: AAAMatrix _set_suppress_features - state="+str(state))
        self._suppress_session_highlight = state
        self._suppress_send_midi = state
        self._set_suppress_rebuild_requests(state)
        
    def _setup_session_control(self):
        Live.Base.log("LOG: AAAMatrix _setup_session_control")
        is_momentary = True

        # Set Highlight Grid Size
        session = CustomSessionComponent(num_tracks, num_scenes)

        # Set Session Name
        session.name = 'AAAMatrix Session'

        # Set Highlight Grid Size
        session.set_offsets(offset_tracks, offset_scenes) 

        # SESSION NAVIGATION BUTTONS
        right_button = ButtonElement(is_momentary, MIDI_CC_TYPE, CHANNEL, right_button_CC)
        left_button = ButtonElement(is_momentary, MIDI_CC_TYPE, CHANNEL, left_button_CC)
        right_button.name = 'Bank_Select_Right_Button'
        left_button.name = 'Bank_Select_Left_Button'
        session.set_track_bank_buttons(right_button, left_button)
        up_button = ButtonElement(is_momentary, MIDI_CC_TYPE, CHANNEL, up_button_CC)
        down_button = ButtonElement(is_momentary, MIDI_CC_TYPE, CHANNEL, down_button_CC)
        up_button.name = 'Bank_Select_Up_Button'
        down_button.name = 'Bank_Select_Down_Button'
        session.set_scene_bank_buttons(down_button, up_button)

        #SCENE NAVIGATION BUTTONS
        prev_button = ButtonElement(is_momentary, MIDI_CC_TYPE, CHANNEL, left_select_CC)
        next_button = ButtonElement(is_momentary, MIDI_CC_TYPE, CHANNEL, right_select_CC)
        next_button.name = 'Next_Select_Button'
        prev_button.name = 'Prev_Select__Button'
        session.set_select_buttons(next_button, prev_button)
        
        #STOP ALL CLIP BUTTON
        stop_all_button = ButtonElement(is_momentary, MIDI_CC_TYPE, CHANNEL, stop_all_clips_CC)
        stop_all_button.name = 'Stop_All_Button'
        session.set_stop_all_clips_button(stop_all_button)

        #SCENE LAUCH BUTTONS
        scene_launch_buttons = [ ButtonElement(True, MIDI_CC_TYPE, CHANNEL, scene_launch_column_CCs[index]) for index in xrange(num_scenes) ]
        scene_launch_buttons = ButtonMatrixElement(name='Scene_Launch_Buttons', rows=[scene_launch_buttons])
        session.set_scene_launch_buttons(scene_launch_buttons)
        
        #CLIP STOP BUTTONS
        scene_stop_buttons = [ ButtonElement(True, MIDI_CC_TYPE, CHANNEL, clip_stop_row_CCs[index]) for index in xrange(num_tracks) ]
        scene_stop_buttons = ButtonMatrixElement(name='Scene_Stop_Buttons', rows=[scene_stop_buttons])          
        session.set_stop_track_clip_buttons(scene_stop_buttons)
                
        #CLIP LAUCH BUTTONS
        matrix = ButtonMatrixElement(name='Button_Matrix')
        for scene_index in xrange(num_scenes):
            row = [ ButtonElement(True, MIDI_CC_TYPE, CHANNEL, clip_CCs[scene_index][track_index]) for track_index in xrange(num_tracks) ] 
            matrix.add_row(row)
        session.set_clip_launch_buttons(matrix)
        
        
            
        self.set_highlighting_session_component(session)

            
    # Close script
    def disconnect(self):
        Live.Base.log("LOG: AAAMatrix disconnect")
        """clean things up on disconnect"""
        ControlSurface.disconnect(self)
