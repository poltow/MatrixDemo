# original script by:
# http://remotescripts.blogspot.com
# Modified by grubtoe


###############################################
# Initialize Live API and Framework elements
from __future__ import with_statement
import Live 
from _Framework.ButtonElement import ButtonElement 
from _Framework.ButtonMatrixElement import ButtonMatrixElement
from _Framework.ControlSurface import ControlSurface
from _Framework.InputControlElement import MIDI_CC_TYPE, MIDI_NOTE_TYPE
from CustomSessionComponent import CustomSessionComponent
from consts import *

###############################################
# Main Script to Configure Red Box and Buttons
# (Not Necessary to edit below here)

class AAAMatrix(ControlSurface):
    __module__ = __name__
    __doc__ = " AAAMatrix controller script "
    
    def __init__(self, c_instance):
        ControlSurface.__init__(self, c_instance)
        self.log_message("LOG: AAAMatrix __init__")
        self._session = None
        with self.component_guard():
            self._set_suppress_features(True) 
            self._session = None
            self._session_A = None
            self._session_B = None
            self._highlight_counter = 0
            self._link_button = None
            
            Live.Base.log("LOG: AAAMatrix _session" + str(self._session ))
            Live.Base.log("LOG: AAAMatrix _session_A" + str(self._session_A ))
            Live.Base.log("LOG: AAAMatrix _session_B" + str(self._session_B ))
            self._setup_session_control(clip_A_notes,control_A,0,0, 'A')    
            self._session_A = self._session
            
            Live.Base.log("LOG: AAAMatrix _session" + str(self._session ))
            Live.Base.log("LOG: AAAMatrix _session_A" + str(self._session_A ))
            Live.Base.log("LOG: AAAMatrix _session_B" + str(self._session_B )) 
            self._setup_session_control(clip_B_notes, control_B,0,2,'B')
                    
            self._session_B = self._session                    
            Live.Base.log("LOG: AAAMatrix _session" + str(self._session ))
            Live.Base.log("LOG: AAAMatrix _session_A" + str(self._session_A ))
            Live.Base.log("LOG: AAAMatrix _session_B" + str(self._session_B ))
            self.set_link_button(ButtonElement(False, MIDI_CC_TYPE, CHANNEL, 93))
            self._set_suppress_features(False) 
            
        
    def _set_suppress_features(self, state):
        self.log_message("LOG: AAAMatrix _set_suppress_features - state="+str(state))
        self._suppress_session_highlight = state
        self._suppress_send_midi = state
        self._set_suppress_rebuild_requests(state)
        
    def _setup_session_control(self, clip_notes, control_notes, offset_tracks, offset_scenes, name):
        Live.Base.log("LOG: AAAMatrix _setup_session_control")
        is_momentary = True

        # Set Highlight Grid Size
        self._session = CustomSessionComponent(num_tracks, num_scenes, auto_name = True)

        # Set Session Name
        self._session.name = 'AAAMatrix_Session_' + str(name)

        # Set Highlight Grid Size
        self._session.set_offsets(offset_tracks, offset_scenes) 

        # Configure navigation buttons
        right_button = ButtonElement(is_momentary, MIDI_CC_TYPE, CHANNEL, control_notes[2])
        right_button.name = 'Bank_Select_Right_Button'
        left_button = ButtonElement(is_momentary, MIDI_CC_TYPE, CHANNEL, control_notes[3])
        left_button.name = 'Bank_Select_Left_Button'
        self._session.set_track_bank_buttons(right_button, left_button)

        up_button = ButtonElement(is_momentary, MIDI_CC_TYPE, CHANNEL, control_notes[0])
        up_button.name = 'Bank_Select_Up_Button'
        down_button = ButtonElement(is_momentary, MIDI_CC_TYPE, CHANNEL, control_notes[1])
        down_button.name = 'Bank_Select_Down_Button'
        self._session.set_scene_bank_buttons(down_button, up_button)

        # Configure clip launch buttons
        matrix = ButtonMatrixElement()
        matrix.name = 'Button_Matrix_' + str(name)
        
        for scene_index in range(num_scenes):
            scene = self._session.scene(scene_index)
            scene.name = 'Scene_' + str(scene_index)
            button_row = []
            for track_index in range(num_tracks):
                button = ButtonElement(is_momentary, MIDI_CC_TYPE, CHANNEL, clip_notes[scene_index][track_index])
                button.name = str(track_index) + '_Clip_' + str(scene_index) + '_Button'
                button_row.append(button)
                clip_slot = scene.clip_slot(track_index)
                clip_slot.name = str(track_index) + '_Clip_Slot_' + str(scene_index)
                clip_slot.set_launch_button(button)
            matrix.add_row(tuple(button_row))
        self.set_highlighting_session_component(self._session)

    def update_display(self):
        self._highlight_counter += 1
        if(self._session_A != None and self._session_B != None):
            if(self._highlight_counter ==2):
                self.set_highlighting_session_component(self._session_A)
            elif(self._highlight_counter ==4):
                self._highlight_counter = 0 
                self.set_highlighting_session_component(self._session_B)
           
    def set_link_button(self, link_button):
        assert (isinstance(link_button, (ButtonElement, type(None))))
        if link_button != self._link_button:
            if self._link_button != None:
                self._link_button.remove_value_listener(self._link_value)
            self._link_button = link_button
            if self._link_button != None: 
                self._link_button.add_value_listener(self._link_value)
        self.update()

    def _link_value(self, value):
        assert (self._link_button != None)
        assert (value in range(128))
        if(self._session_A != None and self._session_B != None):
            if (value >0):
                self._session_A._link()
                self._session_B._link()
            else:
                self._session_A._unlink()
                self._session_B._unlink()
                   
    # Close script
    def disconnect(self):
        Live.Base.log("LOG: AAAMatrix disconnect")
        """clean things up on disconnect"""
        if self._link_button != None:
            self._link_button.remove_value_listener(self._link_value)
            self._link_button = None
        ControlSurface.disconnect(self)
        return None
    
    
    

