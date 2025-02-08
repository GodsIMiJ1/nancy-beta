# create_procfile.py
with open('Procfile', 'w') as f:
    f.write('web: gunicorn enhanced_effects:app')
print("Procfile created successfully!")
