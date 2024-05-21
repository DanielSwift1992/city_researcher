from langchain.tools import tool


class FileTools:
    @tool("Write File with content")
    def write_file(data, relative_path):
        """Useful to write a file to a given relative path with the given content.
        The input to this tool should be the content you want to write to the file,
        and the relative path of the file, excluding the /workdir prefix.
        For example, `notes.txt|This is the content`.
        Replace 'This is the content' with the actual content you want to write to the file."""
        try:
            path = (
                f"./workdir/{relative_path}".replace("\n", "")
                .replace(" ", "")
                .replace("`", "")
            )
            with open(path, "w") as f:
                f.write(data)
            return f"File written to {path}."
        except Exception:
            return "Error with the input format for the tool."

    @tool("Read File content")
    def read_file(relative_path):
        """Useful to read a file from a given relative path.
        The input to this tool should be the relative path of the file, excluding the /workdir prefix.
        For example, `notes.txt`.
        Returns the content of the file as a string."""
        try:
            path = (
                f"./workdir/{relative_path}".replace("\n", "")
                .replace(" ", "")
                .replace("`", "")
            )
            with open(path, "r") as f:
                content = f.read()
            return content
        except Exception:
            return "Error reading the file. Check if the path is correct."
