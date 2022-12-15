from typing import Any, Type, Union

from pydantic import BaseModel, create_model

from mlem.core.data_type import DataSerializer, DataType


class AddSerializer(DataSerializer):
    def serialize(self, data_type: DataType, instance: Any):
        data = data_type.serialize(instance)
        data["metadata"] = {"add": 0}
        return data

    def deserialize(self, data_type: DataType, obj) -> Any:
        data = data_type.deserialize({"values": obj["values"]})
        add = obj["metadata"]["add"]
        data["Age"] += add
        return data

    def get_model(self, data_type: DataType, prefix: str = "") -> Union[
        Type[BaseModel], type]:
        default_model = data_type.get_model(prefix)

        class MetaddataModel(BaseModel):
            add: int = 0

        default_type = default_model.__fields__["values"].outer_type_
        default_value = default_model.__fields__["values"].default
        return create_model("AddModel", **{
            "values": (default_type, default_value),
            "metadata": (MetaddataModel, ...)
        })
