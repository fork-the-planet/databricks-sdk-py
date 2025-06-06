import time

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

created = w.model_registry.create_model(name=f"sdk-{time.time_ns()}")

model = w.model_registry.get_model(name=created.registered_model.name)

w.model_registry.update_model(
    name=model.registered_model_databricks.name,
    description=f"sdk-{time.time_ns()}",
)
