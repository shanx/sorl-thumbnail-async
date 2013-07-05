
# Default sorl-thumbnail backend is overridden. We need to tell which backend to use.
THUMBNAIL_BACKEND = 'sorl-thumbnail-async.thumbnail.backend.AsyncThumbnailBackend'

# Instead of original sorl-thumbnail design, we predefine the thumbnail options
# here and reuse same everywhere. 
THUMBNAIL_OPTIONS_DICT = {
        'small': {
                'geometry': '140x140',
                'crop': 'center'
        }
    }