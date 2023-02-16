import zipfile

with zipfile.ZipFile('data/dialnarr_metadata.zip') as zf:
    zf.extractall("data/")

with zipfile.ZipFile('data/dialnarr_txt.zip') as zf:
    zf.extractall("data/")