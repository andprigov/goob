import json

class JsonWriter:

    def save(

        self,

        records,

        filename

    ):

        with open(

            filename,

            "w",

            encoding="utf-8"

        ) as file:

            json.dump(

                records,

                file,

                indent=4

            )
