###############################################
# Initialize Live API and Framework elements
from __future__ import with_statement
import Live 
from _Framework.ButtonElement import ButtonElement 
from _Framework.ButtonMatrixElement import ButtonMatrixElement
from _Framework.ControlSurface import ControlSurface
from _Framework.InputControlElement import MIDI_CC_TYPE, MIDI_NOTE_TYPE
from consts import *
from _Framework.SessionComponent import SessionComponent 


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
        session = SessionComponent(num_tracks, num_scenes)

        # Set Session Name
        session.name = 'AAAMatrix Session'

        # Set Highlight Grid Size
        session.set_offsets(offset_tracks, offset_scenes) 

        # Configure navigation buttons
        right_button = ButtonElement(is_momentary, MIDI_NOTE_TYPE, CHANNEL, right_button_NOTE)
        left_button = ButtonElement(is_momentary, MIDI_NOTE_TYPE, CHANNEL, left_button_NOTE)
        up_button = ButtonElement(is_momentary, MIDI_NOTE_TYPE, CHANNEL, up_button_NOTE)
        down_button = ButtonElement(is_momentary, MIDI_NOTE_TYPE, CHANNEL, down_button_NOTE)
        right_button.name = 'Bank_Select_Right_Button'
        left_button.name = 'Bank_Select_Left_Button'
        up_button.name = 'Bank_Select_Up_Button'
        down_button.name = 'Bank_Select_Down_Button'
        session.set_track_bank_buttons(right_button, left_button)
        session.set_scene_bank_buttons(down_button, up_button)

        # Configure clip launch buttons
        matrix = ButtonMatrixElement()
        matrix.name = 'Button_Matrix'
        
        for scene_index in range(num_scenes):
            scene = session.scene(scene_index)
            scene.name = 'Scene_' + str(scene_index)
            button_row = []
            for track_index in range(num_tracks):
                button = ButtonElement(is_momentary, MIDI_CC_TYPE, CHANNEL, clip_CCs[scene_index][track_index])
                button.name = str(track_index) + '_Clip_' + str(scene_index) + '_Button'
                button_row.append(button)
                clip_slot = scene.clip_slot(track_index)
                clip_slot.name = str(track_index) + '_Clip_Slot_' + str(scene_index)
                clip_slot.set_launch_button(button)
            matrix.add_row(tuple(button_row))
        self.set_highlighting_session_component(session)

            
    # Close script
    def disconnect(self):
        Live.Base.log("LOG: AAAMatrix disconnect")
        """clean things up on disconnect"""
        ControlSurface.disconnect(self)
        return None
