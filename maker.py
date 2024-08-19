import os
class maker:
    def __init__(self, project_name):
        self.project_name = project_name
    def construct(project_name):
        # code to construct the project
        folders = [
        'src/assets', 
        'src/components', 
        'src/services', 
        'src/utils', 
        'src/styles', 
        'src/config', 
        'src/models', 
        'tests/unit', 
        'tests/integration', 
        'docs', 
        'scripts', 
        'build', 
        'public'
    ]
        os.makedirs(project_name,exist_ok=True)
        for folder in folders:
            os.makedirs(os.path.join(project_name,folder),exist_ok=True)
            open(os.path.join(project_name,'.gitignore'),'w').close()
            open(os.path.join(project_name,'readme.md'),'w').close()
            try:
                print(f"Project {project_name} created ")
            except Exception as e:
                print(f"Error creating project {project_name}: {e}")
