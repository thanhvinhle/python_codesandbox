import subprocess

def run_main():
    try:
        # Replace 'python' with 'python3' if you're using Python 3.x
        subprocess.run(['python', 'neetcode.py'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    run_main()
