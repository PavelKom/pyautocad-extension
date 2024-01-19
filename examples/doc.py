from pyautocad_extension import acad_app, acad_docs

# When importing acad_app will automatically try to open the AutoCAD application

# Creating new document

new_doc = acad_docs.add() # Default template
print(new_doc.name)

# Get full name. Return empty string because document not saved
print(new_doc.fullname)

# Close ALL opened documents WITHOUT saving
acad_docs.close()

acad_app.eval("""Debug.Print "Hello from Python" """")
