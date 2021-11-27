from time import  sleep as sleep 
from notifications import create_notification as create_notification
from global_variables import session_title as session_title
from global_variables import session_message as session_message
from winrt.windows.media.control import \
    GlobalSystemMediaTransportControlsSessionManager as MediaManager

async def pause_current_session_240_seconds():
    session = await MediaManager.request_async()
    current_session = session.get_current_session()
    info = current_session.get_playback_info()
    info_dict = {song_attr: info.__getattribute__(song_attr) for song_attr in dir(info) if song_attr[0] != '_'}
    if info_dict["playback_status"] == 4:
        create_notification(session_title,session_message)
        current_session.try_pause_async()
        sleep(240)
        create_notification("Azan Finished","You can enjoy your audio now!")
        current_session.try_play_async()