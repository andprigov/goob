class HtmlParser:

    def title(

        self,

        html

    ):

        start = html.find("<title>") + 7

        end = html.find("</title>")

        return html[start:end]
