from os import walk
from os.path import splitext
from pydub import AudioSegment, effects

input_path = './input/'
output_path = './output/'
supported_formats = [".mp3", ".wav", ".aac", ".flac", ".ogg"]

def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
 
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
 
def get_file_list(path = "."):  
  f = []
  for (dirpath, dirnames, filenames) in walk(path):
      f.extend(filenames)
      break
  return f

inputs = get_file_list(input_path)
  
for (filename) in inputs:
  extension = splitext(filename)[1]
  if extension in(supported_formats):
    rawsound = AudioSegment.from_file(input_path + filename, extension[1:])
    normalized = effects.normalize(rawsound)
    normalized.export(output_path + filename, format=extension[1:]) 
    prGreen("Success: Normalized " + filename)
  else:
    prYellow("Warning:")
    prYellow(filename + " is not an audio file. Skipping...")
    print("Supported formats: " + "|".join(str(format[1:]) for format in supported_formats))
    continue

