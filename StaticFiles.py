import os

def readFiles(path):
    try:
        if path is None:
            raise ValueError("Path cannot be None")
        
        files = os.listdir(path)
        return files
    except Exception as e:
        print(f"Error reading directory: {e}")
        return []

if __name__ == "__main__":
    path = "your_directory_path_here"  # Replace with actual path
    names = readFiles(path)
    print(names)
