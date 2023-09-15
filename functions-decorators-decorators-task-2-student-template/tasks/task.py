def log(fn):
    """
    Add your code here or call it from here   
    """
    from time import time
    import inspect

    def wrapper(*args, **kwargs):

        start_time = time()
        func = fn(*args, **kwargs)
        execution_time = time() - start_time

        '''
        log generation
        '''
        fn_name = fn.__name__
        parameters = inspect.signature(fn).parameters
        parameter_names = list(parameters.keys())

        kwargs_log = 'kwargs: '
        for k in kwargs:
            parameter_names.remove(k)
            kwargs_log += f'{k}={kwargs[k]}, '
        kwargs_log = kwargs_log[0:-2]

        args_log = 'args: '
        for i in range(len(parameter_names)):
            args_log += f'{parameter_names[i]}={args[i]}, '
        args_log = args_log[0:-2]

        into_log = f'{fn_name}; {args_log}; {kwargs_log}; execution time: {execution_time} sec. \n'

        '''
        writing to file
        '''
        file = open('log.txt', 'a')
        file.write(into_log)
        file.close()

        return func
    return wrapper
