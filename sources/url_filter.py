class UrlFilter:

    def valid(

        self,

        source

    ):

        return source["url"].startswith(

            "https://"

        )
