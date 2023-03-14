import supervisely as sly
import os
from dotenv import load_dotenv

if sly.is_development():
    load_dotenv(os.path.expanduser("~/supervisely.env"))
    load_dotenv("local.env")

api = sly.Api.from_env()
workspace_id = sly.env.workspace_id()
project_id = sly.env.project_id()

project_info = api.project.get_info_by_id(project_id)
project_meta = api.project.get_meta(project_id)  # classes and tags

new_project = api.project.create(
    workspace_id=workspace_id,
    name=project_info.name + "_new",
    type=project_info.type,
    change_name_if_conflict=True,
)

# upload classes and tags into new project on server
api.project.update_meta(new_project.id, project_meta)

print(f"New project [id={new_project.id}] has been successfully created")
print(f"And initialized with these classes and tags:")
print(project_meta)

sly.output.set_project()
