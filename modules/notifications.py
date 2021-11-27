from plyer import notification as notification

def create_notification(Title, Message):
    notification.notify( 
	title = Title, 
	message= Message, 
    timeout=3000 
)