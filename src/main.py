import supervisely as sly
import os
from dotenv import load_dotenv

if sly.is_development():
    load_dotenv("local.env")
    load_dotenv(os.path.expanduser("~/supervisely.env"))

api = sly.Api.from_env()
workspace_id = sly.env.workspace_id()
project_id = sly.env.project_id()

initial_project_meta = api.project.get_meta(project_id)
initial_project_info = api.project.get_info_by_id(project_id)

new_project = api.project.create(
    workspace_id=workspace_id,
    name=initial_project_info.name,
    type=initial_project_info.type,
    change_name_if_conflict=True,
)

new_meta = api.project.update_meta(new_project.id, initial_project_meta)

print(
    f"New project with initial project meta has been successfully created. New project id: {new_project.id}"
)
