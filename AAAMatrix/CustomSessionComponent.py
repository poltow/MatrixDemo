from _Framework.SessionComponent import SessionComponent
from _Framework.SceneComponent import SceneComponent
import Live 
class CustomSessionComponent(SessionComponent):  
    _session_component_ends_initialisation = False
    #Avoid running 2 last lines of __init__
    

    
    scene_component_type = SceneComponent

    def __init__(self, *a, **k):
        super(CustomSessionComponent, self).__init__(*a, **k)
       
        
        self.on_selected_scene_changed()
        self.set_offsets(0, 0)
        
    def disconnect(self):
        SessionComponent.disconnect(self)        
        



'''   
    def update(self):
        self._highlight_counter +=1
        if(self._highlight_counter ==5):
            Live.Base.log("LOG: CustomSessionComponent update")
            self._highlight_counter = 0 
            show_highlight = not self._show_highlight 
            Live.Base.log("LOG: AAAMatrix set_show_highlight: " + str(show_highlight))
            self.set_show_highlight(show_highlight)

        Linking sessions:
        _linked_session_instances = []      
        _minimal_track_offset = -1
        _minimal_scene_offset = -1
        _highlighting_callback = None

      

    auto_name = False

    
 def __init__(self, num_tracks = 0, num_scenes = 0, auto_name = False, enable_skinning = False, *a, **k):
disconnect(self)


_end_initialisation(self)

#set_highlighting_callback(self, callback)
# Setter for callback to be call in _do_show_highlight function,
# which ends calling the ControlSurface_set_session_highlight callback function, the _c_instance proxy

set_show_highlight(self, show_highlight)
#ON/OFF session box

_do_show_highlight(self)
#Refresh session box

on_enabled_changed(self)
#Update skin

update(self)


#NAVIGATION
#set_scene_bank_buttons(self, down_button, up_button)
#set_scene_bank_up_button(self, button)
#set_scene_bank_down_button(self, button)
#set_track_bank_buttons(self, right_button, left_button)
#set_track_bank_left_button(self, button)
#set_track_bank_right_button(self, button)
set_track_banking_increment(self, increment)
_can_bank_down(self)
_can_bank_up(self)
_can_bank_right(self)
_can_bank_left(self)
_bank_up(self)
_bank_down(self)
_bank_right(self)
_bank_left(self)


set_select_buttons(self, next_button, prev_button)
set_select_next_button(self, next_button)
set_select_prev_button(self, prev_button)

scene(self, index)
selected_scene(self)
_create_scene(self)
_on_next_scene_value(self, value)
_on_prev_scene_value(self, value)

set_stop_track_clip_buttons(self, buttons)
set_stop_track_clip_value(self, value)
_update_stop_track_clip_buttons(self)
_on_stop_track_value(self, value, sender)

set_stop_all_clips_button(self, button)
_update_stop_all_clips_button(self)

_on_stop_all_value(self, value)
_stop_all_value(self, value)


set_clip_launch_buttons(self, buttons)
set_scene_launch_buttons(self, buttons)

set_mixer(self, mixer)Sets the MixerComponent to be controlled by this session


on_scene_list_changed(self)Called by the control surface if scenes are added/removed, to be overridden
on_track_list_changed(self)Called by the control surface if tracks are added/removed, to be overridden
on_selected_scene_changed(self)Called by the control surface when a scene is selected, to be overridden

width(self)
height(self)
tracks_to_use(self)

set_offsets(self, track_offset, scene_offset)
track_offset(self)
scene_offset(self)
_get_minimal_track_offset(self)
_get_minimal_scene_offset(self)
_update_scene_offset(self)
_change_offsets(self, track_increment, scene_increment)


_update_select_buttons(self)
_reassign_scenes(self)
_reassign_tracks(self)
_on_fired_slot_index_changed(self, index)

_is_linked(self)
_link(self)
_unlink(self)
'''