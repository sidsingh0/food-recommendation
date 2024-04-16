import glob
import os

#script to import all the controllers automatically to app.py
__all__=[os.path.basename(p)[:-3] for p in glob.glob(os.path.dirname(__file__)+"/*py")]
