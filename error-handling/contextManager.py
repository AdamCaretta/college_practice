class File:
    def __init__(self, file_path, method):
        self.file_obj = open(file_path, method)
        print("Opening File...")

    def __enter__(self):
        print("Entering the context")
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Leaving the context")
        if exc_type:
            print(
                "\texc_type:", exc_type, "\n\texc_val:", exc_val, "\n\texc_tb:", exc_tb
            )

        self.file_obj.close()
        return True


if __name__ == "__main__":
    with File(__file__, "r") as f:
        print("Inside the context")
        raise IndexError("My nasty bug")
    print("Outside the context")
