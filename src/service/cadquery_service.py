import uuid
import os
import cadquery as cq
import asyncio


class CadQueryService:

    def __init__(self):
        self.__output_dir = "files"
        os.makedirs(self.__output_dir, exist_ok=True)

    async def generate_cylinder(
        self,
        diameter: float,
        length: float,
        hole: float
    ) -> str:
        return await asyncio.to_thread(
            self.__generate_cylinder_sync,
            diameter,
            length,
            hole
        )

    async def generate_bolt(
        self,
        diameter: float,
        length: float,
        head_height: float,
        head_size: float,
        hole: float
    ) -> str:
        return await asyncio.to_thread(
            self.__generate_bolt_sync,
            diameter,
            length,
            head_height,
            head_size,
            hole
        )

    def __generate_cylinder_sync(
        self,
        diameter: float,
        length: float,
        hole: float
    ) -> str:
        part = (
            cq.Workplane("XY")
            .circle(diameter / 2)
            .extrude(length)
            .faces(">Z")
            .workplane()
            .hole(hole)
        )

        return self.__export(part)

    def __generate_bolt_sync(
        self,
        diameter: float,
        length: float,
        head_height: float,
        head_size: float,
        hole: float
    ) -> str:
        shaft = (
            cq.Workplane("XY")
            .circle(diameter / 2)
            .extrude(length)
        )

        head = (
            cq.Workplane("XY")
            .polygon(6, head_size)
            .extrude(head_height)
            .translate((0, 0, length))
        )

        bolt = shaft.union(head)

        bolt = (
            bolt.faces(">Z")
            .workplane()
            .hole(hole, depth=length + head_height)
        )

        return self.__export(bolt)

    def __export(self, part) -> str:
        file_path = os.path.join(
            self.__output_dir,
            f"{uuid.uuid4()}.stl"
        )

        cq.exporters.export(part, file_path)
        return file_path