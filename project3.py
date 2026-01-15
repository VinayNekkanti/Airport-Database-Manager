class ExampleContextManager:
    def __init__(self, value):
        print('Initializing')
        self.value = value
    def __enter__(self):
        print('Entering')
        return self
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type is None:
            reason = 'Normally'
        else:
            return True
            #reason = f'because of an exception of type {exc_type.__name__}'
        print(f'Exiting {reason}')

with ExampleContextManager('Boo') as context:
    print(context.value)
    print('Still in with statement')
    raise ValueError('error raised')
    
    
    
   