from os import walk
from os.path import splitext
from pydub import AudioSegment, effects
import pathlib

cwd = pathlib.Path.cwd()
input_folder = cwd / 'input'
output_folder = cwd / 'output'

if not output_folder.exists():
  output_folder.mkdir(exist_ok=True)

supported_formats = [".mp3", ".wav", ".aac", ".flac", ".ogg"]

def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
 
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
 
def get_file_list(path):  
  f = []
  for (dirpath, dirnames, filenames) in walk(path):
      f.extend(filenames)
      break
  return f

inputs = get_file_list(input_folder)
  
for (filename) in inputs:
  extension = splitext(filename)[1]
  if extension in(supported_formats):
    inputFile = input_folder/filename
    outputFile = output_folder/filename
    rawsound = AudioSegment.from_file(inputFile, extension[1:])
    normalized = effects.normalize(rawsound)
    normalized.export(outputFile, format=extension[1:]) 
    prGreen("Success: Normalized " + filename)
  else:
    prYellow("Warning:")
    prYellow(filename + " is not an audio file. Skipping...")
    print("Supported formats: " + "|".join(str(format[1:]) for format in supported_formats))
    continue

prGreen("All audio files have been normalized")
input("Press Enter to quit...")
