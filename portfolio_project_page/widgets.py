from ckeditor.widgets import CKEditorWidget
from django.forms import widgets

class CustomCKEditorWidget(CKEditorWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config['height'] = 400
        self.config['width'] = '100%'
        self.config['toolbar'] = [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', 'Indent', 'Outdent'],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source']
        ]