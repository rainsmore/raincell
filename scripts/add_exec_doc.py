"""Add #| exec_doc to all code cells in a notebook that don't already have it."""
import sys
import nbformat

# Get notebook path from command line
if len(sys.argv) < 2:
    print("Usage: python add_exec_doc.py <notebook_path>")
    sys.exit(1)

nb_path = sys.argv[1]

# Read notebook
nb = nbformat.read(nb_path, as_version=4)

modified = False
for cell in nb.cells:
    if cell.cell_type == 'code' and cell.source:
        cell_code = cell.source.strip()
        
        # Skip nbdev_export calls (these are for exports only)
        if "nbdev_export" in cell_code:
            continue
            
        lines = cell_code.split('\n')
        first_content = lines[0] if lines else ''
        
        # Skip cells with existing nbdev directives that shouldn't have exec_doc
        if first_content.startswith('#|') and any(directive in first_content for directive in 
                                                  ['exec_doc', 'exporti', 'default_exp', 'export']):
            continue
            
        if not cell.source.strip():
            continue  # Empty cell
            
        # Add exec_doc directive at the beginning
        cell.source = '#| exec_doc\n' + cell.source
        modified = True

if modified:
    nbformat.write(nb, nb_path)
    print(f"Modified: {nb_path}")
else:
    print(f"Skipped: {nb_path}")