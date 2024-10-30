from src.main_dir.main import Main
import os
import sys
import subprocess

if __name__ == "__main__":
    main = Main()
    latest_version = main.check_for_update()
    print(f"Latest version: {latest_version}")
    main.clone_or_pull()
    loop = True
    while loop:
        try:
            subprocess.run('python src/clone/run.py', check=True)
            loop = False
        except ModuleNotFoundError as ex:
            print('Broooo')
            loop = False
        except Exception as ex:
            print('Exception', ex)
    input()
