import os
BASE_DIR= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print('Location of static',os.path.join(BASE_DIR, 'static'))