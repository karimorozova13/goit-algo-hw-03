from pathlib import Path
import shutil

def save_files(from_dir:Path, to_dir:Path):
    try:
    
            # if directory exists, doesn't raise the exception or create new directory
        to_dir.mkdir(parents=True, exist_ok=True)
        
        for file_path in from_dir.iterdir():
                try:
                    # check if it's file, not directory
                    if file_path.is_file():
                        
                        extension = file_path.suffix
                        
                        # create subdirectory path
                        subdirectory_path = to_dir / extension.replace('.', '')
                        subdirectory_path.mkdir(parents=True, exist_ok=True)
                            
                        # copy files to correct directories
                        destination_path = subdirectory_path / file_path.name
                        shutil.copy2(file_path, destination_path)
                        
                    # check each file inside subdirectory
                    else:
                        save_files(file_path, to_dir)
                except (PermissionError, FileNotFoundError) as e:
                    print(f"Error processing file {file_path}: {e}")
    except (PermissionError, FileNotFoundError) as e:
        print(f"Error accessing destination directory {to_dir}: {e}")
                    
            
    
def parse_input(user_input):
    l = user_input.split()
    
    from_dir = l[0]
    to_dir = 'dist' if len(l) == 1 else l[1]
    
    return from_dir, to_dir

def main():
    user_input =input("Please, add source directory and path where to copy files >>>>>")
    from_dir, to_dir = parse_input(user_input) 
   
    root = Path(from_dir)
    output_dir = Path(to_dir)
    
    save_files(root,output_dir)
    

if __name__ == '__main__':
    
    main()