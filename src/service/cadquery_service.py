import uuid
import os
import cadquery as cq
import asyncio


class CadQueryService:

    def __init__(self):
        self.__output_dir = "files"

        if not os.path.exists(self.__output_dir):
            os.makedirs(self.__output_dir)

    async def generate(self, diameter: float, length: float, hole: float) -> str:
        return await asyncio.to_thread(
            self.__generate_sync, diameter, length, hole
        )

    def __generate_sync(self, diameter: float, length: float, hole: float) -> str:

        part = (
            cq.Workplane("XY")
            .circle(diameter / 2)
            .extrude(length)
            .faces(">Z")
            .workplane()
            .hole(hole)
        )

        file_id = str(uuid.uuid4())
        file_name = f"{file_id}.stl"
        file_path = os.path.join(self.__output_dir, file_name)

        cq.exporters.export(part, file_path)

        return file_path