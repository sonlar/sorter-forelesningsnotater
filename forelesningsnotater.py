import os
filer = os.listdir('./')

for filnavn in filer:
    plassering = os.path.join('./', filnavn)

    if filnavn.endswith('.ipynb') or filnavn.startswith('F0') and filnavn.endswith('pdf'):
        mappe = os.path.join(
            'C:/OneDrive/OneDrive - University of Bergen/INFO132/Forelesningsnotater', filnavn)
        os.rename(plassering, mappe)

    elif filnavn.endswith('.pdf') and filnavn.startswith('INFO100'):
        mappe = os.path.join(
            'C:/OneDrive/OneDrive - University of Bergen/INFO100/Forelesningsnotater', filnavn)
        os.rename(plassering, mappe)
