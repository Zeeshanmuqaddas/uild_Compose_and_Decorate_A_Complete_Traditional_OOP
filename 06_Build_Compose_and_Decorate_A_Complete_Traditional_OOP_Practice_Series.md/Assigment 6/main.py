class Logger:
    def __init__(self):
        print("Logger object created.")

    def __del__(self):
        print("Logger object destroyed.")


# Example usage:
logger = Logger()  # Prints: Logger object created.
del logger         # Prints: Logger object destroyed.
