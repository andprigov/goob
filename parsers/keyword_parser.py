import re

class KeywordParser:

    def extract(

        self,

        html

    ):

        words = re.findall(

            r"[A-Za-z]{5,}",

            html

        )

        return sorted(

            set(

                word.lower()

                for word in words

            )

        )[:6]
